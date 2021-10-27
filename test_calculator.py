import unittest
from calculator import *

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
        #Act
        output = self.sut.add(1,2)
        #Assert
        self.assertEqual(output,3,"Add test failed")

    #run multiple test cases of the same type at once using subtest
    def testAddMultiple(self):
        a = [1,2,3,4,5]
        b = [3,4,6,5,3]
        c = [4,6,9,9,8]

        for i in range(5):
            with self.subTest(i = i):
                self.assertEqual(self.sut.add(a[i],b[i]),c[i],"Add test failed")

    #use decorator to instruct the test runner to skip the test
    @unittest.skip("demo skip")
    def testAddFail(self):
        #print("TestAddFail")
        with self.assertRaises(CalculatorError) as e:
            self.sut.add("1",2)
        self.assertEqual(str(e.exception),"Type Error")

    #use decorators to instruct the test runner to expect a failure
    @unittest.expectedFailure
    def testSubtract(self):
        #Act
        output = self.sut.subtract(4,1)
        #Assert
        self.assertEqual(output,4,"Subtract test failed")

    #test division
    def testDivide(self):
        #Act
        output = self.sut.divide(10,5)
        #Assert
        self.assertEqual(output,2,"Divide test failed")

    #Handle division failure errors
    def testDivideFail(self):
        with self.assertRaises(CalculatorError) as e:
            self.sut.divide(10,0)
        self.assertEqual(str(e.exception),"ZeroDivisionError")

    #Mock a function call for testing
    def testGetVersion(self):
        with patch('calculator.requests.get') as dummy_get:
            dummy_get.return_value.ok = True
            dummy_get.return_value.text = "Test Passed"
            output = self.sut.getVersion("2000")

            dummy_get.assert_called_with('http://cs.wisc.edu/2000')
            self.assertEqual(output,"Test Passed")

#Run only specific tests
def suite():
    s = unittest.TestSuite()
    s.addTest(TestCalculator('testDivide'))
    s.addTest(TestCalculator('testDivideFail'))
    return s

if __name__=="__main__":
    unittest.main(verbosity=2)
    #runner = unittest.TextTestRunner()
    #runner.run(suite())