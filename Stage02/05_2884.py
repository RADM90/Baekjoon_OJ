"""
import datetime

hrs, mins = map(int, input().split())
dt_obj = datetime.datetime(2, 1, 1, hour=hrs, minute=mins)
result = dt_obj - datetime.timedelta(minutes=45)
print(datetime.datetime.strftime(result, "%H %M"))
"""

hrs, mins = map(int, input().split())
mins -= 45
if mins < 0:
    hrs -= 1
    if hrs < 0:
        hrs = 23
    mins = mins + 60
print(hrs, mins)