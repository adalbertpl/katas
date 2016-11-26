import unittest
import re
import itertools
import string

class StringCalculator:
	def add(self, numbers):
		lines = numbers.split("\n")
		separator = ","
		if len(lines) != 0 and lines[0].startswith("//"):
			if len(lines[0]) == 2:
				raise "Wrong data format"

			separator = lines[0][2]
			lines = lines[1:]

		numberList = itertools.chain.from_iterable([line.split(separator) for line in lines])

		numberSum = 0
		for number in numberList:
			if (number == ''):
				continue

			intNum = int(number)
			if (intNum < 0):
				raise BaseException("Negative not allowed: " + str(intNum))

			numberSum += intNum 
		return numberSum

class TestStringCalculator(unittest.TestCase):
	def setUp(self):
		self.sc = StringCalculator()

	def test_empty(self):
		self.assertEqual(self.sc.add(""), 0)

	def test_one_number(self):
		self.assertEqual(self.sc.add("0"), 0)
		self.assertEqual(self.sc.add("1"), 1)

	def test_two_numbers(self):
		self.assertEqual(self.sc.add("0,1"), 1)
		self.assertEqual(self.sc.add("1,2"), 3)
		self.assertEqual(self.sc.add("11,1"), 12)

	def test_multiple_numbers(self):
		self.assertEqual(self.sc.add("0,0,0"), 0)
		self.assertEqual(self.sc.add("1,2,3,4,5"), 15)

	def test_new_line_delimiter(self):
		self.assertEqual(self.sc.add("0\n0"), 0)
		self.assertEqual(self.sc.add("1\n2"), 3)
		self.assertEqual(self.sc.add("1,2\n3"), 6)

	def test_custom_delimiter(self):
		self.assertEquals(self.sc.add("//;\n0"), 0)
		self.assertEquals(self.sc.add("//;\n0;0"), 0)
		self.assertEquals(self.sc.add("//;\n1;2;3"), 6)
		self.assertEquals(self.sc.add("// \n1 2 3 1001 4 150"), 1161)

	def test_negative_number(self):
		with self.assertRaises(object) as cm:
			self.sc.add("-1")
		self.assertEqual(str(cm.exception), "Negative not allowed: -1")

		with self.assertRaises(object) as cm:
			self.sc.add("2\n8,4,-3,-6")
		self.assertEqual(str(cm.exception), "Negative not allowed: -3")

if __name__ == '__main__':
	unittest.main()