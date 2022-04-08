"""
1 Jan 1900 was a monday.
7 Jan 1990 was a sunday.
September, April, June and November have 30 days.
January, March, May, July, August, October, December have 31 days.
february is 28 if year % 4 != 0 or (year % 100 == 0 and not year % 400 == 0)
February has 29 if year % 4 == 0 and year % 400 == 0 else 28

How many sundays fell on the first of the month during the twentieth century?
(1 Jan 1901 to 31 Dec 2000)
"""
days = {'sep': 30, 'apr': 30, 'jun': 30, 'nov': 30, 'jan': 31, 'mar': 31,
        'may': 31, 'jul': 31, 'aug': 31, 'oct': 31, 'dec': 31, 'feb': (28, 29)}

weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

