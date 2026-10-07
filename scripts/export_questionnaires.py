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

    def export(self) -> None:
        assert self.traceability_index is not None

        output_dir = self.project_config.output_dir or "docs/html"
        os.makedirs(output_dir, exist_ok=True)
        workbook_path = os.path.join(output_dir, "vcr_questionnaires.xlsx")

        fields = [
            "UID",
            "Criticality",
            "Title / Statement",
            "Yes",
            "In-Part",
            "No",
            "N/A",
            "Notes",
        ]
        column_widths = ExcelGenerator._init_columns_width(fields)
        column_widths["Title / Statement"].update(
            {"max_width": column_widths["Title / Statement"]["max_width"] * 5}
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
                document_iterator = SDocDocumentIterator(document)
                req_nodes = []
                for node, _ in document_iterator.all_content(print_fragments=False):
                    if isinstance(node, SDocNode) and node.node_type == "REQUIREMENT":
                        req_nodes.append(node)

                # Skip overview or descriptive documents that do not define requirements
                if not req_nodes:
                    continue

                sheet_title = document.title[:31].replace(":", "-").replace("/", "-")
                worksheet = workbook.add_worksheet(name=sheet_title)

                for idx, field in enumerate(fields):
                    worksheet.write(0, idx, field)

                # Sort by criticality descending
                def sort_key(node: SDocNode):
                    crit_val = node.get_meta_field_value_by_title("CRITICALITY")
                    if crit_val:
                        crit_val = crit_val.strip()
                    else:
                        crit_val = "None"
                    return criticality_order.get(crit_val, 0)

                req_nodes.sort(key=sort_key, reverse=True)

                row = 0
                for row, node in enumerate(req_nodes):
                    uid = node.reserved_uid or ""
                    crit_raw = node.get_meta_field_value_by_title("CRITICALITY")
                    crit = crit_raw.strip() if crit_raw else ""

                    stmt_raw = node.get_meta_field_value_by_title("STATEMENT")
                    stmt = stmt_raw.strip() if stmt_raw else ""

                    title_raw = node.get_meta_field_value_by_title("TITLE")
                    title = title_raw.strip() if title_raw else ""

                    display_text = f"{title}\n{stmt}" if title else stmt

                    worksheet.write(row + 1, 0, uid, wrap_format)
                    worksheet.write(row + 1, 1, crit, wrap_format)
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
