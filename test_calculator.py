import unittest
from unittest.mock import patch
import requests
from calculator import *
#from Project.calculator import Calculator

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #print("Setting up Class")
        pass
    
    @classmethod
    def tearDownClass(self):
        #print("Tear Down Class")
        pass

    def setUp(self):
        #print("SetUp")
        self.sut = Calculator()
    
    def tearDown(self):
        #print("TearDown")
        pass

    def testAdd(self):
        #print("TestAdd")
        #Act
        output = self.sut.add(1,2)
        #Assert
        self.assertEqual(output,3,"Add test failed")

    def testAddMultiple(self):
        a = [1,2,3,4,5]
        b = [3,4,6,5,3]
        c = [4,6,9,9,8]

        for i in range(5):
            with self.subTest(i = i):
                self.assertEqual(self.sut.add(a[i],b[i]),c[i],"Add test failed")

    @unittest.skip("demo skip")
    def testAddFail(self):
        #print("TestAddFail")
        with self.assertRaises(CalculatorError) as e:
            self.sut.add("1",2)
        self.assertEqual(str(e.exception),"Type Error")

    @unittest.expectedFailure
    def testSubtract(self):
        #Act
        output = self.sut.subtract(4,1)
        #Assert
        self.assertEqual(output,3,"Subtract test failed")

    def testDivide(self):
        #Act
        output = self.sut.divide(10,5)
        #Assert
        self.assertEqual(output,2,"Divide test failed")

    def testDivideFail(self):
        with self.assertRaises(CalculatorError) as e:
            self.sut.divide(10,0)
        self.assertEqual(str(e.exception),"ZeroDivisionError")

    def testGetVersion(self):
        with patch('calculator.requests.get') as dummy_get:
            dummy_get.return_value.ok = True
            dummy_get.return_value.text = "Test Passed"
            output = self.sut.getVersion("2000")

            dummy_get.assert_called_with('http://cs.wisc.edu/2000')
            self.assertEqual(output,"Test Passed")

def suite():
    s = unittest.TestSuite()
    s.addTest(TestCalculator('testDivide'))
    s.addTest(TestCalculator('testDivideFail'))
    return s

if __name__=="__main__":
    #unittest.main(verbosity=2)
    runner = unittest.TextTestRunner()
    runner.run(suite())