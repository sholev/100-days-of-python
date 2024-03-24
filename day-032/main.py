import datetime as dt

now = dt.datetime.now()
print(now.year)
print(now.month)
print(now.weekday() + 1)
print(dt.datetime.now().strftime('%A'))
stored_date = dt.datetime(year=2020, month=2, day=20)
print(stored_date)


