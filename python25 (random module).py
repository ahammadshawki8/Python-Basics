# module 25
# Random module

# random values is useful to grab numbers and values randomly from a list or range or something like that.
# It should not be used for security purposes or cryptography and python mentions this in the documentation.
# python suggests us to use secret module instead of random modules for that kind of work.

# first in order to using random library, we need to import it.
import random

# we can use the random method to get a random value between 0 and 1.
# the 0 is going to be inclusive.
# the 1 is going to be none-inclusive.
# it means we can get a exact value of 0, but we can not get a exact value of 1, we can probably get 0.999 or something like that.
value_1=random.random()
print(value_1)

# if we wanted a random floating point value between 1 and 10 , then we can use the uniform method.
value_2=random.uniform(1,10)# this method takes a range as a arguement
print(value_2)

# to get random integers we can use randint(random integer) method.
value_3=random.randint(1,6)
print(value_3)
# we can also use-
print(random.randrange(1,7))
# the difference between randint and randrange is if we put(1,6) as a arguement of randint we can get 6.
# but if we put(1,6) as a arguement of randrange we can't get any 6 
# because it is a range and it means from 1 to 6 but not including 6.

# choice methods picks a random value from a list of values.
greetings=["hello","hi","hey","howdy","hola"]
value_4=random.choice(greetings)
print(value_4,"Shawki!")

# if we want to print multiple random values from our list we can use choices method.
colors=["red","black","green"]
value_5=random.choices(colors,k=10)
print(value_5)
# here we need to add an additional arguement which is K value.
# k value is just how many times we want to pick random values.
# by default the k value is 1.
# here the probability of printing red , green and black are equa-probable.
# but sometimes that wont happen.
# in that case we can weight this so that our random choices take this odds into consideration.
# and we can set these weights of our choices by passing an extra arguement which is weights.
colors=["red","black","green"]
value_6=random.choices(colors,weights=[18,10,2],k=10)# here weights is an list of what we want to weight this.
print(value_6)
# here red has 18 0f 30% chances to print.
# here black has 10 0f 30% chances to print.
# here green has 12 0f 30% chances to print.

# how we can randomly shuffle a list of values?
# lets say we have a list of values from 1 to 52. now we can think this as a deck of cards.
deck=list(range(1,53))
print(deck)
# now we are going to use the random module to shuffle this deck.
random.shuffle(deck)
print(deck)

# now if we want to get 5 random cards from the deck.
# here we could think to use choices method.
# but is should not be useful, because by choices method it can get a random card multiple time.
# but we only want unique cards.
# so to do this we can use sample method.
# it will ensure us of grabbing unique cards of the sequence.
deck_2=list(range(1,53))
hand=random.sample(deck_2,k=5)
print(hand)

# we can find more practical code of random library inthe following link-
#https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Random


# extra credit 1
# making head_tail_baksho
import random
def head_tail_baksho(mot_toss_koibar):
    head=0
    tail=0
    for i in range(mot_toss_koibar):
        value_7 = random.randint(0,1)
        if value_7 ==1:
           head +=1
        else:
            tail +=1
    print("head -->",head) 
    print("tail -->",tail) 
head_tail_baksho(10000)
print("hello!")

# extra credit 2
# making a guessing game
import random
user=int(input("Guess a number between 1 to 10\n-->"))
i=random.choice(range(1,11))
step=1
if i == user:
    print("correct!you won.")
else:
    while i != user:
        i=random.choice(range(1,11))
        if i == user:
            print("correct!you won.")
        elif i > user:
            i=input("guess higher!")
        else:
            i=input("guess lower!")
        step+=1
print("it takes only",step,"times to guess correctly")