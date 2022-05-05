#
# Copyright (c) 2022 National Motor Freight Traffic Association Inc. All Rights Reserved.
# See the file "LICENSE" for the full license governing this code.
#
import os
import re
from pathlib import Path
from typing import Optional, List, Tuple, Any, Union

import defusedxml
from defusedxml.common import EntitiesForbidden
import xlrd
import xlwt

from backend.excel.import_.excel_to_sdoc_converter import ExcelToSDocConverter
from strictdoc.backend.sdoc.writer import SDWriter


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
    all_columns_to_preserve: list

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

    @staticmethod
    def header_rename(header_name):
        header_name = TsrmExcelPreparer.safe_name(header_name)
        if "PUBLIC_REQUIREMENTS_REFERENCES_OR_DESCRIPTIONS" in header_name:
            return "Pub_Refs"
        elif "VERIFICATION_INSPECTION__DEMONSTRATION__TEST__OR_ANALYSIS" in header_name:
            return "Verification"
        else:
            return header_name

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
            if row_num_in == 0:
                value = self.header_rename(value)
            out_sheet.write(row_num_out, column_num_out, value)
            column_num_out = column_num_out + 1

    def create_filtered_workbook(self, predicate_column, output_xls):
        out_book = xlwt.Workbook()
        out_sheet = out_book.add_sheet('dummy name')
        self.copy_preserved_columns(0, 0, out_sheet)

        out_row = 1
        for row_num in range(self.header_row_num + 1, self.first_sheet.nrows):
            if predicate_column is None or self.first_sheet.row_values(row_num)[predicate_column].startswith('Yes'):
                self.copy_preserved_columns(row_num, out_row, out_sheet)
                out_row = out_row + 1

        out_book.save(output_xls)

    def create_stub_workbook(self, predicate_column, prefix, output_xls):
        out_book = xlwt.Workbook()
        out_sheet = out_book.add_sheet('dummy name')
        out_sheet.write(0, 0, "UID")
        out_sheet.write(0, 1, "Requirement")
        out_sheet.write(0, 2, "Parent")

        ref_column = self.get_any_header_column("REF_#")
        assert ref_column != -1

        predicate_label = self.first_sheet.row_values(self.header_row_num)[predicate_column].strip()

        out_row = 1
        for row_num in range(self.header_row_num + 1, self.first_sheet.nrows):
            if predicate_column is None or self.first_sheet.row_values(row_num)[predicate_column].startswith('Yes'):
                parent_uid = self.first_sheet.row_values(row_num)[ref_column].strip()

                out_sheet.write(out_row, 0, f"{prefix}-{parent_uid}")
                out_sheet.write(out_row, 1, f"This {predicate_label} component must satisfy requirement {parent_uid}")
                out_sheet.write(out_row, 2, parent_uid)
                out_row = out_row + 1

        out_book.save(output_xls)

    def do_prep(self):
        self.identify_all_columns()
        Path('out').mkdir(parents=True, exist_ok=True)

        self.create_filtered_workbook(None, 'out/main_tsrm.xls')

        self.create_stub_workbook(self.mobile_app_yn_column, 'MOBILE', 'out/mobile_app_tsrm.xls')
        self.create_stub_workbook(self.vehicle_connection_yn_column, 'VEH', 'out/vehicle_connection_tsrm.xls')
        self.create_stub_workbook(self.connectivity_comms_yn_column, 'COMMS', 'out/connectivity_tsrm.xls')
        self.create_stub_workbook(self.cloud_yn_column, 'CLOUD', 'out/cloud_tsrm.xls')
        return


def sdoc_to_fragment(filename):
    with open(filename, 'r') as f:
        text = f.read()
    text = "[FRAGMENT]\n\n" + text[text.index("[REQUIREMENT]"):]
    with open(filename, 'w') as f:
        f.write(text)


def append_include(to_filename, inc_filename, section_title):
    with open(to_filename, 'a', encoding='utf-8') as f:
        f.write(f"\n[SECTION]\nTITLE: {section_title}\n\n[FRAGMENT_FROM_FILE]\nFILE: {inc_filename}\n\n[/SECTION]\n")


# create:
# a) one sheet per applicable component with parent references and stub text (x4) and:
# b) a master sheet with everything but the component applicabilities
#    TODO: also split tests into sub-requirements
TsrmExcelPreparer('tsrm.xls').do_prep()

# convert the master sheet to sdoc
write_document(ExcelToSDocConverter.convert('out/main_tsrm.xls',
                                            "NMFTA Telematics Security Requirements Matrix"
                                            ), 'out/00_tsrm.sdoc')

# convert each component sheet to an sdoc
write_document(ExcelToSDocConverter.convert('out/mobile_app_tsrm.xls',
                                            "NMFTA Telematics (Mobile App Component) Security Requirements"
                                            ), 'out/mobile_app_tsrm.sinc')
write_document(ExcelToSDocConverter.convert('out/vehicle_connection_tsrm.xls',
                                            "NMFTA Telematics (Vehicle Connection Component) Security Requirements"
                                            ), 'out/vehicle_connection_tsrm.sinc')
write_document(ExcelToSDocConverter.convert('out/connectivity_tsrm.xls',
                                            "NMFTA Telematics (Connectivity or Communications Component) Security Requirements"
                                            ), 'out/connectivity_tsrm.sinc')
write_document(ExcelToSDocConverter.convert('out/cloud_tsrm.xls',
                                            "NMFTA Telematics (Cloud Component) Security Requirements"
                                            ), 'out/cloud_tsrm.sinc')

# replace the [DOCUMENT]...[GRAMMAR].... stuff with [FRAGMENT] in the .sinc files
for f in ['out/mobile_app_tsrm.sinc',
          'out/vehicle_connection_tsrm.sinc',
          'out/connectivity_tsrm.sinc',
          'out/cloud_tsrm.sinc']:
    sdoc_to_fragment(f)

append_include('out/00_tsrm.sdoc', 'cloud_tsrm.sinc', "NMFTA Telematics (Cloud Component) Security Requirements")
append_include('out/00_tsrm.sdoc', 'connectivity_tsrm.sinc', "NMFTA Telematics (Connectivity or Communications Component) Security Requirements")
append_include('out/00_tsrm.sdoc', 'vehicle_connection_tsrm.sinc', "NMFTA Telematics (Vehicle Connection Component) Security Requirements")
append_include('out/00_tsrm.sdoc', 'mobile_app_tsrm.sinc', "NMFTA Telematics (Mobile App Component) Security Requirements")
