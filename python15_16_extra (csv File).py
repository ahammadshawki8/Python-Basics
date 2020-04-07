# what is csv?
# a common format for storing information in a file in Comma Seperated(csv)
# a csv file contains data seperated by a character, usually a comma.
# each row represents one record of data.
# it is sometimes called a Character Seperated Values file because
# the seperated character could be a different character such as a semi-colon ";" 
name="NameWithAge.csv"
mode="w"
files=open(name, mode)
files.write("shawki,14\n")
files.write("sowad,15")
files.close()

# if we are reading a csv file, there is a csv library that will help us.
# to access the features in the csv library we must import it.
import csv

# now we can use the reader function to return all the rows from the file into a list.
# the reader function will take an open csv file and return each row from the file into a list.
with open("ReadAge.csv","r") as files:
    dataFromFile=csv.reader(files)
# if we are not using a coma to separate the values, we can
# tell the reader function what character is used as delimeter.
# dataFromFile=csv.reader(files, delimiter=";")

# now we can open and read a csv file
with open("equipment.txt","w") as mycsvfile:
    mycsvfile.write("book,4\n")
    mycsvfile.write("pen,5\n")
    mycsvfile.write("pencil,8\n")
with open("equipment.txt","r") as mycsvfile:
    # read the file content
    listfromfile=csv.reader(mycsvfile)
    for row in listfromfile:
       print(row)
print()
# once we have all the rows from the csv files returned, 
# how do we access the individual rows?
#= use a for loop to loop through the values in the list
# each row will be one value. 

# what if we want to access an indiviul value from a row and not just print the whole row?
# the row returned in the loop is actually a list of the words in that row.
with open("equipment.txt","r") as mycsvfile:
    listfromfile=csv.reader(mycsvfile)
    for row in listfromfile:
        for word in row:
            print(word)
print()
#so we can just create a nested loop to loop through the words in the row.

# but if we dont like those brackets and quotes added to the rows!-
# we can use the join function to format the output.
        #-SeparatorToDisplay.join(listname)
with open("equipment.txt","r") as mycsvfile:
    listfromfile=csv.reader(mycsvfile)
    for row in listfromfile:
        print(",".join(row))
print()
# Challange 10
import csv
name="age.csv"
mode="w"
with open(name, mode) as files:
    files.write("Name,Age\n")
    files.write("Shawki,14\n")
    files.write("Sowad,15\n")
    files.write("Shahid,13\n")
    files.write("Hasnine,14\n")
    files.write("Rohan,15\n")
with open("age.csv","r") as files:
    AgeFromFile=csv.reader(files)
    for line in AgeFromFile:
        print(",".join(line))