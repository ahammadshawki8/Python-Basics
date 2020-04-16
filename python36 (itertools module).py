# module 36
# itertools

# itertools module is a standerd library of python.
# the functions of itertool module are very handy in functional programming.
# in this module, we are going to explore the itertools module.

# first lets import the module
import itertools as it

# now lets see all the methods and attributes of itertool module.
print(dir(it))

# we have here some pretty basic and handy methods here.

#['__doc__', '__loader__', '__name__', '__package__', '__spec__', '_grouper', '_tee', '_tee_dataobject', 
# 'accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle',
# 'dropwhile', 'filterfalse', 'groupby', 'islice', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 
# 'tee', 'zip_longest']

# we have already talked about combination and permutation in programming terms series.
# lets look at them one more time

# combimations()
a=[2,3,4,5,6,2,7,1,3,5]
comb=it.combinations(a,2)
# combinations() take two arguements. one is the iterable which we need to combinate.
# another one is the number of elements that we need in each combination.
# it makes the combinations in tuple and return all the combinations to us in a list.
print(list(comb))
# we have to convert it to a list to see it.

# permutations()
# it is same as combinations(), but the difference is that here all the indexing matters
perm=it.permutations(a,2)
print(list(perm))

# combinations_with_replacement()
# the difference between combinations() and combinations_with_replacement() 
# is that here we can use single value multiple times. its like the mobile number.
a=list(it.combinations_with_replacement("ABC",2))
print(a)

# count()
# count() function starts from a certain value and counts to infinity.
for i in it.count(10):
    print(i)
    if i==20:
        break
# we have to break the loop, unless it will continue to the end of the world,
# or i guess to the end of the battery life of my pc.

# cycle()
# cycle() function iterate any iterable to the infinity.

i=0
for a in it.cycle([1,2,3]):
    print(a)
    i+=1
    if i==6:
        break

# cycle() takes an iterable. and iterate over that iterable. if the iteration done, then iterate again and again
# it continues the process indifinitely.

# repeat()
# repeat() method repeat an object infinite time or a certain time.
a=it.repeat([1,2,3],3)
print(list(a))
# it takes 2 arguements, first one is the object.
# second one is how many times we want to repeat the object.
# if we ignore second arguement then it will repeat the object infinite times.

# accumulate()
# accumulate() returns a list of the running totals for each item of that list. 
a=[1,3,6,13,5]
b=it.accumulate(a)
print(list(b))

# takewhile()
# takewhile() work likes filter(), it filtered values from list under certain condition.
# but the difference between takewhile() and filter() is, takewhile() stops when it first hit a false condition.
# on the other case filter() iterate over the whole list and filter certain values out.
a=[1,2,3,4,6,7,8,1,2]
b=it.takewhile(lambda x: x<=6,a)
# it takes two arguement first one is a function and second one is that iterable.
print(list(b))

# dropwhile()
# it is like the takewhile() function.
# the difference is that it removes the values form that iterable until it hit a false condition. 
a=[1,2,3,4,6,7,8,1,2]
b=it.dropwhile(lambda x: x<=6,a)
print(list(b))

# product()
# product() gives us paired-values from two different iterable.
# its like the cartesian product in set theory.
a=[1,2,3]
b=["a","b"]
c=it.product(a,b)
print(list(c))

# chain()
# chain() takes multiple iterables and combine all the iterables in one iterable.
a=[1,2,3]
b=[4,5,6]
c=[3,2,7]
d=[1,8,9,2,3]
e=it.chain(a,b,c,d)
print(list(e))

# filterfalse()
# it is jusst the opposite of filter() function.
# it gives us the false values under conditions.
# it is just like the tilda(~) sign in numpy and pandas.
a=[1,2,3,4,6,1,2,3]
b=list(it.filterfalse(lambda x: x<4,a))
print(b)

# groupby()
# it groups the element of the iterable according to a key function
a=[("a",1),("a",2),("b",1),("b",2)]
b=it.groupby(a,lambda x: x[0])# this lambda function called key function
for key,group in b:
    print(key+" : ",list(group))

# islice()
# The islice() function works much the same way as slicing a list or tuple.
# we pass it an iterable, a starting, and stopping point,
# and, just like slicing a list, the slice returned stops at the index just before the stopping point.
# we can optionally include a step value, as well.
# The biggest difference of slicing and islice() is, of course, that islice() returns an iterator.
a=[1,2,3,4,5,6,1,3,2,4]
b=it.islice(a,3,8,2)
print(list(b))

# starmap()
# starmap() is much like map()
# but the difference is map() works in a single list.
# but starmap() works with multiple tuples under a list and run functions on them
a=[(1,2),(3,4),(5,6)]
b=list(it.starmap(lambda x,y: x*y,a))
print(b)

# tee()
# tee() function can be used to create any number of independent iterators from a single iterable.
# It takes two arguments: the first is an iterable inputs , 
# and the second is the number n of independent iterators over inputs to return (by default, n is set to 2).
# The iterators are returned in a tuple of length n .
iterator1, iterator2 = it.tee([1, 2, 3, 4, 5], 2)
print(list(iterator1))
# if we print it agin we can see that,iterator1 is now exhausted.
list(iterator1)
# but iterator2 works independently of iterator1
list(iterator2)  

# zip_longest()
# it is like the zip() function.
# This function makes an iterator that aggregates elements from each of the iterables.
# Iteration continues until the longest iterable is exhausted.

# the difference between zip() and zip_longest() is that,
# zip() only zip values from different iterables of same length.
# it will ignore the extra values if one of the iterables has more values than others. 
# but in zip_longest() method,
# If the iterables are of uneven length, we can handle missing values are filled-in with fillvalue.

colors = ['red', 'orange', 'yellow', 'green', 'blue',]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

for each in it.zip_longest(colors, data, fillvalue=None):
    print(each)


