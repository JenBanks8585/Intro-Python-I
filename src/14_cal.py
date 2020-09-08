"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime, date


'''
year= (input('Please enter the year: \n'))
month= (input('Please enter the month: \n'))

y = int(year)
m = int(month)

def cal(*args):
  return calendar.month(*args)

print(cal(y,m))

'''

m= datetime.today().month
y= datetime.today().year

input_len = len(sys.argv)

if input_len == 1:
  print(calendar.month(y,m))

if input_len == 2:
  month = int(sys.argv[1])
  if month > 12 or month < 1:
    print('This month does not exist')
  else:
    print(calendar.month(y,month))

if input_len == 3:
  month = int(sys.argv[1])
  year = int(sys.argv[2])
  if month > 12 or month < 1 or year > y:
    print('This time does not exist')
  else:
    print(calendar.month(year,month))