#
# Copyright (c) 2022 National Motor Freight Traffic Association Inc. All Rights Reserved.
# See the file "LICENSE" for the full license governing this code.
#
import os
from pathlib import Path
from typing import Optional, List, Tuple, Any, Union

import defusedxml
from defusedxml.common import EntitiesForbidden
import xlrd
import xlwt

from strictdoc.backend.sdoc.models.document import Document
from strictdoc.backend.sdoc.models.document_config import DocumentConfig
from strictdoc.backend.sdoc.models.document_grammar import DocumentGrammar, GrammarElement
from strictdoc.backend.sdoc.models.object_factory import SDocObjectFactory
from strictdoc.backend.sdoc.models.requirement import RequirementField, Requirement
from strictdoc.backend.sdoc.models.type_system import GrammarElementFieldString
from strictdoc.backend.sdoc.writer import SDWriter


class ExcelConverter:
    extra_header_pairs: list[tuple[int, str]]
    criticality_column: int
    title_column: int
    comment_column: int
    uid_column: int
    statement_column: int

    def __init__(self, excel_file):
        defusedxml.defuse_stdlib()

        self.excel_workbook = self.secure_open_workbook(filename=excel_file, on_demand=True)
        self.first_sheet = self.excel_workbook.sheet_by_index(0)
        self.header_row_num = self.lookup_header_row_num()
        assert self.header_row_num is not None

    @staticmethod
    def secure_open_workbook(**kwargs):
        try:
            return xlrd.open_workbook(**kwargs)
        except EntitiesForbidden:
            raise ValueError('Please use an excel file without XEE')

    def lookup_header_row_num(self):
        for i in range(16):  # the first 16 rows should do ¯\_(ツ)_/¯
            if self.first_sheet.row_values(0)[0].strip() != '':
                return i
        return None

    def get_safe_header_row(self):
        header_row = self.first_sheet.row_values(self.header_row_num)
        header_row = list(map(lambda x: self.safe_name(x), header_row))
        return header_row

    def get_any_header_column(self, header_texts):
        if not isinstance(header_texts, list):
            header_texts = [header_texts]
        for t in header_texts:
            try:
                return self.get_safe_header_row().index(t)
            except ValueError:
                continue
        return -1

    @staticmethod
    def safe_name(x):
        x = x.splitlines()[0]
        x = x.strip()
        x = x.upper()
        x = x.replace(':', '')
        x = x.replace('+', '')
        x = x.replace(',', '_')
        x = x.replace(' ', '_')
        x = x.replace('-', '_')
        x = x.replace('/', '_OR_')
        return x

    def convert(self, out_dir, title):
        self.identify_all_columns()
        self.validate_all_required_columns()

        document = self.create_document(title)
        for i in range(self.header_row_num + 1, self.first_sheet.nrows):
            template_requirement = self.create_template_requirement_from_well_known_columns(document, i)
            requirement = self.extend_requirement_with_extra_columns(template_requirement, i)
            document.section_contents.append(requirement)

        self.write_document(document, out_dir)
        return

    def identify_all_columns(self):
        all_header_columns = list(range(self.first_sheet.ncols))

        self.statement_column = self.get_any_header_column(['REQUIREMENT', 'STATEMENT'])
        if self.statement_column != -1:
            all_header_columns.remove(self.statement_column)
        self.uid_column = self.get_any_header_column(['REF', 'REF #', 'REF_#', 'REFDES', 'ID', 'UID'])
        if self.uid_column != -1:
            all_header_columns.remove(self.uid_column)
        self.comment_column = self.get_any_header_column(['REMARKS', 'COMMENT'])
        if self.comment_column != -1:
            all_header_columns.remove(self.comment_column)
        self.title_column = self.get_any_header_column(['TITLE', 'NAME'])
        if self.title_column != -1:
            all_header_columns.remove(self.title_column)

        header_row = self.get_safe_header_row()
        self.extra_header_pairs = list(map(lambda x: (x, header_row[x]), all_header_columns))

    def validate_all_required_columns(self):
        assert self.statement_column != -1

    def create_document(self, title: Optional[str]) -> Document:
        document_config = DocumentConfig(
            parent=None,
            version=None,
            number=None,
            markup=None,
            auto_levels=None,
        )
        document_title = title if title else "<No title>"
        document = Document(None, document_title, document_config, None, [], [])

        fields = DocumentGrammar.create_default(document).elements[0].fields
        for i, name in self.extra_header_pairs:
            fields.extend([
                GrammarElementFieldString(parent=None,
                                          title=name,
                                          required="False"),
            ])

        requirements_element = GrammarElement(parent=None, tag="REQUIREMENT", fields=fields)
        elements = [requirements_element]
        grammar = DocumentGrammar(parent=document, elements=elements)
        document.grammar = grammar
        return document

    def create_template_requirement_from_well_known_columns(self, document, row_num):
        row_values = self.first_sheet.row_values(row_num)
        statement = row_values[self.statement_column]
        uid = None
        if self.uid_column != -1:
            uid = row_values[self.uid_column].strip()
        title = None
        if self.title_column != -1:
            title = row_values[self.title_column].strip()
        comments = None
        if self.comment_column != -1:
            comment = row_values[self.comment_column].strip()
            if comment == '' or comment == '-':
                comments = None
            else:
                comments = [comment]
        template_requirement = SDocObjectFactory.create_requirement(document,
                                                                    requirement_type="REQUIREMENT",
                                                                    title=title,
                                                                    uid=uid,
                                                                    level=None,
                                                                    statement=None,
                                                                    statement_multiline=statement,
                                                                    rationale=None,
                                                                    rationale_multiline=None,
                                                                    tags=None,
                                                                    comments=comments
                                                                    )
        return template_requirement

    def extend_requirement_with_extra_columns(self, template_requirement, row_num):
        row_values = self.first_sheet.row_values(row_num)
        fields = template_requirement.fields
        for i, name in self.extra_header_pairs:
            value = row_values[i].strip()
            if value != '':
                fields.append(RequirementField(parent=None,
                                               field_name=name,
                                               field_value=None,
                                               field_value_multiline=value,
                                               field_value_references=None,
                                               ))
        requirement = Requirement(parent=template_requirement.parent,
                                  requirement_type=template_requirement.requirement_type,
                                  fields=fields)
        requirement.ng_level = 1
        return requirement

    @staticmethod
    def write_document(document, output_path):
        document_content = SDWriter().write(document)
        output_folder = os.path.dirname(output_path)
        Path(output_folder).mkdir(parents=True, exist_ok=True)
        with open(
            output_path, "w", encoding="utf8"
        ) as output_file:
            output_file.write(document_content)


class TsrmExcelPreparer:
    cloud_yn_column: int
    connectivity_comms_yn_column: int
    vehicle_connection_yn_column: int
    mobile_app_yn_column: int
    all_columns_to_preserve: list[int]

    def __init__(self, excel_file):
        defusedxml.defuse_stdlib()

        self.excel_workbook = self.secure_open_workbook(filename=excel_file, on_demand=True)
        self.first_sheet = self.excel_workbook.sheet_by_index(0)
        self.header_row_num = self.lookup_header_row_num()
        assert self.header_row_num is not None

    @staticmethod
    def secure_open_workbook(**kwargs):
        try:
            return xlrd.open_workbook(**kwargs)
        except EntitiesForbidden:
            raise ValueError('Please use an excel file without XEE')

    def lookup_header_row_num(self):
        for i in range(16):  # the first 16 rows should do ¯\_(ツ)_/¯
            if self.first_sheet.row_values(0)[0].strip() != '':
                return i
        return None

    def get_safe_header_row(self):
        header_row = self.first_sheet.row_values(self.header_row_num)
        header_row = list(map(lambda x: self.safe_name(x), header_row))
        return header_row

    def get_any_header_column(self, header_texts):
        if not isinstance(header_texts, list):
            header_texts = [header_texts]
        for t in header_texts:
            try:
                return self.get_safe_header_row().index(t)
            except ValueError:
                continue
        return -1

    @staticmethod
    def safe_name(x):
        x = x.splitlines()[0]
        x = x.strip()
        x = x.upper()
        x = x.replace(':', '')
        x = x.replace('+', '')
        x = x.replace(',', '_')
        x = x.replace(' ', '_')
        x = x.replace('-', '_')
        x = x.replace('/', '_OR_')
        return x

    def identify_all_columns(self):
        self.all_columns_to_preserve = list(range(self.first_sheet.ncols))

        derived_applicable_components_column = self.get_any_header_column('APPLICABLE_COMPONENT_CATEGORIES')
        assert derived_applicable_components_column != -1
        self.all_columns_to_preserve.remove(derived_applicable_components_column)

        derived_combined_etal_column = self.get_any_header_column('COMBINED_REF__SECURITY_CONTROL__REQUIREMENT')
        assert derived_combined_etal_column != -1
        self.all_columns_to_preserve.remove(derived_combined_etal_column)

        self.mobile_app_yn_column = self.get_any_header_column('MOBILE_APP')
        assert self.mobile_app_yn_column != -1
        self.all_columns_to_preserve.remove(self.mobile_app_yn_column)

        self.vehicle_connection_yn_column = self.get_any_header_column('VEHICLE_CONNECTION')
        assert self.vehicle_connection_yn_column != -1
        self.all_columns_to_preserve.remove(self.vehicle_connection_yn_column)

        self.connectivity_comms_yn_column = self.get_any_header_column('CONNECTIVITY_OR_COMMUNICATIONS')
        assert self.connectivity_comms_yn_column != -1
        self.all_columns_to_preserve.remove(self.connectivity_comms_yn_column)

        self.cloud_yn_column = self.get_any_header_column('CLOUD_OR_BACK_END')
        assert self.cloud_yn_column != -1
        self.all_columns_to_preserve.remove(self.cloud_yn_column)

    def copy_preserved_columns(self, row_num_in, row_num_out, out_sheet):
        column_num_out = 0
        for value in map(lambda x: self.first_sheet.row_values(row_num_in)[x], self.all_columns_to_preserve):
            out_sheet.write(row_num_out, column_num_out, value)
            column_num_out = column_num_out + 1

    def create_filtered_workbook(self, predicate_column, output_xls):
        out_book = xlwt.Workbook()
        out_sheet = out_book.add_sheet('dummy name')
        self.copy_preserved_columns(0, 0, out_sheet)

        out_row = 1
        for row_num in range(self.header_row_num + 1, self.first_sheet.nrows):
            if self.first_sheet.row_values(row_num)[predicate_column].startswith('Yes'):
                self.copy_preserved_columns(row_num, out_row, out_sheet)
                out_row = out_row + 1

        out_book.save(output_xls)

    def do_prep(self):
        self.identify_all_columns()
        Path('out').mkdir(parents=True, exist_ok=True)

        self.create_filtered_workbook(self.mobile_app_yn_column, 'out/mobile_app_tsrm.xls')
        self.create_filtered_workbook(self.vehicle_connection_yn_column, 'out/vehicle_connection_tsrm.xls')
        self.create_filtered_workbook(self.connectivity_comms_yn_column, 'out/connectivity_tsrm.xls')
        self.create_filtered_workbook(self.cloud_yn_column, 'out/cloud_tsrm.xls')
        return


TsrmExcelPreparer('tsrm.xls').do_prep()

ExcelConverter('out/mobile_app_tsrm.xls').convert(
    'out/mobile_app_tsrm.sdoc',
    "NMFTA Telematics (Mobile App Component) Security Requirements Matrix"
)
ExcelConverter('out/vehicle_connection_tsrm.xls').convert(
    'out/vehicle_connection_tsrm.sdoc',
    "NMFTA Telematics (Vehicle Connection Component) Security Requirements Matrix"
)
ExcelConverter('out/connectivity_tsrm.xls').convert(
    'out/connectivity_tsrm.sdoc',
    "NMFTA Telematics (Connectivity or Communications Component) Security Requirements Matrix"
)
ExcelConverter('out/cloud_tsrm.xls').convert(
    'out/cloud_tsrm.sdoc',
    "NMFTA Telematics (Cloud Component) Security Requirements Matrix"
)