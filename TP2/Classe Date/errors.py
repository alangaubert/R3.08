class DateError(Exception):
    pass

class InvalidDateError(DateError):
    pass

class DateParseError(DateError):
    pass