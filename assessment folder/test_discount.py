import unittest
import discount

class Testdiscount(unittest.TestCase):

	def test_that_discount_funtion_exit(self):
		discount.my_discount(400,12)

	
	def test_that_discount_return_discount_result(self):
		self.assertEqual(discount.my_discount(150,15),127.5)
		self.assertEqual(discount.my_discount(100,15),85)


	def test_that_discount_function_raise_error_with_negative_amount(self):
		self.assertRaises(ValueError, discount.my_discount,-4, -3)
	

	
	
