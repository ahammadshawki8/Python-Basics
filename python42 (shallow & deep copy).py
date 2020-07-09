# copying in python

# first lets create a list
list1=[[1,2,3],[4,5,6],[7,8,9]]

# when we want to copy a list in python, we generally use the equal sign.
list2=list1
print(list2)
# but this doesn't create a copy of the previous list.
# instead of that, it creates an alias of that previous list.
# they are basically same object having the same id in the memory but with different name.
print("ID of list1 :",id(list1))
print("ID of list2 :",id(list2))

# if we change one list it will impact one both of the list.
list2.append([10,11,12])
print(list1)
print(list2) 


# pythons copy module is a great module which gives us some useful functions.
# those functions can help us to copy any object.

# first we have to import the module
import copy

# shallow copy is a special kind of copy which doesn't copy the object rather than copy the reference of that object.
# we can do a shallow copy using copy() method. we can also use the built-in copy() method here.
list3=[[1,2,3],[4,5,6],[7,8,9]]

list4=copy.copy(list3)
#list4=list3.copy()

# here list4 is a shallow copy of list3
# they have different id in the memory but still they are connected.
print("ID of list3 :",id(list3))
print("ID of list4 :",id(list4))

# if we change an element of list4, the same change will be applied in list 3.
list4[1][0]="CHANGED"
print(list3)
print(list4)

# but we have one issue with the shallow copy.
# they are connected but they are not completely connected.
# it means if we append or remove elements in one list, it wont be carried over to its shallow copy.

list4.append([10,11,12])
print(list3)
print(list4)

list3.remove([1,2,3])
print(list3)
print(list4)

# so changing or updating one value in an object will have impact to its shallow copy.
# but adding or deleting wont have that impact.


# but our goal is still not achieved.
# we want to create a copy that is properly separated from the object.
# there where deep copy comes to play.
# basically, deep copy creates a new object which doesn't have connection to the initial object.

# we can create deep copy be deepcopy() method. 
# we can also use loops or comprehension to copy the object element by element. it will also create a deep copy.
list5=[[1,2,3],[4,5,6],[7,8,9]]
list6=copy.deepcopy(list5)

# so obiously, they have different id in the memory.
print("ID of list5 :",id(list5))
print("ID of list6 :",id(list6))

# we can update, append or remove in the object and it wont impact its deep copy
print(list5)
print(list6)

list6[0][2]="CHANGED"
print(list5)
print(list6)

list6.append([10,11,12])
print(list5)
print(list6)

list6.remove([4,5,6])
print(list5)
print(list6)
