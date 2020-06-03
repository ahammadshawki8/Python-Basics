import unittest
from employee import Employee # importing Employee class form the employee module

# created testcase which inherits from unittest.testcase
class TestEmployee(unittest.TestCase):

    # here we have 3 different tests
    def test_email(self):
        # creating 2 employees
        emp1=Employee("ahammad","shawki",10000)
        emp2=Employee("tony","starc",500)

        # testing email property
        self.assertEqual(emp1.email,"ahammadshawki@email.com")
        self.assertEqual(emp2.email,"tonystarc@email.com")

        # changing the first name
        emp1.first= "pro"
        emp2.first= "jade"

        # testing if the changing successfully executed or not
        self.assertEqual(emp1.email,"proshawki@email.com")
        self.assertEqual(emp2.email,"jadestarc@email.com")

    def test_fullname(self):
        # doing the same thing as test_email() method.

        emp1=Employee("ahammad","shawki",10000)
        emp2=Employee("tony","starc",500)

        self.assertEqual(emp1.fullname,"Ahammad Shawki")
        self.assertEqual(emp2.fullname,"Tony Starc")

        emp1.first= "pro"
        emp2.first= "jade"

        self.assertEqual(emp1.fullname,"Pro Shawki")
        self.assertEqual(emp2.fullname,"Jade Starc")

    def test_apply_raise(self):
        emp1=Employee("ahammad","shawki",10000)
        emp2=Employee("tony","starc",500)

        emp1.apply_raise()
        emp2.apply_raise()

        self.assertEqual(emp1.pay,10500)
        self.assertEqual(emp2.pay,525)

# this is slightly more complicated test then our simple calculator test.
# if we run this then we can see that all of those tests passed.
# one thing we might notice that at the beginning we are created two same employees.
# when should we see the same code over and over, we should make that code dry.
# the reason behind is that if we need to change something we dont want to change that in multiple lines
# so it would be nice if we create them from scratch in one place and reuse them in every place.
# and there is a way to do that and that is what setUp() and tearDown() method for.
# at the top of our class we will create those methods. these are CamelCase.


# lets create another class.

class TestEmployee2(unittest.TestCase):
    # setUP() and tearDown() methods.
    # setUp() method will run its code before every single test.
    def setUp(self):
        print("setUp")
        # we wanted to create those employees before every single test
        self.emp1=Employee("ahammad","shawki",10000)
        self.emp2=Employee("tony","starc",500)
        # in order to access those methods within our other tests,
        # we have to set these as instant attributes by putting self before each emp. 

        # now we can delete the creation of the employess before each test.

        # now as they are instant variables, everywhere we use emp1 and emp2, we need to add self before them.

    # tearDown() method will run its code after every single test.
    def tearDown(self):
    # we haven't using these method for anything. but we can use it.
    # lets say we have some functions where we need to add files to a directory or to a database
    # and we want to test those functions
    # then in the setUp() method we can create the directory or the database 
    # and in the tearDown() method we can delete those so that we have a clean place for next test.
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

# if we run this we can see that all tests passed.
# but lets say we want to be more specific about what we are testing.
# so we can use print method before every function.
# if we run this we can see that we have setUp and then the test and at last the tearDown for every single test.
# another thing to notice here is that tests dont run in order.
# so we should never assume that tests will run straight down through the script.
# thats why we need to keep our tests isolated from one another.

# sometimes it is also useful to run somecode at the very beginning of the test file,
# and then have some clean up code that run after all the test have been run.
# so unlike the setUp() and tearDown() which runs before and after every test,
# it would be nice if we have something that run once before everything and then once after everything.

# we can do this with 2 class method called setUpClass and tearDownClass.
# we will do that in another module.
""" go to test_employee_class """

if __name__ == "__main__":
    unittest.main()