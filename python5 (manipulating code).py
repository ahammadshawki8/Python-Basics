# manipulate the contents of variables.

# lower, upper, swapcase are different string functions.

message="Hello world"
print(message.swapcase())#change cases.
print(message.lower())#all letter is in lower case.
print(message.upper())#all letter is in upper case.
print(message.capitalize())#capitalize the first letter of the sentence.
print(message.title())#capitalize the first letter of every word in the string.
print(message.replace("Hello","hi"))#replace the word after comma to the place of the word before comma.
print(message.find("world"))#tells us the position of the word. the number which comes to the output means the characters before the word is that number.
print(message.count("o"))#count the number of the letter.
print("       dhaka        ".strip())#ignore the blank space.
print(message.startswith("H"))# gives a boolean. if a string starts with the character or not.
print(message.endswith("d"))# gives a boolean. if a string ends with the character or not.

# Example-
name=input("what is your name?")
country=input("which country do you live in?")
country=country.upper()
print(name+" lives in "+country+".")

# when we write down a function we can watch a pop up list. that's called intelliSense.
# Visual Studio will suggest possible functions we can call automically after we type any word.
# we can also press ctrl+space to launch intelliSense.

# programmers do not memorize all functions.
# so how do programmers find them when they need them?-
# 1.intellisense, 2.documentation, 3.internet searches.

# Challange 2
# solution-
name=input("what is your name?\n")
age=input("how old are you?\n")
place=input("where do you live in?\n")
yourclass=input("which class do you read in?\n")
pastime1=input("what is your favourite pastime?\n")
pastime2=input("write down your another favourite pastime.\n") 

print("I am "+name.capitalize()+"."+" I am "+age+" years old."+" My present address is "+place.capitalize()+"."+" I am a student of class "+yourclass+"."+" I like "+pastime1+" and "+pastime2+" during my leisure time.")
