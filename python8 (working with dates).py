# module 8
# Working with dates

import datetime # the import statement gives us access to the functionality of datetime class. It is actually means to avialable any class.
                # datetime is a class. there are different types of class in python.
now = datetime.date.today() # today is a function that returns todays date.
print("todays date is "+str(now))

# we can access different parts of date
print(now.year)
print(now.month)
print(now.day)
print(now.strftime("%a %d %b, %Y"))#strftime allows you to specify date format.
#strftime means str from time.
print(datetime.date.strftime(now,"%a %d %b, %Y"))

# exp-
print(now.strftime("please attend our event at %A, %B %d in the year of %Y."))# we don't need to write str function if we are using strftime function.
# %b is the month abbreviation.
# %B is the full month name.
# %m is month in number.
# %y is two digit year.
# %Y is four digit year.
# %a is the day of the week abbreviated.
# %A is the day of the week.
# %d is the day
# %D is the full date in numbers.
# FOR MORE OPTIONS VISIT "http://strftime.org/" 

# sometimes we have to use different letters, symbles and numbers in our code which is noy belongs to English.
# The programmers speak that is named localization.
# it would take more time and code to access those letters or symbles.
# we can find more information in this site-"http://babel.pocoo.org/" 

import datetime
userinput=input("what is your birthday? (mm/dd/yyyy)\n")
birth=datetime.datetime.strptime(userinput,"%m/%d/%Y").date() # the strptime allows you to convert a string into a date format of python.
print(birth)
# strptime means str python time.
# There is two datetime in the code. One is for datetime module, another is for datetime class.

# How can we create a countdown to see how many days left untill a big event-
import datetime
nextbirthday=datetime.datetime.strptime("12/28/2019","%m/%d/%Y").date() # the date() means that we only wants to access the date.
now=datetime.date.today()
difference=nextbirthday-now
print(difference.days)# here we write down days to make the output how many "days" are left.

# how to find a date's day of the week?
import datetime
date=datetime.datetime.strptime("28/12/2004","%d/%m/%Y").date()
day_week=date.strftime("%A")
print(day_week)

# We can find more options/code/programme to find out the differences between two dates in "http://dateutil/" library.