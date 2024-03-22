import datetime

'''datetime.date class method'''
d = datetime.date.today()
d0 = datetime.date(1990, 9, 14)
print("Today is ", d)
print("But my Birthday is on", d0)
print()


'''datetime.datetime class method'''
d1 = datetime.datetime(1990, 9, 14, hour=16)
print("My birthday is on " + str(d1))
print("My birth date is " + str(d1.day))
print("My birth month is " + str(d1.month))
print("My birth year is " + str(d1.year))
print("My birth time is " + str(d1.time()))
print("My birth hour is " + str(d1.hour))
print("My birth day of the week is " + str(d1.weekday()))
print()


'''today function and now functions'''
d2 = datetime.date.today()
print("Today is " + str(d2))
d3 = datetime.datetime.today()
print("Today is ", d3)
t0 = datetime.datetime.now()
print("Now is ", t0)
print()


'''datetime.time class method'''
t = datetime.time()
print("Timer at 0 ", t)
t1 = datetime.time(16, 15, 00)
print("Time at birth was ", t1)
print("Hour of birth was ", t1.hour)
print("Minute of birth ", t1.minute)
print("Seconds of birth was ", t1.second)
print()


'''Practice/Trying something'''
d4 = datetime.date.today()
print(d4)
d5 = datetime.datetime.today()
print(d5)
td1 = d5-d1
print(td1)
print()


'''datetime.timedelta class method'''
d6 = datetime.date.today()
print(d6)
days = datetime.timedelta(days=1)
d6 = d6+days
print(d6)
days = datetime.timedelta(days=-1)
d6 = d6+days
print(d6)
month = datetime.timedelta(weeks=4)
d6 = d6+month
print(d6)
year = datetime.timedelta(days=365)
d6 = d6+year
print(d6)
year = datetime.timedelta(days=-365)
d6 = d6+year
print(d6)
print()


'''string formatting datetime with datetime.strftime class method'''
dt = datetime.datetime.today()
print(dt)
print(dt.strftime("%a"))  # abbr weekday
print(dt.strftime("%A"))  # full weekday
print(dt.strftime("%A %d"))  # full weekday and 2-digit month day
print(dt.strftime("%A %d %b"))  # full weekday, 2-digit month day and abbr month
print(dt.strftime("%A %d %B"))  # full weekday, 2-digit month day and full month
print(dt.strftime("%A %d %B %y"))  # full weekday, 2-digit month day, full month and abbr year
print(dt.strftime("%A %d %B %Y"))  # full weekday, 2-digit month day, full month and full 4-digit year
print(dt.strftime("%H"))
print(dt.strftime("%I"))
print(dt.strftime("%H:%M"))
print(dt.strftime("%H:%M:%S %p"))
print(dt.strftime("%j"))
print(dt.strftime("%U"))
print(dt.strftime("%c"))
print(dt.strftime("%x"))
print(dt.strftime("%X"))
