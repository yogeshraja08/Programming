# date and time in python
import datetime as dt   #  as dt --> dt can be used instead of datetime
current_date=dt.date.today()
print(current_date)

new_date=dt.date(2023, 1, 4)
print(new_date)
print("year : ",new_date.year)
print("month : ",new_date.month)
print("day : ",new_date.day)

print("----------------------------")

current_time=dt.datetime.now()
print(current_time)

new_time=dt.time(2, 12, 20, 88)
print(new_time)
print("hour : ",new_time.hour)
print("minute : ",new_time.minute)
print("second : ",new_time.second)
print("milli second : ",new_time.microsecond)

new_datetime=dt.datetime(2023,4,1,3,43,40)
print(new_datetime.year)
print(new_datetime.day)
print(new_datetime.hour)

print("========================================")

current=dt.datetime.now()
new_year=dt.datetime(2024,1,1)
diff=new_year-current
print(diff)

print("+++++++++++++++++++++++++++++++++++++++")

# to change the format of date and time
current=dt.datetime.now()
print(current)
s=current.strftime("%a %B %z")  # for values refer : https://w3schools.com/python/python_datetime.asp
print(s)

print("//////////////////////////////////////")

# to add days to current date use 'timedelta'
date=dt.date.today() + dt.timedelta(days=5)
print(date)