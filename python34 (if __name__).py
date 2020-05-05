# module 34
# if __name__=="__main__"

# this is something that we probably going to see a lot in python.

# def main():
#     pass

# if __name__=="__main__":
#     main()

# so is this doing? and why do people use it?
# lets print out __name__ varriable.
print(__name__)
# we can see that it is giving us "__main__"
# what exactly going on here?
# when python runs a file, before going through any code, it  sets a few special variables.
# __name__ is one of the special variables.
# and when we run any code python set __name__ equal to "__main__"

# we can also import module.
# if we import a new module python sets the __name__equal to our imported module name in this case helpers.
# first we need to print(__name__) in the helpers. and then we need to import helpers.
import helpers
# we can see that the value of __name__ is now helpers.
# the reason it is doing that, is that this file is no longer running by python, it is being imported.

# now we are going to our first code.
def main():
    print("Current Module Name:",__name__)

if __name__=="__main__":
    main()

# now we can know why this code useful?
# we can see if __name__=="__main__"
# which pretty much saying, if this file ran directly by python, or it is imported in anyother file. 
# now lets add something in our main() function.
import helpers
# now if we do the same thing in the helpers and run that,
# we can see it didn't execute the main() function of helpers in our current module
# the reason it didnt print that line of main() function is because now we have this (if __name__) check inplace.

# just to illustrate it further, we can go to helpers module and type in an else condition.
import helpers
# we can see that it is saying run from import as our else statement.

# the reason we need to use this because sometimes ther might be code that we want to run that as main file.
# sometimes there code that we will only run by impoting them.

# another thing is why we are using the main() method, we can directly put the code in the if conditional to separate those.
# we are creating a main method because we can also use that method by importing that module, 
# which we cant do with the conditional.
helpers.main()