import unittest
import Addition



class TestAddition(unittest.TestCase):

	def test_that_addition_funtion_exit(self):
		Addition.addition(3,4)
	
	
	def test_that_addition_funtion_return_addition(self):
		self.assertEqual(Addition.addition("3", "4"), "7" )


	def test_that_addition_function_return_error_with_string_value(self):	
		self.assertRaises(TypeError, Addition.addition, "learn")
								