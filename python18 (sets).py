# module 18
# sets

# what is a set?
# a set is a type of data that stores a set of things.
# this is actually a set of unique things.
# this means a set doesn't contains same elements multiple time.

# how to create a set?
# using set function.
a= set()
# this is a empty set.
# example of a set with elements
s=set([1,2,3,4,5,6])
# or- s={1,2,3,4,5,6}
print(s)

# how to add element in this set.
# using add funtion.
a.add(1)
a.add(5)
a.add(3)
print(a)
# we can add multiple values in a set using update method.
a.update([2,6,7,8])

# display each element in a set.
for x in a:
    print(x)

# when should we use sets?
# one example is to remove duplicates from a list.
c=set()
d=[]
b=[1,1,1,3,4,5,7,7,5,8,90]
for x in b:
    c.add(x)
for x in c:
    d.append(x)
print(d)

# easist way to to the same operation.
b=[1,1,1,3,4,5,7,7,5,8,90]
b1=list(set(b))
print(b1)

# how to remove values from a set?
# we can either use remove or discard method.
g={2,3,4,5,6,7,8}
g.remove(5)
print(g)
# but if we want to remove a value which is not exists in the set, we will get an error.
# in order to handle this error we should use discard method.
g.discard(99)
print(g)

# intersection of sets
s1={1,2,3}
s2={2,3,4}
s3={3,4,5}

s4= s1.intersection(s2,s3)
s4_new=s1 & s2 & s3
print(s4)
print(s4_new)

# union of sets.
s5=s1.union(s2,s3)
s5_new=s1|s2|s3
print(s5)
print(s5_new)

# differences of sets
s6= s1.difference(s2,s3)
s6_new=(s1-s2)-s3
print(s6)
print(s6_new)

# symmetric differences of sets
# symmetric differences contains all the differences values in both sets.
s7=s1.symmetric_difference(s2)
s7_new=s1^s2
print(s7)
print(s7_new)

# extra credit 1
# sum of unique items
c=set()
total=0
b=[1,1,1,3,4,5,7,7,5,8,90]
for x in b:
    c.add(x)
for x in c:
    total += x
print(total)

#or(easiest method)
b=[1,1,1,3,4,5,7,7,5,8,90]
print(sum(set(b))) 
