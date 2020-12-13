from calgrade import calGrade
import unittest


class Test_CalGrade(unittest.TestCase):
    def testSumFunctionA(self):
        self.assertEqual(calGrade(80),"A") 

    def testSumFunctionB(self):
        self.assertEqual(calGrade(70),"B") 

    def testSumFunctionC(self):
        self.assertEqual(calGrade(60),"C") 

    def testSumFunctioD(self):
        self.assertEqual(calGrade(50),"D") 

    def testSumFunctioF(self):
        self.assertEqual(calGrade(40),"F") 


