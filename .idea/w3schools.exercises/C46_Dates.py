#Import the datetime module and display the current date:

import datetime

x=datetime.datetime.now()
print(x)        #2023-09-18 23:00:45.094065

print(x.year)       #2023
print(x.month)      #9
print(x.strftime("%A"))     #Monday



#Creating Date Objects
x = datetime.datetime(2018, 6,1)

print(x)        #2018-06-01 00:00:00



# The strftime() Method :for formatting date objects into readable strings.
x = datetime.datetime(2016,6,5)
x = datetime.datetime.now()

print(x.strftime("%w"))

print(x.strftime("%a"))     # %a	Weekday, short version	Sun
print(x.strftime("%A"))     # %A	Weekday, full version	Sunday
print(x.strftime("%b"))     # %b	Month name, short version	Jun
print(x.strftime("%B"))     # %B	Month name, full version	June
print(x.strftime("%w"))     # %w	Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%d"))     # %d	Day of month 01-31, 05
print(x.strftime("%m"))     # %m	Month as a number 01-12, 12
print(x.strftime("%y"))     # %y	Year, short version, without century, 16
print(x.strftime("%Y"))     # %Y	Year, short version, without century, 2016
print(x.strftime("%H"))     # %H	Hour 00-23, 17
print(x.strftime("%I"))     # %I	Hour 00-23, 05
print(x.strftime("%p"))     # %p	AM/PM, PM
print(x.strftime("%M"))     # %M	Minute 00-59, 41
print(x.strftime("%S"))     # %S	Second 00-59, 08
print(x.strftime("%Z"))     # %Z	Timezone, CST
print(x.strftime("%j"))     # %j	Day number of year 001-366
print(x.strftime("%U"))     # %U	Week number of year, Sunday as the first day of week, 00-53
print(x.strftime("%W"))     # %W	Week number of year, Monday as the first day of week, 00-53
print(x.strftime("%x"))     # %x	Local version of date and time, 06/05/16
print(x.strftime("%x"))     # %X	Local version of time, 	17:41:00
