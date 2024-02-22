"""
- datetime.date
"""

import datetime
import time

day1 = datetime.date(2021,12,14)
day2 = datetime.date(2023,4,5)
diff = day2 - day1

print(day1,day1.isoweekday())

day3 = datetime.date(2024,2,16)

weekday_str = ['월', '화', '수', '목', '금', '토', '일'][day3.weekday()]
print(diff)
print(diff.days)
print(weekday_str)

import itertools

import functools
import glob # 