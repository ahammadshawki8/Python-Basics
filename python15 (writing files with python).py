# module 15
# working with files

# how do we write a file with code?
#1.use the open function to create and open a file.
#    myFile= open(fileName,accessMode)
#2.we must specify
#-file name
#-access mode

# what is the file name?
#= the file name is the name of our file including the extension
#-data.txt, mytimes.csv
# the file will be created in the same folder as your program.

# if we aren't sure what directory our project is using, we can right click
# on the tab for our code window and select poen containing folder to see the folder in file explorer.

# what is the access mode?
#= the access mode specifies what we will do with the file after we open it.

# we can specify any of them following:

# Access Mode   -   Actions
#     r         -   Read a file
#     w         -   Write to the file. It will overwrite the file.
#     a         -   Append to the exixting file content.
#     b         -   Open a binary file  
#     r+/w+     -   Read and write.
#     x	        -   Creates a new file. If file already exists, the operation fails.
#     t	        -   This is the default mode. It opens in text mode.

filename="Guestlist.txt"
accessmode="w"
myfile=open(filename, accessmode)
#or  myfile=open(filename, mode=accessmode)
#or  myfile=open(filename, mode="w")
#or  myfile=open("Guestlist.txt", "w")

# Writing to files
 
# how do we write to a function?
# we can use write function.
filename="Guestlist.txt"
accessmode="w"
myfile=open(filename, accessmode)
myfile.write("I am a coder!\n")
myfile.write("I read in class 9.")
# when we are finished we should always close the file.
# we can use close method.
filename="Guestlist.txt"
accessmode="w"
myfile=open(filename, accessmode)
myfile.write("I am a coder!\n")
myfile.write("I read in class 9.")
myfile.close()

#  we can print the name of the file.
print(myfile.name)
# we can also print the mode of the file.
print(myfile.mode)

# we can see if the file is closed or not by using closed method.
print(myfile.closed)

# but everytime opening a file and closing it is a difficult task.
# so we are going to use context manager.
# programmes should always open a file, and close it when they are done.
# context manager automically open and close the file for us.
with open(filename, accessmode) as myfile:
    pass
# here we dont working with this file so we are passing it by pass keyword.
# while using context manager, we need to indent working lines of our code.
# unless the code wont work.

# using seek method in writing files.
with open("overwrite.txt","w") as d:
    d.write("test")
    d.seek(0)
    d.write("test")
# it will overwrite test over test.
# seeking is a little confusing for file write.
# because it dont overwrite everything, it overwrites only what it needs to overwrite.
with open("overwrite.txt","w") as d:
    d.write("test")
    d.seek(0)
    d.write("r")

# user input
filename="UserGuest.txt"
accessmode="w"
data= input("Please enter file info: ")
with open(filename, accessmode) as myfile:
    myfile.write(data)
print("File written successfully.")