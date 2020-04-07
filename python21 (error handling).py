# module 21
# error handling

# Things go wrong in programmes as well.
# they are called errors.

# there many types of errors .

#1.Syntax errors
# syntax errors are errors that a develop tool can detect.
# visual studio highlights syntax errors with the red squiggle.
# sometimes typing problem cant be detected until we run the program.
#exp-
#print(hello world")

#2.Logic errors
# logic errors are syntactically correct, but the program doesn't do what we want to do.
salary="5000"
bonus= "500"
payCheck=salary+bonus
print(payCheck)

#3.runtime errors
# runtime errors occur when the code basically works but sometime out of the ordinary "crashes" the code.
# we write a calculator program and user tries to divide a number by zero(0)
# our programme tries to read a file, and the file is missing.

#lets make a calculator program to divide values
first=input("enter first number: ")
second=input("enter second number: ")
result=float(first)/float(second)
print(result)
# if someone input 0 for second value the program errors runtime.
# in this case,
#       we can add a try/except around the code that generates the error to handle it gracefully.
first=float(input("enter first number: "))
second=float(input("enter second number: "))
try:
    result=first/second
    print(str(first)+" / "+str(second)+" = "+str(result))
except:
    print("I am sorry. Something went wrong")
#the code in the except only runs if there in an error generated when executing the code in try.

# we can use raise command to raise our own error.
first=input("Enter a number: ")
second=input("Enter another number: ")
try:
    division=float(first)/float(second)
    print(division)
except:
    print("I am sorry. Something went wrong.")
    raise

#if we want to know what the error was,how do we know what the errors will be raised.
#we can test it ourselves by using the function sys.exc_info()
# there is a list of standered python errors
#-http://docs.python.org/3/c-api/exceptions.html#standard-exceptions

import sys 
first=float(input("enter first number: "))
second=float(input("enter second number: "))
try:
    result=first/second
    print(str(first)+" / "+str(second)+" = "+str(result))
except:
    error = sys.exc_info()[0]
    print("I am sorry. Something went wrong")
    print(error)
finally:
    print("I will always run")
print("This massage will also run")
# the code in finally will always run whether there in an error or not.

# if we know exactly what error is occuring, we can specify how to handle that exact error.
first=float(input("enter first number: "))
second=float(input("enter second number: "))
try:
    result=first/second
    print(str(first)+" / "+str(second)+" = "+str(result))
except ZeroDivisionError:
    print("The answer is undefined")
 
# Ideally we should handle one or more specific error and then have a generic error handler as well.
import sys 
first=input("enter first number: ")
second=input("enter second number: ")
try:
    result=float(first)/float(second)
    print(str(first)+" / "+str(second)+" = "+str(result))
except ZeroDivisionError:
    print("The answer is infinity")
except:
    error = sys.exc_info()[0]
    print("I am sorry. Something went wrong")
    print(error)
finally:
    print("I will always run")
print("This massage will also run")

# how can we force our programme to exit if an error occurs and we dont want to continue?
# we can use the function sys.exit() in the sys library.
# or we can raise our own error in the except.

import sys 
first=input("enter first number: ")
second=input("enter second number: ")
try:
    result=float(first)/float(second)
    print(str(first)+" / "+str(second)+" = "+str(result))
except ZeroDivisionError:
    print("The answer is undefined")
    sys.exit()
finally:
    print("i will alwayss run")
print("This message will only execcute if there is no error.")
# in this case, the non indented code wont run if an error occur.
# on the other hand, the code in finally will always run.
# that is the differencs between finally and non-indented code.

# we can also use variables and an if statement to control what happens after an error.
import sys 
first=input("enter first number: ")
second=input("enter second number: ")
error=False
try:
    result=float(first)/float(second)
    print(str(first)+" / "+str(second)+" = "+str(result))
except ZeroDivisionError:
    print("The answer is infinity")
    error= True
if not error:
    print("This message will only execcute if there is no error.")

# there are lot of different situations that can raise errors in our code.such as-
    # Converting between datatypes.
    # opening files.
    # mathematical calculations.
    # trying to access a value in a list that does not exits.

# the most important thing to do error handling is to test.
# we need to-
#   execute our code with everything running normally.
#   execute our code with incorrect user input
#       -enter letter instead of numbers.
#       -enter 0 or spaces.
#       -enter a value in the wrong format(e.g. dates)
#   try other error senarios such as missing file.
#   try anything we can think of that mignt crash our code.
#       -entering really big nubers.
#       -negative numbers

# do we need to handle EVERY possible error?
# sometimes writing the code to handle the errors takes more time than writing the original program.
# whether it is necessary to handle EVERY error depend on how the code will be used.
# if we are writing a system for air traffic control we would want very through error handling.
# if we are writing a fun little app to remind us when our plants needs water, we wouldn't worry about it too much.

# challange 12 
import sys
name=input("enter the name of your file: ")
fileType=input("what type of file you want to open(txt/csv): ")
fileName=name+"."+fileType
try:
    fileToOpen=open(fileName,"r")
    fileContents=fileToOpen.read()
    print(fileContents)
except FileNotFoundError:
    print("Sorry, the action couldn\'t completed because the file is no longer exixts.")
except:
    error=sys.exc_info()[0]
    print(error)
    print("Sorry. Something went wrong. Couldn\'t complete the action.")