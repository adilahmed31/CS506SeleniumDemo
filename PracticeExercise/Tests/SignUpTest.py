from PracticeExercise.Pages.SignUpPage import SignUpPage
from selenium import webdriver
import unittest
import HtmlTestRunner

class SignUpTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\obaid\PycharmProjects\CS506SeleniumDemo\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testSignUp(self):
        driver = self.driver
        signup = SignUpPage(driver)
        #enter_details(self, firstName, lastName,email, password, day, month, year, firstNameAddress, lastNameAddress,
                          #address, city, state, zipcode, country, mobilephone, alias):
        signup.enter_details("Samantha","Johansson","samantha@her.com","thepastisjustastorywekeeptellingourselves","13","12","2013","Theodore","Twombly","The Cloud","Los Angeles","CA","94129","United States","6011111111","Her")