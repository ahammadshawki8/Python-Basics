# module 13
# repeating events until they have done.
# using while loop
answer="0"
while answer != "4":  # while loop allows us to execute our code until a perticular condition is true.
    answer=input("what is 2 + 2 ?")
print("yes. 2+2=4")

# drawing square with while loop
import turtle
counter=0
while counter < 4 :
    turtle.forward(100)
    turtle.right(90)
    counter= counter+1

# challange 7
import turtle
color=input("what colour of pen you want to use?\n")
lenth=int(input("what will the lenth of your line?\n"))
angle=int(input("what will your shapes angle?\n"))
while lenth != 0:
    turtle.forward(lenth)
    turtle.right(angle)
    lenth=int(input("what will the lenth of your line?\n"))
    angle=int(input("what will your shapes angle?\n"))

# we can also use else command in for or while loop like if statement.

# extra credit1
# displaying fibonacci series using while loop
first=0
second=1
while first<10000:
    print(first)
    temp=first
    first=second
    second=temp+second

# extra credit 2 
# displaying sum of positive numbers from a list
given_list=[9,7,7,5,4,4,3,1,0,-1,-2,-3,-5,-6,-6]
total=0
i = 0
while given_list[i] > 0:
    total += given_list[i]
    i += 1
print(total)

# what if the list have only positive numbers.
given_list=[9,7,7,5,4,4,3,1]
total=0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total += given_list[i]
    i += 1
print(total)

# break command in for loop.
# displaying sum of positive numbers from a list using break command.
# break command means to break out of the loop.
given_list=[9,7,7,5,4,4,3,1,0,-1,-2,-3,-5,-6,-6]
total=0
for element in given_list:
    if element <= 0:
        break
    total += element
print(total)

# break command in while loop.
given_list=[9,7,7,5,4,4,3,1,0,-1,-2,-3,-5,-6,-6]
total=0
i=0
while True:# true means the while loop will always run because the statement ins true.
    total += given_list[i]
    i += 1
    if given_list[i] <=0:
        break
print(total)

# extra credit 3
# displaying sum of negative numbers from a list
given_list=[9,7,7,5,4,4,3,1,0,-1,-2,-3,-5,-6,-6]
total=0
i=-1
while True:
    total += given_list[i]
    i -= 1
    if given_list[i] >=0:
        break
print(total)