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

def build_month(month):
    month_str = [' ']*(LENGTH - 2)
    month = month_list[month - 1]
    month_len = len(month)
    start = (LENGTH - month_len) // 2 - 1
    end = start + month_len
    for ind, c in enumerate(month):
        month_str[start + ind] = c
    month_str = ''.join(month_str)
    month_str += '|'
    month_str = '|' + month_str
    return month_str

def show_calendar(month=False, frame='=', start=7, end=31, today=1, today_sign='*', fcolor='w', bcolor='b', mode='default', color=True):
    # Validation
    assert end <= 31
    assert today <= end
    if month:
        assert isinstance(month, int)
    up_frame = ''.join([frame]*(LENGTH - 2))
    up_frame = '*' + up_frame
    up_frame += '*'
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
    if month:
        out_str = '\n'.join([out_str, build_month(month), up_frame])
    if color:
        cprint(out_str, color=fcolor, bcolor=bcolor, mode=mode)
    else:
        print(out_str)

if __name__ == '__main__':
    show_calendar(frame='&', start=1, end=31)

