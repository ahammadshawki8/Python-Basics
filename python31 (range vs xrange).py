# range() vs xrange()

# in python2, there are 2 functions range and x range()
# though they both are used when we are working with a range of values.
# they have some difference.
# range() returns a list while xrange() returns a generator.
# the type of the range object is <class "list"> where the type of a xrange object is <class "xrange">
# range() take much more space in the memory compared to xrange()
# range() is little faster than xrange() but that it tottaly neglectable
# we can do slicing with range() as it is a list, but we can do it with xrange()
# we have to iterate over xrange() object to use it.

# in python3, there is no xrange() function.
# there is only range() function which works as the xrange() function 
# and all the disadvantages of xrange() function has solved.
# 1. so range() function in python3 returns a generator and the range() object is <class "range">
# 2. it takes little space in the memory and it is fast too.
# 3. we can slice the range() object and the slice will also be a range object.
# 4. we have to iterate over range() object to use it.

# 1
print(range(1,6))
print(type(range(1,6)))

# 2
import sys
print(sys.getsizeof(range(100))) 

# 3
a=range(1,6)[2:5]
print(a)

# 4
for i in range(1,6):
    print(i)
