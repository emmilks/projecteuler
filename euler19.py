def is_leapyear(year):
    if year % 400 == 0 or year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False


def month_days(month, year):
    long_month = [1, 3, 5, 7, 8, 10, 12]
    short_month = [4, 6, 9, 11]

    if month in long_month:
        return 31
    elif month in short_month:
        return 30
    elif is_leapyear(year):
        return 29
    else:
        return 28


year = 1900
month = 1
day = 1
weekday = 1

count = 0

while True:
    day += 1
    if day > month_days(month, year):
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1

    weekday += 1
    if weekday > 7:
        weekday = 1

    if day == 1 and weekday == 7 and year > 1900:
        count += 1

    if year == 2000 and month == 12 and day == 31:
        break

print(count)
