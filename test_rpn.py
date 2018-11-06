import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	
	def test_sub(self):
		result = rpn.calculate('1 1 -')
		self.assertEqual(0, result)

	def test_toomany(self):
		with self.assertRaises(ValueError):
			result = rpn.calculate('1 2 3 +')

	def test_pow(self):
		result = rpn.calculate('2 2 ^')
		self.assertEqual(4, result)
