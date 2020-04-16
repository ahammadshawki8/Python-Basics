# module 2
# displaying text

#to make multiple line we can- 1.add \n in the string or, 2.use print command again and again.\n means newline.
print ("I am Shawki\n")

#we can use \t in the string for big space.\t means TAB.
print ("I am a\t student")

#we can use triple quotes outside the string for newline.For doing that,we can just press enter after ending a line into three quotes' string.
print ("""I read in class 9.
which class do you read in?""")

#we can use + between two strings under same command for displaying them jointly.
# this is called string concatenation.
print ("I am a coder."+"I am learning python.")

# we can also use comma between two string or a strind and integer/float value.
# comma give spaces automatically after each of its part.
print("I read in class",9)

#if we use single quotes in the string ,we should use double quotes outside of the string.
#if we use double quotes in the string ,we should use single quotes outside of the string.
#if we want to use extra quote in string and we want to display that quote, we need to put an \ before that quote.
print ("I love programming \" do you?")

#if we want to display \, just put it in its place.
#but some string may have words like \news, \talk,This time we have to put another \ before \.
print("I want to print\\news")

# string repetition
# we can multiply string with integer. it is called repetition.
print("Boo! "*4)

# all the work that we have done before using back-slash are called "escape sequence"
# there are lots more escape sequence.
# sequence              intro
# \\                single back-slash
# \'                single quote
# \"                double quote
# \a                ASCII Bell (BEL)
# \b	            ASCII Backspace (BS)
# \f	            ASCII Formfeed (FF)	
# \n	            ASCII Linefeed (LF)	
# \r	            ASCII Carriage Return (CR)	
# \t	            ASCII Horizontal Tab (TAB)	
# \v	            ASCII Vertical Tab (VT)	
# \ooo	            Character with octal value ooo	
# \xhh	            Character with hex value hh
# \N{name}	        Character named name in the Unicode database
# \uxxxx	        Character with 16-bit hex value xxxx. Exactly four hexadecimal digits are required.
# \Uxxxxxxxx	    Character with 32-bit hex value xxxxxxxx. Exactly eight hexadecimal digits are required.

# to learn more, we can go to
"http://python-ds.com/python-3-escape-sequences"