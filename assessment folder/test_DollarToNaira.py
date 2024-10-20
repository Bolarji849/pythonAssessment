import unittest
import DollarToNaira
import divie

class TestDollarToNaira(unittest.TestCase):

	def test_that_DollarToNaira_funtion_exit(self):
		DollarToNaira.covert_dollars_to_niara(400)

	
	def test_that_DollarToNaira_return_DollarToNaira_result(self):
		self.assertEqual(DollarToNaira.covert_dollars_to_niara(400),620000)
		self.assertEqual(DollarToNaira.covert_dollars_to_niara(100),155000)


	def test_that_DollarToNaira_function_raise_error_with_negative_amount(self):
		self.assertRaises(ValueError, DollarToNaira.covert_dollars_to_niara, -3)
	

	def test_that_DollarToNaira_function_handles_rounding_issues(self):
		self.assertAlmostEqual(DollarToNaira.covert_dollars_to_niara(90000.009), 139500013.95, places=2)

	def test_that_covert_currency_funtion_raise_error_with_string_value(self):
		self.assertEqual(convert_currency("williams-Gstring"),"invalid input")



	
class TestDivideOrSquare(TestCase):
	def test_that_divide_or_square_function_exist(self):
		divide_or_square(1)

	def test_that_divide_or_square_function_return_correct_value(self):
		self.assertEqual(divide_or_square(10),3)

