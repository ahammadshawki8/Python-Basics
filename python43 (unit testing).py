# unit testing

# in this module, we will learn how to unit test our code.
# we will learn how to write test, how to set up test and also some best practises.

# we should test our code when we are working in projects.
# testing the code is the most exciting thing to do and we need to know how to properly write test.
# the reason for that is testing saves a lots of time and headache for us.
# again when we unit test our code it gives us much confidence 
# about the update and refactoring dont have any unexpected consiquences and break our code anyway.

# for example, if we update a function in our project, 
# that function may broke several code blocks in our code even though itself is still working.
# good unit test will make sure that everything is working good as they should.
# and if it is not working then, it will show us exactly what block has broken


# lets get started
""" we can find all the children files for this module in python43 (unit testing) folder"""
""" so that will be our current workspace"""

""" go to calc.py """

# there we have some simple functions.


# a lot of us use print statement and test our code.
# but testing our code this way isn't easy to automate.
# it is also hard to maintain as if we test for lot of function we cant see at a glance that what failed and what succeeded.
# that where we need unit testing.

# for unit testing we need to first create a test module.
# we are going to name it test_calc.py
# it is convention that our testing file starts with test_ and then what we are testing.

""" go to test_calc.py file """

# now we have seen unit testing with simple function.
# now lets do unit testing with slightly more difficult code.

""" go to employee.py file """
""" go to test_employee.py file """
""" go to test_employee_class """

# before we finish up, we need to learn few things about best practises.

# practise 1:
# test should be isolated.
# it means our test should not rely or depend on other tests.
# so we should be able to run any test by itself independent to other tests.

# practise 2:
# we will notice that we were adding test in existing code.
# we may have heared something called "test driven development".
# it is basically means we write the test before we write the code.
# that might sound strange but sometimes it is useful.
# we dont need to strictly follow "test driven development".
# but basically the concept is we should think about what our d=code will do before writing the code.
# and then write the test implementing that behaviour 
# and then watch the tests to fail as their is no code to overcome that.
# and finally, write the code to amke the test successful.

# NOTE: any testing is better than no testing.
# so we dont need to feel bad if we are not master in testing, mock or things like that.
# we should need to able to write some basic assertions.

# there is another test framework called pytest which lot of people like to use than the bulit in unittest library.

