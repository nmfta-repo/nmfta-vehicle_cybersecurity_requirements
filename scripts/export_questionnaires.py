import argparse
import os
import sys
from typing import Optional

import xlsxwriter
from strictdoc.api import (
    ALL_EDGES,
    DocumentTreeError,
    ExcelGenerator,
    GraphLinkType,
    Parallelizer,
    ProjectConfig,
    ProjectConfigLoader,
    SDocDocument,
    SDocDocumentIterator,
    SDocNode,
    TraceabilityIndex,
    TraceabilityIndexBuilder,
)


class ExportQuestionnaires:
    def __init__(self, project_config: ProjectConfig, parallelizer: Parallelizer):
        self.project_config = project_config
        self.parallelizer = parallelizer
        self.traceability_index: Optional[TraceabilityIndex] = None

    def build_index(self) -> None:
        try:
            traceability_index: TraceabilityIndex = (
                TraceabilityIndexBuilder.create(
                    project_config=self.project_config,
                    parallelizer=self.parallelizer,
                )
            )
            self.traceability_index = traceability_index
        except DocumentTreeError as exc:
            print(exc.to_print_message())  # noqa: T201
            sys.exit(1)

    def resolve_ancestor_meta(self, node: SDocNode):
        """
        Recursively look up criticality and statement from the requirement
        or its parent/ancestor nodes in the traceability graph.
        """
        assert self.traceability_index is not None

        crit = node.get_meta_field_value_by_title("CRITICALITY")
        title = node.get_meta_field_value_by_title("TITLE")
        stmt = node.get_meta_field_value_by_title("STATEMENT")

        current = node
        parents = self.traceability_index.graph_database.get_link_values(
            link_type=GraphLinkType.NODE_TO_PARENT_NODES,
            lhs_node=current,
            edge=ALL_EDGES,
        )

        parent_title = ""
        parent_stmt = ""
        while parents:
            p_node = parents[0]
            p_crit = p_node.get_meta_field_value_by_title("CRITICALITY")
            if not crit and p_crit:
                crit = p_crit

            p_t = p_node.get_meta_field_value_by_title("TITLE")
            if not parent_title and p_t:
                parent_title = p_t

            p_s = p_node.get_meta_field_value_by_title("STATEMENT")
            if p_s:
                parent_stmt = p_s

            parents = self.traceability_index.graph_database.get_link_values(
                link_type=GraphLinkType.NODE_TO_PARENT_NODES,
                lhs_node=p_node,
                edge=ALL_EDGES,
            )

        crit_str = crit.strip() if crit else "None"
        display_title = title.strip() if title else parent_title.strip()
        display_stmt = stmt.strip() if stmt else ""
        if parent_stmt and parent_stmt.strip() != display_stmt:
            if display_stmt:
                display_stmt = f"{display_stmt}\n\nParent Requirement Details:\n{parent_stmt.strip()}"
            else:
                display_stmt = parent_stmt.strip()

        display_text = f"{display_title}\n{display_stmt}" if display_title else display_stmt
        return crit_str, display_text

    def export(self) -> None:
        assert self.traceability_index is not None

        output_dir = self.project_config.output_dir or "docs/html"
        os.makedirs(output_dir, exist_ok=True)
        workbook_path = os.path.join(output_dir, "vcr_questionnaires.xlsx")

        fields = [
            "UID",
            "Criticality",
            "Requirement Specification",
            "Yes",
            "In-Part",
            "No",
            "N/A",
            "Notes",
        ]
        column_widths = ExcelGenerator._init_columns_width(fields)
        column_widths["Requirement Specification"].update(
            {"max_width": column_widths["Requirement Specification"]["max_width"] * 5}
        )
        column_widths["Notes"].update(
            {"max_width": column_widths["Notes"]["max_width"] * 4}
        )

        criticality_order = {"High": 3, "Medium": 2, "Low": 1, "None": 0}

        with xlsxwriter.Workbook(workbook_path) as workbook:
            workbook.set_properties(
                {
                    "title": "NMFTA Vehicle Cybersecurity Requirements Questionnaires",
                    "comments": (
                        "Created with StrictDoc from sources in "
                        "https://github.com/nmfta-repo/nmfta-vehicle_cybersecurity_requirements ."
                    ),
                }
            )
            wrap_format = workbook.add_format({"text_wrap": True})

            for document in self.traceability_index.document_tree.document_list:
                # Only generate worksheets for ECU Class specifications
                if not document.title.startswith("Class "):
                    continue

                document_iterator = SDocDocumentIterator(document)
                req_nodes = []
                for node, _ in document_iterator.all_content(print_fragments=False):
                    if isinstance(node, SDocNode) and node.node_type == "REQUIREMENT":
                        req_nodes.append(node)

                if not req_nodes:
                    continue

                sheet_title = document.title[:31].replace(":", "-").replace("/", "-")
                worksheet = workbook.add_worksheet(name=sheet_title)

                for idx, field in enumerate(fields):
                    worksheet.write(0, idx, field)

                # Sort by criticality descending
                def sort_key(node: SDocNode):
                    crit_str, _ = self.resolve_ancestor_meta(node)
                    return criticality_order.get(crit_str, 0)

                req_nodes.sort(key=sort_key, reverse=True)

                row = 0
                for row, node in enumerate(req_nodes):
                    uid = node.reserved_uid or ""
                    crit_str, display_text = self.resolve_ancestor_meta(node)

                    worksheet.write(row + 1, 0, uid, wrap_format)
                    worksheet.write(row + 1, 1, crit_str, wrap_format)
                    worksheet.write(row + 1, 2, display_text, wrap_format)

                if req_nodes:
                    worksheet.add_table(
                        0,
                        0,
                        row + 1,
                        len(fields) - 1,
                        {
                            "columns": ExcelGenerator._init_headers(fields),
                            "style": "Table Style Medium 4",
                        },
                    )

                ExcelGenerator._set_columns_width(
                    workbook, worksheet, column_widths, fields
                )

        print(f"Exported questionnaires to {workbook_path}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "export":
        sys.argv.pop(1)

    parser = argparse.ArgumentParser(
        description="Export questionnaires from SDoc documents."
    )
    parser.add_argument("input_path", type=str, help="Path to input path.")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="docs/html",
        help="Optional directory to save output.",
    )

    args = parser.parse_args()

    project_config = ProjectConfigLoader.load(
        input_path=args.input_path, output_dir=args.output_dir
    )
    parallelizer = Parallelizer.create(False)

    exporter = ExportQuestionnaires(
        project_config=project_config, parallelizer=parallelizer
    )
    exporter.build_index()
    exporter.export()
