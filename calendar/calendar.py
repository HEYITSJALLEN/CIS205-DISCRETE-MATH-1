# Import the calendar schedule
import calendar
import datetime

#User input for month and year
cur_datetime= datetime.datetime.now()
year = cur_datetime.year
month = cur_datetime.month

#Display the calendar
print(calendar.month(year,month))

#print(calendar.calendar(year))