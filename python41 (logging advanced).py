# module 41
# advanced logging

# in this module, we will learn about loggers, different handlers and some other things.

# first part
import logging
logging.basicConfig(level=logging.DEBUG,filename="loggingA.log",
                    format="%(asctime)s: %(name)s: %(message)s")

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b

n1=20
n2=5

add_res=add(n1,n2)
logging.debug(f"add: {n1} + {n2} = {add_res}")

sub_res=sub(n1,n2)
logging.debug(f"sub: {n1} - {n2} = {sub_res}")

mul_res=mul(n1,n2)
logging.debug(f"mul: {n1} * {n2} = {mul_res}")

div_res=div(n1,n2)
logging.debug(f"div: {n1} / {n2} = {div_res}")

# second part
import logging
logging.basicConfig(filename="Employee.log",level= logging.INFO, format="%(levelname)s:%(message)s")

class Employee: 
    def __init__(self,first,last):
        self.first=first
        self.last=last

        logging.info("Created Employee: {} - {}".format(self.fullname,self.email)) # here we are printing out that we haave crated a new employee.

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @property
    def email(self):
        return f"{self.first}{self.last}@email.com"

emp1=Employee("Ahammad","Shawki")
emp2=Employee("John","Dalton")
emp3=Employee("Carl","Goog")

# first lets comment put first part and run second part.
# we can see it creates a Employee.log file with our format.

# now lets comment out second part and rerun this module again after uncomment out the first part.
# we can see that it creates a loggingA.log file and we can see our formatting there.

# we haven't deiscusseed what this root message mean yet?
# it specifies that we are working with the root logger.
# this isnt a bad thing when we are working with smaller applications and specific files.
# but it is best to build the habit of logging with specific loggers that can all be configured separately.

# but working with this root logger isn't the best idea.why?
# let us first delete this employee and loggingb log files.

# now if we are working with 2 modules then we can import one to another.
# for our case we can uncommon out our both 2 parts.
# lets just rewrite the first part below and import the second part as another module.
# so we have to create a module first.  

import logging
import loggingA_helpers

logging.basicConfig(level=logging.DEBUG,filename="loggingA.log",
                    format="%(asctime)s: %(name)s: %(message)s")

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b

n1=20
n2=5

add_res=add(n1,n2)
logging.info(f"add: {n1} + {n2} = {add_res}")

sub_res=sub(n1,n2)
logging.info(f"sub: {n1} - {n2} = {sub_res}")

mul_res=mul(n1,n2)
logging.info(f"mul: {n1} * {n2} = {mul_res}")

div_res=div(n1,n2)
logging.info(f"div: {n1} / {n2} = {div_res}")

# when we import a module it runs all the code from that module when it was imported.
# so if we run this code it will log our all employees

# we can see that we have Employee.log file here.
# but our loggingA.log file that we specify in this module isn't created.

# so what happened here?
# the reason it do something like that it is because when we set up this logger here whitin this employee class,
# it configures the root logger there with that Employee.log file name, log level and format.
# and that happen first because we have imported loggingA.helpers file.
# and this module is sharing that logger.
# so by the time we get to configuring within this module, the logger already figured with those other values.
# so this doesn't actually do anything, it doesn't overwrite the previous initial configuration.
# the reason is that our log statements are logging down at the bottom is that the root logger is set to the info level in loggingA_helpers module.
# so the debug doesn't hit that level.

# if we chnage the debug to info and rerun this.
# we can see in employee.log file it did log the information from this module.
# but this is still kind of mess asa we are sharing this root logger.
# we arae not getting the file or the format or the level that we want.

# so lets get a logger for each of our modules so that we can configure them separately.
# in the loggingA.helpers module,
    # we will create a variable loggers = logging.getLogger()
    # now we need to specify any naming in the getLogger() function.
    # but the convention is __name__ variable.
    # so if we run this file derectly, this __name__ will be equal to "__main__"
    # if we import that in another module then it will be its own module name.
    # now we are getting a new logger here if it doesn't exits it will be created.
    # now we should use the logger variable to run the log method.
    # when we are writing logging.info, instead of that we will write logger.info
    # one nice thing about this loggers, is that they are within the hierarchy.
    # it means if this employee logger doesn't have something set, then it will fall back to the root logger.
    # for example, this logging.basicConfig() i still configuring the root logger.
    # if we run this module, we can see that it doesn't print anything in the console, it print the message in the employee.log file.
    # here we can see the logger is now set to __main__
    # now lets configure the logging with the our logger, not the root logger.
    # first to specify the employee.log file that we want to log to we have to add a file handler.
    # so we will create a new variable file_handler = logging.FileHandler("Employee.log") # we need to pass the name of our log file here.
    # now we havae this file_handler but it need to be added to our logger.
    # to do that we can say, logger.addHandler(file_handler)
    # now we need the formatting to be same that we specify in our basicConfig()
    # NOTE: we need to add this formatting to the file_handler not to the logger.
    # first lets create a formatter variable, formatter=logging.Formatter("%(levelname)s:%(name)s:%(message)s")
    # now we need to add this to our file handler.
    # we can do this by, file_handler.setFormatter(formatter)
    # and lastly lets set the log_level in this employee logger.
    # to do this we can say, logger.setLevel(logging.INFO)
    # now lets delete our basicConfig() and Employee.log file.
    # now rerun out loggingA.helpers module.
    # now we can see that it logs all the messages with correct format.
    # now lets back to our current script.

# before that it was giving us problem because we are sharing the root logger.
# but we rerun this now, we can see this time it created a new loggingA.log file with our specific format.
# in this case it stills the root logger.
# in employee.log file, we can see this prints the message correctly and it gave the name loggingA_helpers to the logger this time because we imported it.

# now quickly set up a logger for our this current module.
# first lets comment out the previous code and write them again in below.

import logging
import loggingA_helpers

logger=logging.getLogger(__name__)
file_handler=logging.FileHandler("loggingA.log")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
file_handler.setFormatter(formatter)


def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b

n1=20
n2=5

add_res=add(n1,n2)
logger.debug(f"add: {n1} + {n2} = {add_res}")

sub_res=sub(n1,n2)
logger.debug(f"sub: {n1} - {n2} = {sub_res}")

mul_res=mul(n1,n2)
logger.debug(f"mul: {n1} * {n2} = {mul_res}")

div_res=div(n1,n2)
logger.debug(f"div: {n1} / {n2} = {div_res}")

# now if we rerun this and see to our log files.
# we can see that everything is working as we thought.
# now, lets delete this files.

# one good thing for logging like this is that now we got a lot more flexibility, its nice how this hierarchy works.
# for example, we wanted our logger level debug but we only wanted our errors or worst to get logged to loggingA.log file.
# to do this, we can set level to the file_handler as well.

# so if we want tp keep our logger level to debug but only capture the errors or above, in this specific file handler
# then we can, file_handler.setLevel(logging.ERROR)

import logging
import loggingA_helpers

logger=logging.getLogger(__name__)
file_handler=logging.FileHandler("loggingA.log")
file_handler.setLevel(logging.ERROR)

logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
file_handler.setFormatter(formatter)


def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b

n1=20
n2=5

add_res=add(n1,n2)
logger.debug(f"add: {n1} + {n2} = {add_res}")

sub_res=sub(n1,n2)
logger.debug(f"sub: {n1} - {n2} = {sub_res}")

mul_res=mul(n1,n2)
logger.debug(f"mul: {n1} * {n2} = {mul_res}")

div_res=div(n1,n2)
logger.debug(f"div: {n1} / {n2} = {div_res}")

# now if we run this we can see it created our log file.
# but there is nothing in our loggingA.log
# it didnt log those debug statements because the logging statements doesn't match.
# lets put some error in our code.
import logging
import loggingA_helpers

logger=logging.getLogger(__name__)
file_handler=logging.FileHandler("loggingA.log")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
file_handler.setFormatter(formatter)


def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b

# lets add here try except handler. 
def div(a,b):
    try:
        res=a/b
    except ZeroDivisionError:
        logger.error("Try to devide by zero")
    else:
        return res

n1=20
n2=0 # change it to 0

add_res=add(n1,n2)
logger.debug(f"add: {n1} + {n2} = {add_res}")

sub_res=sub(n1,n2)
logger.debug(f"sub: {n1} - {n2} = {sub_res}")

mul_res=mul(n1,n2)
logger.debug(f"mul: {n1} * {n2} = {mul_res}")

div_res=div(n1,n2)
logger.debug(f"div: {n1} / {n2} = {div_res}")

# now if we run that and go to loggingA.log file we can see it logged our error.
# anytime we will logging an error, we should include traceback so that we caan get multiple information about what exactly happen.
# and the logging module allows us to do this very easily.
# we can do this by changing the logging.error() to logging.exception().
import logging
import loggingA_helpers

logger=logging.getLogger(__name__)
file_handler=logging.FileHandler("loggingA.log")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
file_handler.setFormatter(formatter)


def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b

# lets add here try except handler. 
def div(a,b):
    try:
        res=a/b
    except ZeroDivisionError:
        logger.exception("Try to devide by zero")
    else:
        return res

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

# now if we run this again, we can see that we get the traceback in our log file.

# another good thing is that it is easy to add multiple handlers to loggers.
# for example, lets say we want to see this debug statements that we are executing in the bottom.
# but we only want to display those to the console.
# what we can do here is that we can create another handler but instead of a fileHandler(), we will create a StreamHandler().
import logging
import loggingA_helpers

logger=logging.getLogger(__name__)
file_handler=logging.FileHandler("loggingA.log")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
file_handler.setFormatter(formatter)

stream_handler=logging.StreamHandler()
# we dont need to set the log level here because our logger already logging level of debug.
# now lets add this new stream_handler to logger.
logger.addHandler(stream_handler)



def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b

# lets add here try except handler. 
def div(a,b):
    try:
        res=a/b
    except ZeroDivisionError:
        logger.exception("Try to devide by zero")
    else:
        return res

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

# now if we run this, we can see it log our debug and error in the console, and the error is only printed to the log file.
# one thing to notice here is that, the formatting to the console insn't same that we have here in the log file.
# but we can set the formatter for stream_handler like the file_handler.
import logging
import loggingA_helpers

logger=logging.getLogger(__name__)
file_handler=logging.FileHandler("loggingA.log")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
formatter=logging.Formatter("%(asctime)s: %(name)s: %(message)s")
file_handler.setFormatter(formatter)

stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)


def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b

def div(a,b):
    try:
        res=a/b
    except ZeroDivisionError:
        logger.exception("Try to devide by zero")
    else:
        return res

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

# now we can run that and see that the format is changed.
# we can also create a new formatter and change the format as well.

# every projects need logging to their production point.
# good logs can save us from headache of lots of debug problems.
# we can do lot more advanced and complex thing in logging.
# we can learn them in python documentation and we can look at other handlers that python have.
# there are some handlers that send us email when some error occurs or something like that.
# they also have rotating logs so that one log file doesn't build up too much.
