from datetime import datetime,timedelta
cur_time=datetime.now() # this is equivalent to datetime.today()
cur_date=datetime.today().date() # this is equivalent to datetime.now().date()
c=datetime.now().time() # this is equivalent to datetime.today().time()
yesterday=cur_time-timedelta(days=1)
day = cur_time.day
month = cur_time.month
year = cur_time.year
print(f"Today is: {day}/{month}/{year}")  # Output: Today's date)
print(cur_time)
print(cur_date)
print(c)
print(yesterday)


