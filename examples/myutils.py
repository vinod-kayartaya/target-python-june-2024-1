"""
Here is an example of a Java function to determine if the input is a leap year or not
boolean isLeap(int year){
    return year % 400 == 0 || year % 4 == 0 && year % 100 != 0;
}
"""


def is_leap(year: int) -> bool:
    """
    Checks if the year is leap
    """
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def max_days(month:int, year: int) -> int:
    """
    Returns the maximum number of days in the given month/year combination
    """
    if month < 1 or month > 12:
        raise ValueError('Month should be between 1 and 12')
    if year < 1:
        raise ValueError('Year should be >= 1')
    if month == 2:
        return 29 if is_leap(year) else 28  # return is_leap(year) ? 29 : 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


def dir2(obj: any) -> list:
    attrs = []
    for each_attr in dir(obj):
        if not each_attr.startswith('_'):
            attrs.append(each_attr)
    return attrs

# print(f'inside myutils.py, value of __name__ is {__name__}')


# the value of builtin variable __name__ is '__main__' only when you execiute the module
# and not when you import
if __name__ == '__main__':  
    m = int(input('Enter month: (1-12) '))
    y = int(input('Enter year: (>=1) '))

    days = max_days(m, y)
    print(f'Maximum days in month {m} of year {y} is {days}.')

