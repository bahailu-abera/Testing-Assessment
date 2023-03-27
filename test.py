"""
Test module for string module
"""
import unittest
from string_functions import *


class TestToUpper(unittest.TestCase):

    def test_to_upper(self):
        """
        Test to_upper method of the string module
        """
        self.assertEqual(to_upper('hello'), 'HELLO')
        self.assertEqual(to_upper('Hello'), 'HELLO')
        self.assertEqual(to_upper(''), '')
        self.assertEqual(to_upper('helLO2423!'), 'HELLO2423!')


class TestToLower(unittest.TestCase):
    # your code goes here
    pass


class TestCapitalize(unittest.TestCase):
    # your code goes here
    pass


if __name__ == '__main__':
    unittest.main()
