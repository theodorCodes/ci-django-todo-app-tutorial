from django.test import TestCase

# Create your tests here.


# To get started let's create a class called test Django which inherits the built-in test case class.
# Giving us access to all its functionality.
# Inside our new class. Every test will be defined as a method that begins with the word test.
# I'll create one here called test this thing works.
# And it will take in self as its only parameter.
# Self here refers to our test Django class which because it inherits the test case class
# wi'll have a bunch of pre-built methods and functionality that we can use.
# For example inside the test this thing works method.
# I'll use the built-in assert equal method to determine whether one equals zero.
# Obviously we know one is not equal to zero so this test should fail.
# To run it we can head to the terminal and use the command python3 manage.py test.

class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)
