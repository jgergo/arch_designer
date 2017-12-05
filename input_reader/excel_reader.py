from xlrd import open_workbook
# from typing import List


def read_excel_by_line(filename: str, sheet_name: str = "Sheet1"):
    with open_workbook(filename=filename) as wb:
        for sheet in wb.sheets():
            if sheet.name != sheet_name:
                continue
            for row in range(sheet.nrows):
                if row == 0:
                    continue
                row_value = []
                for col in range(sheet.ncols):
                    row_value.append(sheet.cell(row, col).value)
                yield row_value
