from PracticeExercise.Pages.SignUpPage import SignUpPage
from PracticeExercise.Pages.LoginPage import LoginPage
from selenium import webdriver
import time
import unittest
import HtmlTestRunner

class SignUpTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Replace path with local path or add chromedriver to environment variable PATH
        cls.driver = webdriver.Chrome(r"C:\Users\obaid\PycharmProjects\CS506SeleniumDemo\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

#This function is a mess and can be cleaned up a bit. Does the job rn tho
    def testSignUp(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation")
        signup = SignUpPage(driver)
        firstName = "Samantha"
        lastName = "AI"
        #change email each time the code is run to avoid duplicate email ID errors
        email = "samantha@her.com"
        signup.initiate_signup(email)
        #enter_details(self, firstName, lastName,email, password, day, month, year, firstNameAddress, lastNameAddress,
                          #address, city, state, zipcode, country, mobilephone, alias):
        signup.enter_details(firstName,lastName,email,"whatdoesababycomputercallitsdad","13","12","2013","Theodore","Twombly","The Cloud","Los Angeles","California","94129","United States","6011111111","Her")
        #Successful sign-up logs the user in automatically. Check if the username display on the top right returns the correct value
        driver.get("http://automationpractice.com/")
        self.assertEqual(signup.check_signup_success(firstName,lastName), True, "Registration Failed")

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    #Replace with local path
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\obaid\PycharmProjects\CS506SeleniumDemo\PracticeExercise\Reports"))