import unittest
import divide

class Testdivide(unittest.TestCase):

	def test_that_divide_funtion_exit(self):
		divide.square(10)
	
	def test_that_divide_funtion_return_dive_result(self):
		self.assertEqual(divide.square(10),  3.1622776601683795)
		self.assertEqual(divide.square(7), 1.4)

	def test_that_divide_function_raise_error_with_negative_amount(self):
		self.assertRaises(ValueError,divide.square,-3)

	def test_that_divide_function_raise_error_with_string_value(self):
		self.assertRaises(TypeError,divide.square,"1", "5", "6","10","-3","-4")

	
