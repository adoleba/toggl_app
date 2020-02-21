from datetime import date


def start_day():
    return date(year=date.today().year, month=date.today().month, day=1)


def end_day():
    if date.today().month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif date.today().month in [4, 6, 9, 11]:
        days = 30
    elif date.today().year in [2020, 2024, 2028, 2032]:
        days = 29
    else:
        days = 28
    return date(year=date.today().year, month=date.today().month, day=days)
