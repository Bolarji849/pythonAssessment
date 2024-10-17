import unittest
import SwapNumber



class TestSwapNumber(unittest.TestCase):

	def test_that_swap_number_funtion_exit(self):
		SwapNumber.get_swap_number([1,2,3,4,6,5])
	
	
	def test_that_get_swap_number_return_array(self):
		given = [1,2,3,4,6,5]
		expected = [2,1,4,3,5,6]
		self.assertEqual(SwapNumber.get_swap_number(given),expected)


	