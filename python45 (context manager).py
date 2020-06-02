# context manager

# context manager allows us to properly manage resources 
# so that we can specify exactly what we want to set up and tear down
# when working with certain object.

# there are two different ways we can work with files.
# way 1
f=open("con_man.txt","w")
f.write("general way of writing file\n")
f.close()
# here we have to close the file after we working with it.

# way 2 (using context manager)
with open("con_man.txt","a") as f:
    f.write("writing file with context manager\n")
    # here we no longer need to remember to close the file after we are done working with it.
    # this approach is also recomamaded because if we through an error while working with this file,
    # then will still going to close the file properly.

# that is why context manager is so useful.
# it tear down the resources for us.
# and the more operations are handled automatically, the better it is. 

# we could use context managers for so many differnt resources.
# for example, we can use this to conect and close databases automatically.
# we can aquire and release locks. so there are plenty of usecase.

# so in this module we will learn how to write our own coustom context managers to  manage resources. 
# couple of different ways that we can write our own context manager.
# we can either do this with class, or with a function with a decorator.

# first lets create a context manager which opens the file for us and then automatically closes the file.
# first we will use class becase it shows clearly whats going on.

class OpenFile():
    # here we have 3 special methods.
    def __init__(self,filename,mode):
        # here we will set up couple of things.
        self.filename=filename
        self.mode=mode
    
    # __enter__ and __exit__ method are going to be the set_up and tear_down of our class.
    def __enter__(self):
        self.file = open(self.filename,self.mode) # opening the file
        return self.file # returning the created file.

    def __exit__(self,exc_type,exc_value,traceback):
        self.file.close() # closing the file
        # here teh extra parameters are for if we through an exception.
        # then we could use them to access those information.

# now lets use this context manager.
# we can use it just like before.

with OpenFile("con_man.txt","a") as f:
    f.write("writing to file using custom class context manager\n")

# to make sure that our file is closed lets use the closed attribute.
print(f.closed)
# we see that it prints True.

# now lets walk through the context manager and see what is going on,

# first of all when we use the cotext manager with OpenFile class, 
# it goes inside of the class and comes to the __init__ method and sets those attributes.

# and then since we are using with statement here what it does,
# is that it runs our statement with the __enter__ method.
# so, that open the file and that file is returned.-- method.
# that is why f is a file object inide of our context manager because that is what was returned form the __enter__ method.

# now within the context manger we could work with this anyway we like to.
# then when it finish its operation and get back to the unindent part,
# then it hits the __exit__ method and runs it.
# and then the file was closed.
# that is why (f.closed) return true after we exited the context manager.


# now lets see how to create context manager that with function.

# here we are going to use the contextlib module and from that module we will import contextmanager decorator.
from contextlib import contextmanager
# we can use this decorator to decorate a generator function

@contextmanager
def open_file(filename,mode):
    my_file = open(filename,mode)
    yield my_file # here we have one yeild statement.
    f.close()
# this is a little less code then our class was.

# everything before the yeild statement will going to eqivalent with the __enter__ method of our class.
# so this is going to be the set up of our context manager.

# everything after the yeild statement will going to eqivalent with the __exit__ method of our class.
# this is going to be the tear down of our context manager.

# technically, we should be using some try and finally statementes here we handle errors.
# but we will look at them later.


with open_file("con_man.txt","a") as f: # at this point it will run everything up until our yield statement.
    # here f will be equal to my_file as it was yield in the function.
    # now we can work with this f inside the context manager.
    f.write("writing to file using custom function context manager --> using the contextmanager decorator with a generator class\n")
# after we exit the with statement block, the all of the code after the yield statement will be run

print(f.closed) # checking if the file is closed or not.


# now lets use the try and finally statements.
@contextmanager
def open_file_try(filename,mode):
    try: # set up cpde will be in the try block.
        my_file = open(filename,mode)
        yield my_file 
    finally:
        f.close() # tear down code will be in the finally block since we always want to run it after the operation
        # it will ensure us even though we fall into any error, our tear down code will always run.

with open_file_try("con_man.txt","a") as f:
    f.write("writing to file using custom function context manager \
--> using the contextmanager decorator with a generator class which have try and finally block\n")

# but this is not much practical as the open() function inpython is already a context manager. 
# now we jave seen how to replicate the built_in functionality of context manager using both class and generator. 
# now lets look at a practical example that we will build from scratch.

# lets say we are using python to do some work in lots of different directories.
# and we are constantly entering those directories, do some work and then seed back to where we started.
# so first lets look how the code will like without a context manager.

import os

cwd = os.getcwd() # setting cwd variable to current working directory
os.chdir("6. Numpy") # changing the directory
print(os.listdir()) # doing some operation (listing the sub directories and files)
os.chdir(cwd) # seeding back to the previous directory.

# doing the same operaion multiple times.
cwd = os.getcwd()
os.chdir("7. Matplotlib")
print(os.listdir())
os.chdir(cwd)

# if we run this code now, we can see that this works.
# but this is pretty unconvenient.
# if we look at that, we can see that saving the current directory and changing the directory is setup code.
# and switching back to our original directory is the tear down code.

# these are things that we dont want to remember to do each time,
# so this is a good usecase of context manager.
# so lets crete one which does this. we will create this with generator function.

@contextmanager
def change_dir(dir_name): # taking dir_name as a parameters
    try:
        cwd = os.getcwd()
        os.chdir(dir_name)
        yield
        # here we are not working with any variable inside of the context manager.
        # so we dont have to yeild anything.
    finally:
        os.chdir(cwd)

# now lets do the same operation using context manager.
with change_dir("6. Numpy"): # here we are bot working with any variable, so we dont need to use "as" keyword. 
    # we can do whatever operation we wanted there.
    print(os.listdir())

with change_dir("7. Matplotlib"):
    print(os.listdir())

with change_dir("8. Pandas"):
    print(os.listdir())
# we can see that it works just like before.
# but now we dont need to worry about set up and tear down each time we are doing our operations.
# now we can reuse the context manager over and over and we know that those resources will be managed by context manager.