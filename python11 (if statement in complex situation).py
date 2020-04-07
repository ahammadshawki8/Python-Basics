# module 11
# using if statement in complex situation

# elif
country= input("Where are you form?\n").upper()
if country=="ENGLAND":
    print("Hello!")
elif country=="GERMANY":# elif allows us to check for different values. It means else-if.
    print("Gutan Tag!")
elif country=="FRANCE":
    print("Bonjour!")
elif country=="MEXICO":
    print("Ola Amigo!")
elif country=="INDIA":
    print("Namaste!")
else:
    print("Hey!")

# The code will run 1st condition first.If it is true, then it doesn't run the other condition.
# If it is not true then it run the 2nd conditon.
#exp-

deposit=int(input("How much you want to deposit?\n"))
if deposit> 1000:
    print("You got a new TV!")
elif deposit> 100:
    print("You got a new toaster!")
else:
    print("You got a new mug!")
print("Have a nice day!")


# and/or
# and statement will only execute if every condition is True.

wonlottery=False
bigwin=False
lottery=input("Have you won a lottery?(yes/no)\n").lower()
if lottery==("yes"):
    wonlottery=True
    amount=int(input("How much have you won?\n"))
    if amount > 1000000 :
        bigwin=True
    else:
        bigwin=False
if wonlottery and bigwin:
    print("You can retire.")
else:
    print("You can\'t retire.")

# or statement executes is either one codition is true.

saturday=False
sunday=False
day=input("What day is today?\n").lower()
if day=="saturday":
    saturday=True
else:
    saturday=False
if day=="sunday":
    sunday=True
else:
    sunday=False
if saturday or sunday:
    print("Today is holiday.")
else:
    print("Today is working day.")

#combining multiple "and"/"or" command in a single if statement.

month=input("which month is it?\n").lower()
if month=="september" or month=="november" or month=="june" or month=="april":
    print("There 30 days in this month.")
elif month=="february":
    print("There are 28 days in this month.")
else:
    print("There are 31 days in this month.")


favmovie=input("What is your favourite movie?\n").lower()
favbook=input("What is your favourite book?\n").lower()
favpast=input("What is your favourite pastime?\n").lower()
if favmovie=="avenzers" and favbook=="harry potter" and favpast=="playing football":
    print("We must hang out!")
else:
    print("I appreciate your choice.")

# Combining and/or in a single statement.
# "and" statement will run first between "and"/"or".
# we need to put () to separate conditions.

favs=input("What is your favourite sport?\n").lower()
favt=input("What is your favourite team?\n").lower()
if favs=="football"  and (favt=="brazil" or "real madrid"):
    print("Great choice. Best team of all time.")
else:
    print("Worst choice. Get out from my code.")

# we can do the same operation by using flag(boolean variables)
football=False
team=False
favs=input("What is your favourite sport?\n").lower()
if favs=="football":
    football=True
else:
    football=False
favt=input("What is your favourite team?\n").lower()
if favt=="brazil" or favt=="real madrid":
    team=True
else:
    team=False
if football and team:
     print("Great choice. Best team of all time.")
else:
    print("Worst choice. Get out from my code.")

# nesting if statement inside each other
# nested statement will only execute if the first statement is true.

monday=False
coffee=False
day=input("What day is today?\n").lower()
if day=="monday":
    monday=True
    drink=input("Do we have any fresh coffee?\n").lower()
    if drink=="yes":
        coffee=True
        print("That\'s what I needed.")
    else:
        coffee=False
    if not coffee:
        print("Go buy a coffee!")
        print("I hate mondays.")
print("Now we can start work.")

# (simmilar to elif statement)
# using nested if statement instead of elif statement.
a=9
b=5
if a < b:
    print("a is less than b")
else:
    if a == b:
        print("a is equals to b")
    else:
        print("a is greater than b")

# extra credit 1
# making bmi calculator using if statement.
name =input("enter your name: ").capitalize()
height_m =float(input("enter your height in metre: "))
weight_kg =float(input("enter your weight in kilogram: "))

bmi=weight_kg/(height_m**2)
print("bmi: ")
print(bmi)

if bmi < 25:
    print(name+" is not overweight.")
else:
    print(name+" is overweight.")