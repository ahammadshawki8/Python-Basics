# module 24
# importing module and exploring standerd library.

# we can find all the modules and library we can use in python in this link-
    #https://docs.python.org/3/library/index.html

# to import a module, we have to-
import helpers
courses=["math", "physics", "comsci", "ict", "english"]
index=helpers.found_index(courses,"comsci")# we need to tell python first that we are wanting the index variable to work with the found_index function which is situated in helpers module.
print(index)

# but if we work with this function several times, we have to write down the module name for several time.
# to ignore this, we can set a short name for our module.
# we can do this by-
import helpers as h
courses=["math", "physics", "comsci", "ict", "english"]
index=h.found_index(courses,"comsci")# now we are using h for helpers module.
print(index)

# we can even import the function itself-
from helpers import found_index
courses=["math", "physics", "comsci", "ict", "english"]
index=found_index(courses,"comsci")# we do not write the module name.
print(index)
# here we accessed the function but we did not access the variable in helpers.
# to access the variables from helpers, we can-
from helpers import found_index, shawki
courses=["math", "physics", "comsci", "ict", "english"]
index=found_index(courses,"comsci")
print(index)
print(shawki)

# if we want to import everything from helpers, we can-
from helpers import *
courses=["math", "physics", "comsci", "ict", "english"]
index=found_index(courses,"comsci")
print(index)
print(shawki)

# when we import a module,python checks multiple location.
# the location that it checks is within a list called sys.path.
# we can actually see this list if we import sys module.
from helpers import found_index, shawki
import sys
courses=["math", "physics", "comsci", "ict", "english"]
index=found_index(courses,"comsci")
print(index)
print(shawki)
print(sys.path)

# if sys.path doesn't find our module, we get an error.
# to avoid this error we can append our module location to sys.path as it is a list.
# we can do this-
#       import sys
#       sys.path.append(module location)

# but it is hard to write module location every time we want to use.
# we can set this path to python path environment variable. 
# we can set this in following location in windows.
#         settings/advance system settings/environment variable/new

# sys is a standard library. It means we do not have to download additional library from internet. It is a default library.

# we can import random library.
import random
courses=["math", "physics", "comsci", "ict", "english"]
# if we wnt to grab a random value from our course list.
# we can write-
random_courses=random.choice(courses)
print(random_courses)

# we can also import math library
import math
# we can convert degrees to radian using radians function in the math library.
rad=math.rad(90)
print(rad)
# we can also sin this radian by using sin function
print(math.sin(rad))

# we can also import calendar library
import calendar
year=calendar.isleap(2017)# finding if the year is leapyear or not.
print(year)
# it will give us a boolean.

# we can also import os library.
import os
# we can find which directory we are working currently by getcwd method(cwd=current working directory)
print(os.getcwd())

# all this libraries/modules are files itself.
# we can find its location by using __file__ attribute.
print(os.__file__)
