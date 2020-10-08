# Variables

# The input function allows you to specify a massage to display and returns the value typed in by user.
# We use a variable to remember the value entered by the user.
# name = is a variable.
# here's variable name is "name". But we can call it anything as long the variable's name doesn't contain any space.
# if some one give new value in the previous variable, python will remember the last value.

# rules of variables-1.don't contain spaces.2.don't start with a number,3.the variable name should me specific because we can understand that easily.

# collect from the user-
name = input("what is your name?")
# display the value-
print(name)
#update the value-
name="mraha"
print(name)

# 2 ways for making newline in the input.
a=input("enter a number\n")

print("enter another number")
b=input()

# Working with variables-
firstname=input("what is your first name?\n")
lastname=input("what is your last name?\n")
print("hello,"+ firstname+lastname)

# Way to give spaces in the variables-
print("hello, "+firstname+""+lastname)
# use blank quotes between to variables in the string.

# swapping values between two variables
first =1
second=2

temp=first
first=second
second=temp

print(first)
print(second)

#or-
# shortest method
a=1
b=2

a,b=b,a  # magic line of code.
# this is is simultaneous assignment. it happens because automatic packing and unpacking data.

print(a)
print(b)

# we can also use multiple initialization at a single line.
a=b=c=d=e=20
# here a,b,c,d,e all are alias of each other.
