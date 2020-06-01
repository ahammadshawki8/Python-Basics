import logging
logging.basicConfig(filename="secret.log",level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


a=20
b=2

add_result=add(a,b)
logging.debug("add")

sub_result=sub(a,b)
logging.debug("sub")

mul_result=mul(a,b)
logging.debug("mul")

div_result=div(a,b)
logging.debug("div")