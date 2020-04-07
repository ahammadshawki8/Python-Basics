# module 9
# working with times
import datetime
current_time=datetime.datetime.now()# the part after "=" is the code which access the current_time in our code. Now is a function which returns present time.
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print(datetime.datetime.strftime(current_time,"%H:%M"))  #or 
print(current_time.strftime("%H:%M"))
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