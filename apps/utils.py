import time


class ExcelError(Exception):
    pass


class ExcelReadError(ExcelError):
    pass


class ExcelWriteError(ExcelError):
    pass


def time_sleep(sleep_time = 1):
    time.sleep(sleep_time)
