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
    
    def test_to_lower(self):
        """
        Test to_lower method of the string module
        """
        self.assertEqual(to_lower('hello'), 'hello')
        self.assertEqual(to_lower('Hello'), 'hello')
        self.assertEqual(to_lower(''), '')
        self.assertEqual(to_lower('HELLO'), 'hello')
        self.assertEqual(to_lower('helLO2423!'), 'hello2423!')


class TestCapitalize(unittest.TestCase):
    
    def test_capitalize(self):
        """
        Test capitalize method of the string module
        """
        self.assertEqual(capitalize('hello'), 'Hello')
        self.assertEqual(capitalize('Hello'), 'Hello')
        self.assertEqual(capitalize(''), '')
        self.assertEqual(capitalize('HELLO'), 'Hello')
        self.assertEqual(capitalize('helLO2423!'), 'Hello2423!')

if __name__ == '__main__':
    unittest.main()
