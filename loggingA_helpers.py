import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter=logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("Employee.log")
logger.addHandler(file_handler)
file_handler.setFormatter(formatter)

class Employee: 
    def __init__(self,first,last):
        self.first=first
        self.last=last

        logger.info("Created Employee: {} - {}".format(self.fullname,self.email)) # here we are printing out that we haave crated a new employee.

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @property
    def email(self):
        return f"{self.first}{self.last}@email.com"

emp1=Employee("Ahammad","Shawki")
emp2=Employee("John","Dalton")
emp3=Employee("Carl","Goog")

