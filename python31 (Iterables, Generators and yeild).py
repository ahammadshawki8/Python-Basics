# Module 31
# Iterables, Generators and yeild function

# QUESTION: 
# What is the use of the yield keyword in Python? What does it do?

# ANSWER:
# To understand what yield does, we must understand what generators are. 
# And before we can understand generators, we must understand iterables.

# ITERABLES:
# When we create a list, we can read its items one by one. Reading its items one by one is called "Iteration":
mylist = [1, 2, 3]
for i in mylist:
    print(i)
# here mylist is an iterable. When we use a list comprehension, we create a list, and so it is another iterable:
mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)

# Everything where we can use "for... in..." on is an iterable; lists, strings, files...
# These iterables are handy because we can read them as much as we wish,
# but we store all the values in memory and this is not always what we want when we have a lot of values.

# GENERATORS:
# Generators are iterators, a kind of iterable we can only iterate over once.
# Generators do not store all the values in memory, they generate the values on the fly:
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)
# It is just the same except we used () instead of [].
# BUT, we cannot perform for i in mygenerator a second time since generators can only be used once:
# they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

# YIELD:
# yield is a keyword that is used like return, except the function will return a generator.
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # we can see that mygenerator is an object!
for i in mygenerator:
    print(i)
# Here it's a useless example,
# but it's handy when we know our function will return a huge set of values that we will only need to read once.

# To master yield, we must understand that
# when we call the function, the code we have written in the function body does not run. 
# The function only returns the generator object.
# so we have to iterate over the generator.

# Now the hard part:
# The first time the for calls the generator object created from our function,
# it will run the code in our function from the beginning until it hits yield,
# then it'll return the first value of the loop.
# Then, each other call will run the loop we have written in the function one more time,
# and return the next value until there is no value to return.
# The generator is considered empty once the function runs, but does not hit yield anymore.
# It can be because the loop had come to an end, or because we do not satisfy an "if/else" anymore.