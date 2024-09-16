import unittest
import DollarToNaira

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
	
