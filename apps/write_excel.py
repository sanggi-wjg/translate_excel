import xlsxwriter

from apps.utils import ExcelWriteError


class WriteExcel:

    def write(self, write_data: list, path: str):
        workbook = xlsxwriter.Workbook(filename = path)
        sheet = workbook.add_worksheet()

        try:
            for data in write_data:
                sheet.write('{}{}'.format(data['column'], data['row']), data['translate'])

        except Exception:
            raise ExcelWriteError

        finally:
            workbook.close()
