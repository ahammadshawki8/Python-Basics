# walrus operator :=

# there is a new syntax := that assigns values to variables as part of a larger expression.
# It is known as the walrus operator.
# This is the most controvercial feature of python3.8

# this is desisgned to use inside expressions.
# it actually assigns a variable to some part of the expression.

# Example 1
a = [0,1,2,3,4,5,6]

if (n := len(a)) > 5:
    print(f"List is too long ({n} elements, expected <= 5)")

# what it does is that, it sets a variable n as the len(a) so that we can use it later on.
# it helps avoid calling len() function twice.
# But it doesn't effects the expression.
# we must use brakets to distinguish the part of expression that we want to set as a var with walrus.


# Example 2
while (ans := input("Enter a number: ")) != "":
    print(ans)

# this operator is also helpful with while-loops that compute a value to test loop termination 
# and then that same value again in the body of the loop.


# Example 3
names = ["1. ahammad", "2. cristiano", "3. ramos", "4. zidan"]
allowed_names = ["ahammad", "cristiano", "marcelo"]

walrus_list = [clean_name.title() for name in names if (clean_name := name[3:]) in allowed_names]
print(walrus_list)

# Another motivated use case of walrus operator in list comprehensions
# where a value computed in a filtering condition isalso needed in the expression body.


# Example 4
# we can do all the stuffs without walrus which we can do with walrus.
# the only advantage walrus gives us is to remove some extra line of codes.

# Without Walrus
x = 5
without_walrus = x < 7
print(without_walrus)

# With Walrus
x = 5
print(walrus := x < 7) 
# we can use the var later on
print(not walrus)

# Example 5
# this is the best advantage of walrus operators. 
# It is simmilar to example 2.

# Without Walrus
nums = []
num = input("Type a number: ")
while num.isdigit():
    nums.append(int(num))
    num = input("Type a number: ")
print(nums)

# With Walrus
nums = []
while (num := input("Type a number: ")).isdigit():
    nums.append(num)
print(nums)



# Example 6
# if helps us avoiding levels of indentation.

# Without Walrus
var = 5
if var == 5:
    ans = input("Enter your name: ")
    if ans != "":
        print("Nice name!")


# With walrus
var = 5
if var == 5 and (ans := input("Enter your name: ")) != "":
    print("Nice name") 


# Now we know what is walrus and where should we use it.
# It makes the code kind of hard to understand.
# so, if we really want to implement it within our code and make our code DRY, then we can do thaat.
# Otherwise, we can do the exact same things without the walrus operator :=