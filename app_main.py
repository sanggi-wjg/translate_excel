from pprint import pprint

from apps.chrome_driver import ChromeDriver
from apps.read_excel import ReadExcel
from apps.write_excel import WriteExcel

sample_read_excel_path = 'assets/sample.xlsx'
sample_read_excel_path = 'assets/20200807_TN_디비스키마_sample.xlsx'
sample_write_excel_path = 'assets/result.xlsx'

if __name__ == '__main__':
    reader = ReadExcel()
    read_result = reader.read(path = sample_read_excel_path)
    pprint(read_result)

    chrome = ChromeDriver()
    translate_result = chrome.run(translate_data = read_result)
    pprint(translate_result)

    writer = WriteExcel()
    writer.write(write_data = translate_result, path = sample_write_excel_path)
