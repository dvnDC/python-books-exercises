"""
"Date Detection

Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31,
the months range from 01 to 12, and the years range from 1000 to 2999.
Note that if the day or month is a single digit, it’ll have a leading zero.”

Excerpt From
Automate the Boring Stuff with Python
Al Sweigart
This material may be protected by copyright.
"""

import re


def is_valid_date(date_string):
    match = re.match(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$', date_string)
    if match:
        day, month, year = map(int, (match.group(1), match.group(2), match.group(3)))
        if month == 2:
            if day > 29 or (day == 29 and not is_leap_year(year)):
                return False
        elif month in (4, 6, 9, 11):
            if day == 31:
                return False
        return True
    return False


def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


print(is_valid_date("31/12/2022"))  # True
print(is_valid_date("29/02/2020"))  # True
print(is_valid_date("29/02/2021"))  # False
print(is_valid_date("31/04/2022"))  # False
