import unittest
import divide_or_square



class Testdivide_or_square(unittest.TestCase):

	def test_that_divide_or_squarefuntion_exit(self):
		divide_or_square.divide_or_square(3)
	
	
	def test_that_divide_or_square_funtion_return_divide_or_square(self):
		self.assertEqual(divide_or_square.divide_or_square(25),  5)
		
		
	def test_that_divide_or_square_function_raise_error_with_negative_amount(self):
		self.assertRaises(ValueError, divide_or_square.divide_or_square, (-3))

	def test_that_divide_or_square_function_return_error_with_string_value(self):
		self.assertRaises(TypeError, divide_or_square.divide_or_square, "learn")
											