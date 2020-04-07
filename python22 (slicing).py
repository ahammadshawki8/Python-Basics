  # module 23
# slicing

# slicing list 

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9 -positive index
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 -negative index
# we can use both positive and negative index to diplay a value from a list or a string.

# how can we access certain range from a list?
# we can use this equation-
#            list[start:end:step]

# how can we print 0 to 5 from this list?
print(my_list[0:6])
# this means print the values of the list which includes index 0 to 6 but not including 6.

# we can also do that by negative index.
print(my_list[-10:-4])

# we can also combine positive and negative number.
print(my_list[0:-4])
print(my_list[-10:6])

# what if we want to print the values of indexes 1 to 9?
# if we want to print something till the end of the list, we can just leave the end index blank.
print(my_list[1:])

# we can also do the same thing for start.
# if we leave the start index blank, then it will print from the start of the list to the given end.
# printing the values from start to 7
print(my_list[:8])

# what happens if we leave both start and end blank?
print(my_list[:])
# we print a copy of our entire list!!

# what does step index do?
# step allows us to skip a number of values.
# what if we want to print every second value from our list?
print(my_list[0:9:2])

# we can also access a negative step also.
# it will run our list reversely.
print(my_list[-2:1:-1])

# if we want our entire list reversly, we can leave start and end index blank and set step index -1.
print(my_list[::-1])


# slicing string

url = "http://codingbat.com"
print(url)

# reverse the url
print(url[::-1])

# get the top level domain.(.com)
print(url[-4:])

# print the url without beginning with http://
print(url[7:])

# print the url without http:// and top level domain.
print(url[7:-4])