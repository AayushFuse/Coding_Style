"""
Create a function that validates email addresses based on following set of rules:
Proper email format such as presence of “@”, no space in the address
Presence of valid email providers such as yahoo, gmail and outlook.
Make sure there are no no disposable email providers such as yopmail.
"""

import unittest
from validate_email import validate_email


class TestEmail(unittest.TestCase):
    """
    Usecases for Unit Test
    """
    def test_gmail(self):
        """checking if gmail is valid"""
        self.assertTrue(validate_email("ayushregmi@gmail.com"))

    def test_yahoo(self):
        """checking if yahoo is valid"""
        self.assertTrue(validate_email("ayushregmi@yahoo.com"))

    def test_outlook(self):
        """checking if outlook is valid"""
        self.assertTrue(validate_email("ayushregmi@outlook.com"))

    def test_yopmain(self):
        """checking if yopmain is valid or not"""
        self.assertFalse(validate_email("ayushregmi@yopmain.com"))

    def test_random(self):
        """checking if random mail is valid"""
        self.assertFalse(validate_email("ayush@fusemachines.com"))


if __name__ == "__main__":
    unittest.main()
