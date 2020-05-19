# here we have some simple functions.
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y


""" 
go to the main module 
python43 (unit testing).py
"""