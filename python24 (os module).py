# module 25
# os module 
# os means operating system.

# first import os module
import os

# we can see all the methods and attributes of this module using dir method.
print(dir(os)) 

# we can find which directory we are working currently by getcwd method(cwd=current working directory)
print(os.getcwd())

# we can change the directory by chdir (changeDirectory) function.
# os.chdir("F:\python\.vscode\mm")

# we can see all file and folders in the directory by listdir function.
print(os.listdir())
# it is set default in which directory we are currently using.
# we can change this directory.

# we can create a new folder to the directory.
# first method-(using mkdir method)
#os.mkdir("directory1")
# second method-(using makedirs method)
#os.makedirs("directory1")

# the difference between mkdir and makedirs is we can create sub-directory with makedirs method which cant be created by mkdir method.
os.makedirs("directory1/subDir1")

# deleting directors
# first method-(using rmdir method)
#os.rmdir("directory1")
# second method-(using removedirs method)
os.removedirs("directory1/subDir1")
# the difference between rmdir and removedirs is same as mkdir and makedirs.

# deleting files
# using remove method
#os.remove(filename)

# rename folders using rename method.
#os.rename("UserGuest.txt","Ug.txt")

# print out all the information of a file.
# we can use stat function
print(os.stat("Ug.txt"))
# we can see different info in the terminal. they all are attribute. we can use them too.
print(os.stat("Ug.txt").st_size)
# this is the file size in byte.
# we can print the modification time of the folder using another attribute.
print(os.stat("Ug.txt").st_mtime)
# this will print out the time in computer readable way.
# to print it out in human readable way, we can-
from datetime import datetime# importing datetime method from datetime module
d=os.stat("Ug.txt").st_mtime
print(datetime.fromtimestamp(d))# using fromtimestamp method. 

# if we want to see the entire directory tree in files within the dextop.
# we can use walk method
# os.walk is a generator that yeilds a tuple of three values as it walking the directory tree.
# so each directory it sees, it yeilds the directory path, directories within that path and the files and folders within the path.
for dirpath, dirname, filename in os.walk("F:/MK-XL"):
    print("currentpath: ", dirpath)
    print("Directory: ", dirname)
    print("files: ", filename)
    print()
# this loop will be continued while all the files are printed in the terminal.

# printing all environment variable by using environ method
print(os.environ)
# access the HOME directory location grabbing the home environment variable by using get method.
print(os.environ.get("HOME"))

# how to create a new folder in this directory location.
# we can use os.path module.
# we can use join method of this module
file_path=os.path.join(os.environ.get("HOME"),"TEXT.txt")
print(file_path)

# grab the basename of any path using basename method.
print(os.path.basename("/user/AhammadShawki8/TEXT.txt"))
# print the directory name of anypath using dirname method.
print(os.path.dirname("/user/AhammadShawki8/TEXT.txt"))
# if we want to print both of those, we can use split method.
print(os.path.split("/user/AhammadShawki8/TEXT.txt"))
# we can also check the path's existence by exists method.
print(os.path.exists("/user/AhammadShawki8/TEXT.txt"))
# we can check if the path is a directory or not using isdir method.
print(os.path.isdir("/user/AhammadShawki8/TEXT.txt"))
# we can check if the path is a file or not using isfile method.
print(os.path.isfile("/user/AhammadShawki8/TEXT.txt"))
# if we want to split the paths root and the extension, we can use spilttext method.
print(os.path.splitext("/user/AhammadShawki8/TEXT.txt"))
# we can split the drive and the directory,filename with extension using splitdrive method.
print(os.path.splitdrive("C:/user/AhammadShawki8/TEXT.txt"))

# we can also see all the methods and attributes in os.path module by dir function.
print(dir(os.path))