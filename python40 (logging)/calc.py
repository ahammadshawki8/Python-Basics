# initial code

        # import employee

        # import logging
        # logging.basicConfig(level=logging.DEBUG,filename="Calc_Log.log",format="%(asctime)s: %(name)s: %(message)s")

        # def add(a,b):
        #     return a+b
            
        # def sub(a,b):
        #     return a-b
            
        # def mul(a,b):
        #     return a*b
            
        # def div(a,b):
        #     return a/b

        # n1=20
        # n2=5

        # add_res=add(n1,n2)
        # logging.debug(f"add: {n1} + {n2} = {add_res}")

        # sub_res=sub(n1,n2)
        # logging.debug(f"sub: {n1} - {n2} = {sub_res}")

        # mul_res=mul(n1,n2)
        # logging.debug(f"mul: {n1} * {n2} = {mul_res}")

        # div_res=div(n1,n2)
        # logging.debug(f"div: {n1} / {n2} = {div_res}")



# initial code 2 (without error)

        # import employee
        # import logging

        # logger=logging.getLogger(__name__)
        # logger.setLevel(logging.DEBUG)

        # file_handler=logging.FileHandler("Calc_Log.log")
        # logger.addHandler(file_handler)
        # file_handler.setLevel(logging.ERROR)

        # formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
        # file_handler.setFormatter(formatter)


        # def add(a,b):
        #     return a+b
            
        # def sub(a,b):
        #     return a-b
            
        # def mul(a,b):
        #     return a*b
            
        # def div(a,b):
        #     return a/b

        # n1=20
        # n2=5

        # add_res=add(n1,n2)
        # logger.debug(f"add: {n1} + {n2} = {add_res}")

        # sub_res=sub(n1,n2)
        # logger.debug(f"sub: {n1} - {n2} = {sub_res}")

        # mul_res=mul(n1,n2)
        # logger.debug(f"mul: {n1} * {n2} = {mul_res}")

        # div_res=div(n1,n2)
        # logger.debug(f"div: {n1} / {n2} = {div_res}")



# initial code 3 (with error)

        # import employee
        # import logging

        # logger=logging.getLogger(__name__)
        # logger.setLevel(logging.DEBUG)

        # file_handler=logging.FileHandler("Calc_Log.log")
        # logger.addHandler(file_handler)
        # file_handler.setLevel(logging.ERROR)

        # formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
        # file_handler.setFormatter(formatter)


        # def add(a,b):
        #     return a+b
            
        # def sub(a,b):
        #     return a-b
            
        # def mul(a,b):
        #     return a*b
            
        # # lets add here try except handler. 
        # def div(a,b):
        #     try:
        #         result=a/b
        #     except ZeroDivisionError:
        #         logger.error("Try to devide by zero")
        #     else:
        #         return result


        # n1=20
        # n2=0 # change it to 0

        # add_res=add(n1,n2)
        # logger.debug(f"add: {n1} + {n2} = {add_res}")

        # sub_res=sub(n1,n2)
        # logger.debug(f"sub: {n1} - {n2} = {sub_res}")

        # mul_res=mul(n1,n2)
        # logger.debug(f"mul: {n1} * {n2} = {mul_res}")

        # div_res=div(n1,n2)
        # logger.debug(f"div: {n1} / {n2} = {div_res}")



# initial code 4 (with traceback)

        # import employee
        # import logging

        # logger=logging.getLogger(__name__)
        # logger.setLevel(logging.DEBUG)

        # file_handler=logging.FileHandler("Calc_Log.log")
        # logger.addHandler(file_handler)
        # file_handler.setLevel(logging.ERROR)

        # formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
        # file_handler.setFormatter(formatter)


        # def add(a,b):
        #     return a+b
            
        # def sub(a,b):
        #     return a-b
            
        # def mul(a,b):
        #     return a*b
             
        # def div(a,b):
        #     try:
        #         result=a/b
        #     except ZeroDivisionError:
        #         logger.exception("Try to devide by zero") # adding traceback
        #     else:
        #         return result


        # n1=20
        # n2=0 

        # add_res=add(n1,n2)
        # logger.debug(f"add: {n1} + {n2} = {add_res}")

        # sub_res=sub(n1,n2)
        # logger.debug(f"sub: {n1} - {n2} = {sub_res}")

        # mul_res=mul(n1,n2)
        # logger.debug(f"mul: {n1} * {n2} = {mul_res}")

        # div_res=div(n1,n2)
        # logger.debug(f"div: {n1} / {n2} = {div_res}")



# initial code 5 (multiple handlers)

        # import employee
        # import logging

        # logger=logging.getLogger(__name__)
        # logger.setLevel(logging.DEBUG)

        # file_handler=logging.FileHandler("Calc_Log.log")
        # logger.addHandler(file_handler)
        # file_handler.setLevel(logging.ERROR)

        # formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
        # file_handler.setFormatter(formatter)

        # stream_handler=logging.StreamHandler()
        # # we dont need to set the log level here because our logger already logging level of debug.
        # # now lets add this new stream_handler to logger.
        # logger.addHandler(stream_handler)



        # def add(a,b):
        #     return a+b
            
        # def sub(a,b):
        #     return a-b
            
        # def mul(a,b):
        #     return a*b

        # def div(a,b):
        #     try:
        #         result=a/b
        #     except ZeroDivisionError:
        #         logger.exception("Try to devide by zero") 
        #     else:
        #         return result


        # n1=20
        # n2=0 

        # add_res=add(n1,n2)
        # logger.debug(f"add: {n1} + {n2} = {add_res}")

        # sub_res=sub(n1,n2)
        # logger.debug(f"sub: {n1} - {n2} = {sub_res}")

        # mul_res=mul(n1,n2)
        # logger.debug(f"mul: {n1} * {n2} = {mul_res}")

        # div_res=div(n1,n2)
        # logger.debug(f"div: {n1} / {n2} = {div_res}")



# current code (multiple handlers with formatter)

import employee
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler=logging.FileHandler("Calc_Log.log")
logger.addHandler(file_handler)
file_handler.setLevel(logging.ERROR)

formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
file_handler.setFormatter(formatter)

stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter) # changed the format.


def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
 
def div(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        logger.exception("Try to devide by zero")
    else:
        return result


n1=20
n2=0 

add_res=add(n1,n2)
logger.debug(f"add: {n1} + {n2} = {add_res}")

sub_res=sub(n1,n2)
logger.debug(f"sub: {n1} - {n2} = {sub_res}")

mul_res=mul(n1,n2)
logger.debug(f"mul: {n1} * {n2} = {mul_res}")

div_res=div(n1,n2)
logger.debug(f"div: {n1} / {n2} = {div_res}")