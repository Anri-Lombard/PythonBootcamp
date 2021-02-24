import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
weekday = now.weekday()
print(f"This month is {month} of year {year} on day {day} of hour {hour}\nThis is weekday number {weekday}")

date_of_birth = dt.datetime(year=2002, month=3, day=22, hour=12)
print(f"You were born {date_of_birth}")
