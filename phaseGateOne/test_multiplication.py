import unittest
import multiplication



class Testmultiplication(unittest.TestCase):

	def test_that_multiplication_funtion_exit(self):
		multiplication.number_multiplication(3, 4)
	
	
	def test_that_multiplication_funtion_return_multiplication_result(self):
		self.assertEqual(multiplication.number_multiplication(2, 2), 4)
		self.assertEqual(multiplication.number_multiplication(2, 4), 8)
		

	def test_that_multiplication_function_return_error_with_string_value(self):
		self.assertRaises(TypeError, multiplication.number_multiplication, "pen")
			
	
								