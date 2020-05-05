# python 39
# duck typing and asking forgiveness, not permission (EAFP)

# in this module, we will go over couple of aspects of being pythonic.
# basically, it means we are following conventions and coding style of python language and we need to write clean and readable code.
# here we will going to learn basically two concepts of being python.
# they are-
    # 1. Duck typing
    # 2. Easier to Ask Forgiveness than Permission (EAFP)
# they are very closely related.

# duck typing
# the reason is called duck typing is that we assume
# if a object walks and quacks like a duck then it is duck.
# it means we simply dont care what type of object we are working with,
# we only care if our object can do what we ask it to do.
# lets see a easy example.

# here we have two different class and they have two methods.
# those two methods do different thing depending on the class.
class Duck:
    def quack(self):
        print("Quack, quack")
    def fly(self):
        print("Flap, flap!")

class Person:
    def quack(self):
        print("I'm quacking like a duck")
    def fly(self):
        print("I'm flapping my Arms!")

# here we have this function because we want to execute those two methods in it.
def quack_and_fly(object_1):
    """ Not Duck-Typed (Not Pythonic)"""
    if isinstance(object_1,Duck):
        object_1.quack()
        object_1.fly()
    else:
        print("This has to be a duck!")

    print()

# here we have two instances
d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

# but we dont care if that object p is a duck or not. we only care if it behaves like a dy=uck when we asked to do so.
# our PErson class has quack and fly method. so it should work too in quack_and_fly() method.
# so we should treat it at that way.
def quack_and_fly_new(object_1):
    """Duck-Typed (Pythonic)"""
    object_1.quack()
    object_1.fly()
    print()

quack_and_fly_new(d) 
quack_and_fly_new(p)
# now it doesn't care what object we are passing in.
# thats what duck typing is.

# now we might thinking isn't this dangerous?
# can we pass in any object that will pass an error?
# thats true.
# we might think that all we care about in this example is not what type of object it is but whether it can quack and fly.
# So, how about we put some checks inplace to make sure that those methods exists.
# this is what where the second concept comes in that EAFP

# first just look at the non-pythonic way to do this.
# this is actually called "look before you leap" (LBYL).

def quack_and_fly_new2(object_1):
    """LYBL (Non-Pythonic)"""
    if hasattr(object_1, "quack"): # this line ensures that if an attribute exists within our object.
        if callable(object_1.quack): # this line ensures that if an attribute which exists within our object is callable or not.
            object_1.quack()

    if hasattr(object_1, "fly"):
        if callable(object_1.fly):
            object_1.fly()
    print()

quack_and_fly_new2(d) 
quack_and_fly_new2(1)

# here we are asking for permission in everystep.
# we are saying can we do this? can we do this?
# and then finally after all permissions we are actually doing what we want.

# but in pythonic concept we should ask forgiveness not permissions (EAFP)
# we have to to here error handling.
# we are just going to say lets try to do something and it doesn.t work then we handle it.

def quack_and_fly_new3(object_1):
    """EAFP (Pythonic)"""
    try:
        object_1.quack()
        object_1.fly()
        object_1.bark()
    except AttributeError as err:
        print(err)

    print()

quack_and_fly_new3(d) 
quack_and_fly_new3(p)



# these pythonic concepts actually extends to many real world problems.
# lets see some of them.

# Example 1

#person= {"name": "Shawki", "age": 15, "job": "Programmer"}
person = {"name": "Arko", "age": 16}

# LBYL (Non-Pythonic)
if "name" in person and "age" in person and "job" in person:
    print("I'm {name}. I'm {age} years old and I'm a {job}".format(**person))
else:
    print("Missing Some keys :(")

# EAFP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I'm a {job}".format(**person))
except KeyError as key:
    print("Missing {} key :(".format(key))


# Example 2

my_list=[1,2,3,4,5,6]

# Non-Pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print("That index does not exists :|")

# Pythonic
try:
    print(my_list[5])
except IndexError:
    print("That index does not exists :|")

# Example 3 from python docs
# there are lots of advantage of being pythonic.
# because it is faster to execute as we are acessing the object once, easier to read and we can also avoid race condition and certains situation.

import os
my_file = "/temp/test.txt"

# Race Condition
if os.access(my_file,os.R_OK):# checking if we can access the file or not
    with open(my_file,"r") as f:
        print(f.read())
else:
    print("file cannot be accessed")
# this is a race- condition because first we are checking if we can access the file or not.
# if that gives us True we go to the next line where we accessing the file.
# but within the certain time period form first line to second, the file may be become un usable.
# so, we are not likely catch that error because we thought that we can access the file.
# so we should use the No race-condition.

# No Race-Condition
try:
    f=open(my_file,"r")
except IOError as e:
    print("File cannot be accessed")

else:
    with f:
        print(f.read())
# in this eaxmple, we are actually trying to open the file.
# if we cant the we are printing the line else we are reading the file content.
# so here we are instead of asking permission we are just doing what we need.
# if we cant do that then just handle it the way that it need to be handled.


# NOTE:
# but there are some situation when becoming pythonic becomes disadvantage.
# there we have to few checks and ask for the permissions
