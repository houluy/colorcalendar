import argparse
import datetime
import functools
import sys

from .colorcalendar import show_calendar, month_list
from colorline import cprint

eprint = functools.partial(cprint, color='r', bcolor='g', mode='highlight')

parser = argparse.ArgumentParser(description='A colorful calendar')
parser.add_argument('--date', help='ISO format: 2018-2-11', default=datetime.date.today().isoformat(), dest='date')
parser.add_argument('-b', '--background', help='background color', dest='bg')
parser.add_argument('-f', '--foreground', help='foreground color', dest='fg')

args = parser.parse_args()

start_year = 0
end_year = 2100

thirty_list = [4, 6, 9, 11]

def check_date(year, month, day):
    if year <= start_year or year >= end_year:
        raise ValueError('Year must be in [1900, 2100]')
    elif month < 1 or month > 12:
        raise ValueError('Month must be in [1, 12]')
    elif day < 1 or day > 31:
        raise ValueError('Day must be in [1, 31]')

    days_count = 31
    leap_year = True if year % 4 == 0 else False
    if month == 2:
        days_count = 29
        if day > 29:
            raise ValueError("There's only 28 days in {}".format(month_list[month - 1]))
        elif not leap_year:
            if day == 29:
                raise ValueError('Year {} is not a leap year'.format(year))
            else:
                days_count = 28
    elif month in thirty_list:
        if day > 30:
            raise ValueError("There's only 30 days in {}".format(month_list[month - 1]))
        else:
            days_count = 30
    return days_count

def exit():
    parser.print_help()
    sys.exit(-1)

def zeller_formula(year, month, day):
    if month == 1 or month == 2:
        zeller_month = month + 12
        zeller_year = year - 1
    else:
        zeller_month, zeller_year = month, year

    zeller_century = zeller_year // 100
    year_suf = zeller_year - zeller_year // 100 * 100
    first_day = (year_suf + year_suf // 4 + zeller_century // 4 - 2 * zeller_century + (26 * (zeller_month + 1)) // 10) % 7

    if zeller_year > 1582:
        return first_day
    else:
        return first_day + 4

def main():
    try:
        year, month, day = [int(x) for x in args.date.split('-')]
    except ValueError:
        #Date must be integer, must be format year-mo-da
        eprint('Invalid date, please refer to the ISO format: 2018-2-11')
        exit()

    try:
        days_count = check_date(year, month, day)
    except ValueError as error:
        eprint(error)
        exit()

    first_day = zeller_formula(year, month, day)
    show_calendar(start=first_day, end=days_count, today=day)

