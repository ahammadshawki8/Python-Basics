# map, filter & reduce function.

# map function
# how to calculate the area of all circle in the given list?
import math
def area(r):
    return math.pi*(r**2)
radii=[2,5,7.1,0.3,10]

# method 1
areas=[]
for r in radii:
    a=area(r)
    areas.append(a)
print(areas)

# method 2
# using map fuction 
# math function takes two argument first is our function and second is your list.
print(map(area,radii))
# but it is not a list. it gives us its address not our answer.
print(list(map(area,radii)))
# so, we can make it list first.

# we can also use lambda expression in map function.
import math
print(list(map(lambda x:math.pi*(x**2),radii)))


# filter function.
# filter functions filter items out of the sequence and return the filter list.
n=[4,3,2,1]

# method 1
def over_two(n):
    filtered_n=[x for x in n if x>2]# using conditional in list comprehension
    return filtered_n 
print(over_two(n))

# method 2
# using filter method
print(list(filter(lambda x:x>2, n)))
# we must use lambda expression when we create filter function.
# here we need to make it list too. 

# reduce functions
# reduce functions applies same operations to items of a sequence.
# it uses result of operations as the first param(param is the short form of parameter) of next operation.
# it continues till we have the last item.
# it returns a item, not a list.

n=[4,3,2,1]

# method 1
def multiply(n):
    product=n[0]
    for i in range(1,len(n)):
        product *=n[i]
    return product
print(multiply(n))

# method 2
# using reduce function
print(reduce(lambda x,y:x*y ,n))
# as it doesn't return list, we don't need to convert it into list.

# I THINK PYTHON HAS CANCELED REDUCE FUNCTION.