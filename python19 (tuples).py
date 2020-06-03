# tuples

# tuples are pretty much simmilar to list.
# the main differences between tuples and list is-
# tuples are immutable, lists are mutable.
# it means if they are written once, they will be same until the end of the world.
# we cant append, cant remove a value or change a value in tuple.

# how to make a tuple.
tuple_1=("history","math",'physics',"comsci")
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)
# we can convert a list or a set into tuple by using tuple method.
list_1=["apple","banana","mango"]
tuple_3=tuple(list_1)
print(tuple_3)
# we can do the same operations in tuple that we have done in list.
# we can loop through, we can access values etc.etc.
# but we couldn't apply any method in tuple that will mute it.

# create an empty tuple.
tuple_w=()
tuple_x=tuple()

# sort tuple 
# we can not sort a tuple with sort method as it makes a tuple mutable
# so we can rather use sorted function.
tup =(1,9,4,7,5,3,8,6,2)
tup1=sorted(tup)
print(tup1)
# sorted method gives us a list.
# so we can just-
tup2=tuple(tup1)
print(tup2)

# if we want to instantiate a tuple with single value we need to use comma after that.
# because if we dont use comma, then python will thought that it is a single value.
my_tup=(1,)
print(type(my_tup))
# we can see that it prints <class 'tuple'>
not_tup=(1)
print(type(not_tup))
# we can see that it prints <class 'int'>