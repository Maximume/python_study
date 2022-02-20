# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0
cnt = 0
for year in range(1900, 2001):

    for month in range(12):
        month_dates = dates[month]
        if year%4 == 0 and month == 1:
            month_dates += 1

        for i in range(month_dates):
            if days%7 == 6 and year > 1900 and i == 0:
                print(year, month + 1, i + 1)
                cnt += 1
            days += 1
            
print(days)
print(cnt)