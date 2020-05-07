# Repeating events
# Using for loop

import turtle # turtle is a library that helps us to draw.
turtle.color("blue")
turtle.forward(100)
turtle.right(45)
turtle.color("green")
turtle.forward(50)
turtle.right(45)
turtle.color("grey")
turtle.forward(100)

# turtle commands

# right(x)    -     rotate right x degrees.
# left(x)     -     rotate left x degrees.
# colour("x") -     change pen color to x.
# forward(x)  -     move forward x.
# backward(x) -     move backward x.

# drawing square with turtle

import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
# this is a bad way to complete this task.
# we can use loops to make this task easiar.

# Loops allows us to repeat the same line of code as often as we want.
# exp-

import turtle
for steps in range(4): # for loop is a special kind of loop which allows us to specifice how many time we need to execute this code.
    turtle.forward(65)
    turtle.left(90)
# in this code "steps" is a variable. we can name it anything.
 
# Nested loops 
import turtle
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
    for moresteps in range(4):
        turtle.forward(50)
        turtle.right(90)

# variables inside loop
import turtle
shawki=8
for steps in range(shawki):
    turtle.forward(100)
    turtle.right(360/shawki)
    for moresteps in range(shawki):
        turtle. forward(50)
        turtle.right(360/shawki)
 # In python counting starts to 0. But we can specify numbers to count to or form.
for steps in range(1,10,2):
        print(steps)
# here counting starts to 1 from 10. but it skips 1 numbers after each step.

# we can also tell python exactly what values we want to use in the loop.
for steps in[1,2,3,4,5]:
        print(steps)

# even we dont have to use numbers.
import turtle
for steps in ["red","blue","green","black"]:
        turtle.color(steps)
        turtle.forward(100)
        turtle.right(90) 
        print(steps)


# Challange 6

import turtle
print("Today we are going to draw an object using turtle librery in python.")
print("Tell us your opinion")
user=int(input("How many sides the object will have?\n"))
for steps in range(user):
        turtle.forward(160)
        turtle.right(360/user)
        for moresteps in range(user):
            turtle.forward(50)
            turtle.right(360/user)

# extra credit1
# displaying febonacci series using for loop
first=0
second=1
n=int(input("enter how many numbers you want in this series: "))
for i in range(n):
        print(first)
        temp=first
        first=second
        second=temp+second

# extra credit 2
# display the sum of the series:1,3,5,7,9,11.......1119 using list
#first method-
first = 1
listf=[]
while first<=1119:
    listf.append(first)
    first=first+2
num=len(listf)
v1=listf[0]
v2=listf[-1]
sum=(v1+v2)*num/2
print(sum)

# second method
first = 1
total=0
listf=[]
while first<=1119:
    listf.append(first)
    first=first+2
for steps in listf:
    total=total+steps
print(total)

# third method
# list function converts to list
# range function is used to create a range of numbers.
# here range function indicates 1 to 1121, but not including 1121.
# and the third part indicates the gap between two number.
c=list(range(1,1121,2))
total=0
for steps in c:
    total=total+steps
print(total)

# fourth method
# without using list
total=0
for steps in range(1,1121,2):
    total=total+steps
    #or  total+=steps
print(total)

#fifth method
# using while loop
total=0
j=1
while j < 1121:
    total += j
    j += 2
print(total)

# sixth method 
# easiest method
# one line code
print(sum(range(1,1121,2)))

# extra credit 3
# sum of those values which are the multiple of 3 from a range.
total=0
for steps in range(1,10000):
    if steps % 3 == 0:
        total += steps
print(total)

# extra credit 4
# sum of those values which are the multiple of 3 and 5 less than 100.
total=0
for steps in range(1,100):
    if steps % 3 == 0 and steps % 5 == 0:
        total += steps
print(total)

# extra credit 5
# displaying a lists first value 1 time, second value 2 time, third value 3 time,....
a=["banana","apple","mango"]
for i in range(len(a)):
        for j in range(i+1):
                print(a[i])

# break keyword.
nums=[1,2,3,4,5]
for n in nums:
        if n == 3:
                print("found!")
                break
        print(n)   
# when the conditional is true, break keyword will breaks out the loop. It will ignore the value 3.

# continue keyword
# what if we want to ignore a value but not break out of the loop completely?
nums=[1,2,3,4,5]
for n in nums:
        if n == 3:
                print("found!")
                continue
        print(n)   
# continue will skip to next value of the loop.

turtle.done()