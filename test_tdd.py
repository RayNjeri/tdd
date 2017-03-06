import unittest
from tdd import test_solution

class Test_solution(unittest.TestCase):
	def test_addition(self):
		self.assertTrue(test_solution.solution(10,20, "+"),30)


	def test_subtraction(self):
		self.assertTrue(test_solution.solution(10,20,"-"),-10)
		

	def test_multiplication(self):
		self.assertTrue(test_solution.solution(10,20,"*"),200)

	def test_division(self):
		self.assertTrue(test_solution.solution(20,5,"/"),4)

	def test_modulo(self):
		self.assertTrue(test_solution.solution(20,3,"%"),2)	

if __name__=="__main__":
    unittest.main()