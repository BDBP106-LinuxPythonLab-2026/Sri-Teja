# A magic date is a date where the date multiplied by the month is equal to the two-digit year
"""function that determines whether a date is magic date or not"""


def magic_date(day, month, year):
    return month * day==year % 100


for year in range(1901, 2001):
    for month in range(1, 13):
        for day in range(1, 32):
            if magic_date(day, month, year):
                print(day, month, year)