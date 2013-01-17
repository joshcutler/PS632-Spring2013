import unittest
import inlab1

class TestInLab1Code(unittest.TestCase):

	def setUp(self): 
		return 

	# Correctness tests 

	def test_binarify_16(self):
		self.assertEqual(inlab1.binarify(16), "10000")

	def test_binarify_127(self):
		self.assertEqual(inlab1.binarify(127), "1111111")

	def test_binarify_0(self):
		self.assertEqual(inlab1.binarify(0), "0")

	def test_binarify_negative(self):
		self.assertEqual(inlab1.binarify(-16), "0")

	def test_anyary_16(self):
		self.assertEqual(inlab1.anyary(16, 2), "10000")

	def test_anyary_base3(self):
		self.assertEqual(inlab1.anyary(10, 3), "101")

	# base_to_int
	def test_base_to_int_16(self):
		self.assertEqual(inlab1.base_to_int(inlab1.anyary(16,2), 2), 16)

	def test_base_to_int_3(self):
		self.assertEqual(inlab1.base_to_int("110", 3), 12)

	def test_base_to_int_10(self):
		self.assertEqual(inlab1.base_to_int("16", 10), 16)

	def test_base_to_int_0(self):
		self.assertEqual(inlab1.base_to_int("123", 0), 0)

	def test_base_to_int_negative(self):
		self.assertEqual(inlab1.base_to_int("-10000", 2), -16)

if __name__ == '__main__':
  unittest.main()	