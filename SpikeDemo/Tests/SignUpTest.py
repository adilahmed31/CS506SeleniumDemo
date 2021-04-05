import unittest
from selenium import webdriver
from SpikeDemo.Pages.LoginPage import LoginPage
from SpikeDemo.Pages.SignUpPage import SignUpPage
import os
import HtmlTestRunner

class SpikeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #Instantiate driver
        #Replace path with local path or add chromedriver to environment variable PATH
        cls.driver = webdriver.Chrome(r"C:\Users\obaid\PycharmProjects\CS506SeleniumDemo\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_signUp_validUsernamePassword_validDetails(self):
        #Load Sign-Up Page
        driver = self.driver
        driver.get("http://spikelocal/create-account/")

        #Instantiate SignUpPage class
        signup = SignUpPage(driver)

        #Regular sign-up
        signup.enter_all_details("HAL9000", "openthepodbaydoors", "1234567890", "customer", "Stripe", "1210 W Dayton St", "42", "Madison", "WI", "53706")

        #Redirect to Log-In Page
        driver.get("http://spikelocal/sign-in/")

        #Sign-In using the same details
        login = LoginPage(driver)
        login.login("HAL9000","openthepodbaydoors")

        #Check if the user is redirected  to the home page
        self.assertEqual(self.driver.current_url, "http://spikelocal/menu/")

    def test_signUp_invalidUsernamePassword_validDetails(self):
        #Load Sign-Up Page
        driver = self.driver
        driver.get("http://spikelocal/create-account/")
        signup = SignUpPage(driver)
        signup.enter_all_details("R2-D2","beepboopbeep","1234567890","customer","Stripe","1210 W Dayton St","42","Madison","WI","53706")

        #Redirect to Log-In Page
        driver.get("http://spikelocal/sign-in/")

        #Sign-In using the same details
        login = LoginPage(driver)
        login.login("R2-D2","beepboopbeep")

        #Check if the user is redirected to an error page
        self.assertEqual(self.driver.current_url, "http://spikelocal/sign-in/index.php","Invalid characters allowed in username")

    def test_signUp_validUsername_invalidPassword_validDetails(self):
        #Load Sign-Up Page
        driver = self.driver
        driver.get("http://spikelocal/create-account/")
        signup = SignUpPage(driver)
        signup.enter_all_details("deepthought","42","1234567890","customer","Stripe","1210 W Dayton St","42","Madison","WI","53706")

        #Redirect to Log-In Page
        driver.get("http://spikelocal/sign-in/")

        #Sign-In using the same details
        login = LoginPage(driver)
        login.login("deepthought","42")

        #Check if the user is redirected to an error page
        self.assertEqual(self.driver.current_url, "http://spikelocal/sign-in/index.php","Short Passwords Accepted")

    def test_signUp_validUsernamePassword_invalidDetails(self):
        #Load Sign-Up Page
        driver = self.driver
        driver.get("http://spikelocal/create-account/")
        signup = SignUpPage(driver)
        signup.enter_all_details("skynet","illbeback","xyz","customer","Stripe","1210 W Dayton St","42","Madison","WI","53706")

        #Redirect to Log-In Page
        driver.get("http://spikelocal/sign-in/")

        #Sign-In using the same details
        login = LoginPage(driver)
        login.login("skynet","illbeback")

        #Check if the user is redirected to an error page
        self.assertEqual(self.driver.current_url, "http://spikelocal/sign-in/index.php","Invalid Phone Number Accepted")

    def test_signUp_duplicateUsername_validPassword_validDetails(self):
        #Load Sign-Up Page
        driver = self.driver
        driver.get("http://spikelocal/create-account/")
        signup = SignUpPage(driver)
        signup.enter_all_details("joshua","shallweplayagame","1234567890","customer","Stripe","1210 W Dayton St","42","Madison","WI","53706")

        #Redirect to Log-In Page
        driver.get("http://spikelocal/sign-in/")

        #Sign-In using the same details
        login = LoginPage(driver)
        login.login("joshua","shallweplayagame")

        #Check if the user is redirected to an error page
        self.assertEqual(self.driver.current_url, "http://spikelocal/sign-in/index.php","Duplicate usernames are allowed")

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\obaid\PycharmProjects\CS506SeleniumDemo\SpikeDemo\Reports"))

