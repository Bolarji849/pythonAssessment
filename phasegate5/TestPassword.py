import unittest
import Password
import string
class TestPassword(unittest.TestCase):

	def test_that_password_funtion_exit(self):
		Password.generate_password()

	def test_that_lower_case_letter_funtion_exit(self):
		Password.get_lowercase_letters()

	def test_that_upper_case_letter_funtion_exit(self):
		Password.get_upper_letters()

	def test_that_numbers_funtion_exit(self):
		Password.get_numbers_letters()

	def test_that_symbols_funtion_exit(self):
		Password.get_symbols_letters()

	

	def test_that_upper_case_letter_funtion_(self):
		password = Password.generate_password()
		self.assertTrue(any(c for c in password if c.isupper()))

	def test_that_lower_case_letter_funtion_(self):
		password = Password.generate_password()
		self.assertTrue(any(c for c in password if c.islower()))

	def test_that_number_funtion_(self):
		password = Password.generate_password()
		self.assertTrue(any(c for c in password if c.isdigit()))

	def test_that_symbol_funtion_(self):
		symbols = string.punctuation
		password = Password.generate_password()
		self.assertTrue(any(c for c in password if symbols.__contains__(c)))
	
	