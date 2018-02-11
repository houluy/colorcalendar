from colorline import cprint

LENGTH = 35
WEEK = 7

month_list = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

def show_calendar(frame='=', start=7, end=31, today=1, today_sign='*', color='w', bcolor='b', mode='default'):
    # Validation
    assert end <= 31
    assert today <= end
    up_frame = ''.join([frame]*LENGTH)
    title = '|SUN  MON  TUE  WEN  THU  FRI  SAT|'
    start = start % WEEK #Sunday is zero
    out_str = '\n'.join([up_frame, title, up_frame])
    line = 0
    date = 1
    sun = 2
    step = 5
    while True:
        temp = [' ' for x in range(LENGTH)]
        temp[0] = '|'
        anchor = sun
        above_ten = 0
        for day in range(WEEK):
            if line == 0 and day < start:
                anchor += step
                continue
            if date >= 9:
                sun = 1
                step = 4
                if date > 9:
                    above_ten += 1
            if date == today:
                temp[anchor] = str(date) + today_sign
                anchor -= 1
                above_ten += 1
            else:
                temp[anchor] = str(date)
            date += 1
            if date == end + 1:
                break
            anchor += step
        else:
            anchor -= step
        last_pos = LENGTH - 1 - above_ten
        temp[last_pos] = '|'
        del temp[last_pos + 1:]
        out_str = '\n'.join([out_str, ''.join(temp)])
        if date == end + 1:
            break
        line += 1
    out_str = '\n'.join([out_str, up_frame])
    cprint(out_str, color=color, bcolor=bcolor, mode=mode)

if __name__ == '__main__':
    show_calendar(frame='&', start=1, end=31)

