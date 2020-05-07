# Let's Start

# my first python programme -this is called comment.
# print-it is a command.
# "hello world"-it is string of text.
# print command displays a massage on the screen.
print ("hello world")
print ('I am Shawki')

""" this is a string. but we are not working with it.
    so we are using it as a comment. this string like
    comment is called documentation."""  

# how to count the number of characters in a string?
# using len function
# len is the short form of lenth 
s="hello world"
print(len(s))

# how to find a characters with index
print(s[0])

# how to print hello from this variable.
print(s[0:5])
# this means print the characters from the beginning to the index 5 but not including index no 5.

# how to display a message with a place holder.
greeting="hello"
name="Shawki"
message="{}, {}. welcome!".format(greeting, name)
print(message) 

# we can do the same thing using f strings.
greeting="hello"
name="Shawki"
message=f"{greeting}, {name}. welcome!"
print(message)

# how to display the methods that we can use in a string?
# using dir method.
print(dir(name))

# if we want to know lot more information about strings we can use help method.
print(help(str))# here str is the short form of string

# we can also search help for any function.
print(help(str.lower))