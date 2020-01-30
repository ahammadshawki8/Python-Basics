# module 29
# comprehensions
# comprehensions is used to simplify our large and complicated code shortly.

# list comprehensions
nums=[0,1,2,3,4,5,6,7,8,9]

#print out squares.
#general method
mylist=[]
for n in nums:
    mylist.append(n**2)
print(mylist)
#using map
print(list(map(lambda x:x**2,nums)))
# we can do this with list comprehension too.
mylist=[n**2 for n in nums]
print(mylist)

# printing out even numbers.
# general method
mylist=[]
for n in nums:
    if n%2==0:
        mylist.append(n)
print(mylist)
#using filter
print(list(filter(lambda x:x%2==0,nums)))
#using conditionals in list comprehension.
mylist=[x for x in nums if x%2==0]
print(mylist)

# I want a (letter,number) tuple pair for each letter in "abcd" and each number in "0123"
#general method
mylist=[]
for letter in "abcd":
    for number in range(4):
        mylist.append((letter,number))
print(mylist)
# nested list comprehension
mylist=[(letter,number) for letter in "abcd" for number in range(4)]
print(mylist)


# dictionary comprehension.
# but before that we need to know what zip function does?
# zip function match the items of multiple lists one to one and returns them in tuples.
# it means index 0 item in list 1, will be matched up with index 0 intem of list 2 and so on.
names=["tony","peter","wade","bruce"]
heroes=["iron man","spider man","deadpool","batman"]
print(list(zip(names,heroes)))
# we need to convert it into list.

# general method
mydict={}
for name,hero in list(zip(names,heroes)):
    mydict[name]=hero
print(mydict)
#using dictionary comprehensions
mydict={name:hero for name,hero in list(zip(names,heroes))}
print(mydict)
#if we dont want deadpool in our dictionary, we can add conditionals.
mydict={name:hero for name,hero in list(zip(names,heroes)) if hero !="deadpool"}
print(mydict)


# set comprehensions
nums=[1,1,2,1,3,4,5,4,4,6,7,7,8,9,6,8]
myset=set()
for i in nums:
    myset.add(i)
print(myset)

# set comprehensions are simmilar to dictionary comprehensions.
# but it does not contains any colon.
myset={n for n in nums}
print(myset)
#just like list comprehension, we can add conditionals and nested loops to the end of the set comprehensions as much as we want.


#Generator Expression
#generator expressions are simmilar to list comprehensions.

#general method
nums=[1,2,3,4,5,6,7,8,9]
def gen_func(nums):
    for n in nums:
        yield n**2 
my_gen=gen_func(nums)
# yeild function dont return values immidiately.
# it continues till the end of the loop and store all values in a list.
# Finally, return the list.
print(list(my_gen))
# we need to convert yeilded generator function into list.

#using generator expression.
my_gen=(n**2 for n in nums)
print(list(my_gen))