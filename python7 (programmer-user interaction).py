# module 7
# asking user to input number 

# there are functions to convert from one datatype to another-
# int(value)       converts to an integreter.
# long(value)      converts to a long integreter.
# float(value)     converts to a floating number.  (i.e.  a number that can hold decimal places)
# str(value)       converts to a string. 
# bool(value)      converts to boolean.

a=input("enter a number")
b=input("enter another number")
answer=int(a)+int(b)
print(answer)

# how to find the type of a variable?
# we can use type function
c="Shawki"
print(type(c))

# challange-
# making a loan calculator-
l=input("Please enter your cost of loan.\n")
i=input("Please enter the interest rate of your loan.\n")
n=input("Please enter the number of years for the loan.\n")
monthlypayment=int(l)*((float(i)*(1+float(i))*12)/(((1+float(i))*12)-1))
print("Your monthly loan is %.2f." % monthlypayment)