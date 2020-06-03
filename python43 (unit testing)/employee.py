# here we have a simple employee class.
# this is from oop series.

# it is for mocking
import requests


class Employee:
    raise_amt=1.05

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    @property
    def email(self):
        return f"{self.first}{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first.title()} {self.last.title()}" 

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    
    ## Mocking ##
    # it is going to be a method in our class
    def monthly_scedule(self,month):
        # pulling down employee's scedule for a perticular month
        response=requests.get(f"https://www.company.com/{self.last}/{month}")
        # we need to import requests library
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
    # this is a sample method that we will pretend that it will go to a companies website.
    # the information on this website we want to mock 
    # because we dont our test success depends on the website being up
    # we only care the get method went to the currect url and our code works correctly whether the response is ok or not.
    # to do this we need to import patch from unittest.mock

    "go back to test_employee_class.py"
        