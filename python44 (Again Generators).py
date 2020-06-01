# Generators in python

# in this module we will learn about generators 
# and why we should use them and some of their advantages over list.

# here we have a simple function here.
def square_number(nums):
    result = []
    for n in nums:
        result.append(n**2)
    return result

my_nums=square_number([1,2,3,4,5])
print(my_nums)

# currrently our function returning a list. how could we convert it to a generator?
# to do this we can,
def gen_square_number(nums):
    for n in nums:
        yield n**2
        # here we have used yeild keyword instead of return and yeild the square numbers.

# this yeild keyword is what makes a generator.
# now if we run the previous code again,
my_nums=gen_square_number([1,2,3,4,5])
print(my_nums)
# we can see that we are getting <generator object gen_square_number at 0x000001F8BC38E270>
# we are no longer getting the list.

# the reason for this is because generator dont hold the entire result in memory.
# it yields one result at a time.
# so really it is waiting for us to ask for the next result.
# so it has not computed anything yet.

# so we need to ask the generator to print the next result.
# we can do that by using next() method.
print(next(my_nums))
# we can see the first value which is 1.
# if we print out this line few times.
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# we can see that we are getting 4,9,16,25 accordingly.

# now 25 is the last value of our result. if we run this line again we are getting an StopIteration error.
#print(next(my_nums))
# it means the entire generator has been exhausted and stop generating the next values.

# now instead of getting each of the values one at a time we can use for loop in generator.
for n in my_nums:
    print(n)
    # inside this loop we can use several operations with each of the values. we dont have to wait for the entire list.

# one immidiate advantage of generator over list is that it is much readable than the list.
# we can also write the same code in a easy way using list comprehension.
my_nums=[x**2 for x in [1,2,3,4,5]]
print(my_nums)
# we can create a generator in the same way by using first () instead of third []
# this is called generator comprehension.
my_nums=(x**2 for x in [1,2,3,4,5])
print(my_nums)
# we can see that we are getting <generator object gen_square_number at 0x000001F8BC38E270>
# we can also loop through generator comprehension.
for n in my_nums:
    print(n)

# what if we want to print out all of the values at onece form the generator?
# we can convert it to a list and then print it.
print(list(my_nums))
# if we convert the generator into a list,
# then we do loss the advanteage of generators over a list in terms of performance.

# generators are better than list in terms of performance because it isn't holding all values in the memory.
# it isn't a big deal if we are working with small data.
# but if we have a big data, then having many items in the memory will decrease the efficiency of our code.


# let us see a better example here about this performance difference.
import random
import time
import psutil
import os

name = ["Shawki","Arko","Hasnine","Mahidul","Tausif"]
major= ["ComSci","Math","Chemistry","Physics","FineArts"]

# make list
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            "id" : i,
            "name" : random.choice(name),
            "major": random.choice(major)
        }
        result.append(person)
    return result

# make generator
def people_generator(num_people):
    for i in range(num_people):
        person = {
            "id" : i,
            "name" : random.choice(name),
            "major": random.choice(major)
        }
        yield person

# printing out the memory with list
process = psutil.Process(os.getpid())
print(f"Memory (Before) : {(process.memory_info().rss)/1000} MB")

t1 = time.time()
people = people_list(10000)
t2 = time.time()

print(f"Memory (After) : {(process.memory_info().rss)/1000} MB")
print(f"Took microseconds : {(t2-t1)*1000}")

# printing out the memory with generator
process = psutil.Process(os.getpid())
print(f"Memory (Before) : {(process.memory_info().rss)/1000} MB")

t1 = time.time()
people = people_generator(10000)
t2 = time.time()

print(f"Memory (After) : {(process.memory_info().rss)/1000} MB")
print(f"Took microseconds : {(t2-t1)*1000}")



# lets look at the example first with the list then with the generator (comment one and run another).
# we can see that after running with the list, the memory raised a large amount and the operaton took more time.
# and when we used generator for the same operation we can see that,
# the memory is about same and the esplased time is close to 0.
# because it hasn't done anything yet. it is waiting for us to do some operation.
# basically when it entered the loop and see the first yeild it stopped functioning.

# we have said earliar that if we convert it to a list then we loose the performance.
process = psutil.Process(os.getpid())
print(f"Memory (Before) : {(process.memory_info().rss)/1000} MB")

t1 = time.time()
people = list(people_generator(10000))
t2 = time.time()

print(f"Memory (After) : {(process.memory_info().rss)/1000} MB")
print(f"Took microseconds : {(t2-t1)*1000}")

# we can see that the performance same as the list

# so generator is bit readable and it gives us performance boost.
# it efficient the execution time and memory as well.
# not only that we can do almost every operation with generator that we do with list.
# thats why we should use generator.

# NOTE: actually generators use lazy evolution where list use eager evolution.
# eager evotution means that list are eager to return us all the values at once even we need only the first few values.
# we have to wait for the eager evoution.
# lazy evotution means generators are lazy. they dont give us result until we ask them to do it.
# we can only grab few values if we want.
# so with generator, we can instead of eagarly producing values, provide the certain values to the user as hey asked for.


# lets see another use case of generator in the real world example.
# we have all seen that api looks like that.
class Api():
    def run_this_first(self):
        pass
    def run_this_second(self):
        pass
    def run_this_last(self):
        pass
# if we dont run the methods accordingly they everything in api blow up.
# in api's documentation, they say again and again please run this first, then that blah blah..
# cause if we do it in any other order all the system crash.

# but nothing physically stops us to break the order. we can,
Api().run_this_last()
Api().run_this_second()
Api().run_this_first()

# onething we have noticed with the generator, that it computes a result.
# then it not only yeild the result back nut also the control back to the user.

# in the eagar evolution, the library code do the full computation, then gave the result back to user.
# and the  user do waht he want.
# in the generator formulation, we have little bit library code run, then lillte bit user code run, then little bit library ....
# and we interlive them.
# this is the actual core concept for why generators are made. the ide of "co-routines"

# "sub-routines" we can think of as any piece of executable code from some starting point to some ending point to complish a task.
# they have one single entry point and one single exit point and thats it. they run, then they are done.
# the library code has a sub routine and the user has to pick up.

# for the generators (co-routine), we enter the generator.
# we ask for values and the generator run but we have a nice interliving.
# here we have interliving of both library code and user code.

# when we use this Api we want to have some interliving.
# if we dont want that then we can just make it this way,
def run_Api():
    Api().run_this_first()
    Api().run_this_second()
    Api().run_this_last()
# then we can force the user run this method in correct order.
# if we could do this Api wouldnt provide us three methods.

# the reason Api give us this different functions because it specifically intend us to interlive codes.
# they just want to make sure that we interlive code in a fixed order.'
# we can easily do this with generator.
def gen_Api():
    Api.()run_this_first()
    yield()
    Api().run_this_second()
    yield()
    Api().run_this_last()
    yield()
# here we could do the interliving while easily maintaining sequence.
# we can gerantee here that the last method will never call before the first and second method.
# so genrator forces the sequencing for the users.

# NOTE: so generator is a mechanism with which we can interlive with library and user code and it can also ensure sequencing.

    
    

