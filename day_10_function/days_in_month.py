#!/usr/bin/env python3
# Python 3.9.6

def is_leap(year):
    if (year % 4 == 0) and (year % 100) and (year % 400):
        return True
    else:
        return False


def days_in_month(month, year):
    if month > 12 or month < 1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Check leap year
    days = 0
    if is_leap(year) and month == 2:
        days = 29
    else:
        days = month_days[month-1]
    return days


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(month, year)
print(days)
