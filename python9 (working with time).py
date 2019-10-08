# module 9
# working with times
import datetime
currenttime=datetime.datetime.now()# the part after "=" is the code which aaccess the currenttime in our code. Now is a function which returns present time.
print(currenttime)
print(currenttime.hour)
print(currenttime.minute)
print(currenttime.second)

print(datetime.datetime.strftime(currenttime,"%H:%M"))  #or 
print(currenttime.strftime("%H:%M"))
# In first line we have to write two arguments, because here we did not mention our variable name earliar.
# In second line we have to write only one argument as we have mention our variable name earliar.

# %H means hours(24 o'clock)
# %I means hours(12 o'clock)
# %p means AM or PM
# %M means minutes
# %S means seconds

# Challange 4
import datetime
last=input("what is yours projects last submission date? mm/dd/yyyy\n")
lastdate=datetime.datetime.strptime(last,"%m/%d/%Y").date()
currentdate=datetime.date.today()
difference=lastdate-currentdate
print("You have "+str(difference.days)+" days in your hand to submit your project.")