import unittest
from tdd import test_solution

class Test_solution(unittest.TestCase):
	def test_addition(self):
		self.assertTrue(test_solution.solution(10,20, "+"),30)


	def test_subtraction(self):
		self.assertTrue(test_solution.solution(10,20,"-"),-10)
		

	def test_multiplication(self):
		self.assertTrue(test_solution.solution(10,20,"*"),200)


if __name__=="__main__":
    unittest.main()