import argparse
import datetime
import functools
import sys

import colorcalendar
from .colorcalendar import show_calendar, month_list
from colorline import cprint

__version__ = colorcalendar.__version__

eprint = functools.partial(cprint, color='r', bcolor='c', mode='highlight')

available_color = ['k', 'r', 'g', 'y', 'c', 'b', 'p', 'w']

parser = argparse.ArgumentParser(description='A colorful calendar', prefix_chars='-+')
parser.add_argument('-v', '--version', help='show version', version=__version__, action='version')
parser.add_argument('--date', help='ISO format: 2018-2-11', default=datetime.date.today().isoformat())
parser.add_argument('-y', '--year', help='specify a year to display', default=None)
parser.add_argument('-m', '--month', help='specify a month to display', default=None)
parser.add_argument('-t', '--today', help='specify date of today to display', default=1)
parser.add_argument('-f', '--foreground', help='foreground color', dest='fg', default='w', choices=available_color)
parser.add_argument('-b', '--background', help='background color', dest='bg', default='r', choices=available_color)
parser.add_argument('-c', '--color', help='disable color', action='store_false')
parser.add_argument('--frame', help='one character for frames', default='=')
parser.add_argument('--today-sign', help='character for today', dest='today_sign', default='*')

args = parser.parse_args()

colorp = functools.partial(cprint, color=args.fg, bcolor=args.bg)

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

def show(year, month, day):
    try:
        days_count = check_date(year, month, day)
    except ValueError as error:
        eprint(error)
        exit()

    first_day = zeller_formula(year, month, day)
    if args.color:
        colorp('Today: {}-{}-{}'.format(year, month, day))
    else:
        print('Today: {}-{}-{}'.format(year, month, day))
    show_calendar(month=month, start=first_day, end=days_count, today=day, fcolor=args.fg, bcolor=args.bg, frame=args.frame, today_sign=args.today_sign, color=args.color)


def main():
    if args.year:
        if args.month:
            date = [args.year, args.month, args.today]
        else:
            date = [args.year, 0, args.today]
    else:
        if args.month:
            eprint('Month cannot be assigned without year')
            exit()
        date = args.date.split('-')

    try:
        year, month, day = [int(x) for x in date]
    except ValueError:
        #Date must be integer, must be format year-mo-da
        eprint('Invalid date, please refer to the ISO format: 2018-2-11, or specify correct year or month')
        exit()

    if month == 0:
        month = range(1, 13)
    else:
        month = [month]

    for m in month:
        show(year, m, day)
