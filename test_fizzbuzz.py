import unittest # This is the default Python testing library. unittest

from fizzbuzz import generate
# We import our generate function from the fizzbuzz module (file)

class TestFizzbuzz(unittest.TestCase):  # Sets up a new test case
    def test_lists_values_up_to_one(self):  # This is a test, don't forget `self`!
        self.assertEqual(
            generate(1), 
            "1"
        )

    def test_lists_values_up_to_two(self):
        self.assertEqual(
            generate(2), 
            "1, 2"
        )

    def test_fizz_for_three(self):
        self.assertEqual(
            generate(3),
            "1, 2, Fizz"
        )
    
    def test_buzz_for_five(self):
        self.assertEqual(
            generate(5),
            "1, 2, Fizz, 4, Buzz"
        )
    
    def test_fizzbuzz_for_fifteen(self):
        self.assertEqual(
            generate(15),
            "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz"
        )