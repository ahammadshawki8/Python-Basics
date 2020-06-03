import unittest
from employee import Employee
from unittest.mock import patch # it is for mocking

class TestEmployee(unittest.TestCase):
    # setUpClass() and tearDownClass() method
    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass\n")

    def setUp(self):
        print("setUp")

        self.emp1=Employee("ahammad","shawki",10000)
        self.emp2=Employee("tony","starc",500)

    def tearDown(self):
        print("tearDown\n")


    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email,"ahammadshawki@email.com")
        self.assertEqual(self.emp2.email,"tonystarc@email.com")

        self.emp1.first= "pro"
        self.emp2.first= "jade"

        self.assertEqual(self.emp1.email,"proshawki@email.com")
        self.assertEqual(self.emp2.email,"jadestarc@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp1.fullname,"Ahammad Shawki")
        self.assertEqual(self.emp2.fullname,"Tony Starc")

        self.emp1.first= "pro"
        self.emp2.first= "jade"

        self.assertEqual(self.emp1.fullname,"Pro Shawki")
        self.assertEqual(self.emp2.fullname,"Jade Starc")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay,10500)
        self.assertEqual(self.emp2.pay,525)

# we can see that it ran setUpClass() first 
# and then all the tests with setUp() and tearDown() 
# and at the last there is tearDownClass()


# why should we use this class methods?
# setUpClass() and tearDownClass() will be useful if we want to do something once 
# and it is too costly to do before each test.

# for example, lets say we want to read data from a database to test our methods.
# then it would be good if we read the data from the database at once in the setUpClass() and then do our tests
# and at last close the connection of the database at the tearDownClass() method.

# there is one more thing we need to learn about unit testing.
# sometimes our code relies on certain things that we have no control over.
# for example, lets say we have a function that goes to a website and pulls the information from that site.
# if the website is down then our function will fail and then our test will fail.
# but we want our test to fail if something is wrong with our code.
# so if a website is down, we cant do anything about that.
# we are going to overcome that with something called "mocking"
# now mocking is a large concept. but lets look at some basic usage of it.
# lets create our test class again.
# we have to create the method for mocking in our real class which we are testing.
"""go to employee.py"""

import unittest
from employee import Employee

class TestEmployee2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass\n")

    def setUp(self):
        print("setUp")

        self.emp1=Employee("ahammad","shawki",10000)
        self.emp2=Employee("tony","starc",500)

    def tearDown(self):
        print("tearDown\n")


    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email,"ahammadshawki@email.com")
        self.assertEqual(self.emp2.email,"tonystarc@email.com")

        self.emp1.first= "pro"
        self.emp2.first= "jade"

        self.assertEqual(self.emp1.email,"proshawki@email.com")
        self.assertEqual(self.emp2.email,"jadestarc@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp1.fullname,"Ahammad Shawki")
        self.assertEqual(self.emp2.fullname,"Tony Starc")

        self.emp1.first= "pro"
        self.emp2.first= "jade"

        self.assertEqual(self.emp1.fullname,"Pro Shawki")
        self.assertEqual(self.emp2.fullname,"Jade Starc")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay,10500)
        self.assertEqual(self.emp2.pay,525)

    ## Mocking ##
    # there is couple of different ways that we can use patch.
    # we can use it either a decorator or as a context manager.
    # it will allow us to mock an object during the test and that object will automatically restored after the test has run.
    # so lets first create a test method for monthly_scedule() function.
    def test_monthly_scedule(self):
        # we are going to use patch for mocking as a context manager
        with patch("employee.requests.get") as mocked_get:
            # here within the patch we passed what we want to mock which is request.get of the employee module
            # and then we are setting that equal to mocked_get

            # we may wonder why would we import request into our test and mocked that?
            # thats is because we want to mock this objects where they are actually used currently it is in the employee module.

            # now we can assign the return value insted of going up to the website
            # we can test a successful call by saying,
            mocked_get.return_value.ok=True
            # we want this return value of ok to True
            # lets also set the text of the returned value.
            mocked_get.return_value.text="IT IS SUCCESSFUL :)"

            # so in our employee module if its response.ok is true, then we will get our response.text back

            # now within this context manager, lets run our monthly scedule method just like we are testing it.
            scedule = self.emp1.monthly_scedule("May") # here we pass the month name, it is not useful in this context.
            # one cool thing about mock is that, they actually record when they are called and with what values.
            # so we want to make sure that the get method is called with the currect url.
            # to do this we can,
            mocked_get.assert_called_with("https://www.company.com/shawki/May")
            # this url is from the employee class
            # after we know that the method is called with correct url, 
            # lets make sure that this method has returned the correct text.         
            self.assertEqual(scedule,"IT IS SUCCESSFUL :)")

            # now if we run this code, we can see that all of our test has passed.
            # last thing is that we want to test a failed response.
            # we can do the exact same thing.
            mocked_get.return_value.ok=False # setting ok value to False so that it returns bad response from the website.

            scedule = self.emp2.monthly_scedule("June")
            mocked_get.assert_called_with("https://www.company.com/starc/June")

            self.assertEqual(scedule,"Bad Response!")

            # if we run this we can see that all of our tests passed

# this mocking can be little confusing when we first see it.
# we dont use it much unless we are accessing with real urls which are basically out of our control.
# so whenever we do need it it is nice to know the basics about how to use them.


if __name__ == "__main__":
    unittest.main()

"""
go to the main module
python43 (unit testing).py
"""