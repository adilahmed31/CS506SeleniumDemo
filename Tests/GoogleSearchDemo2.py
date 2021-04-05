from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
import time

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\obaid\Downloads\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_selenium(self):
        self.driver.get("http://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Selenium" + Keys.ENTER)

    def test_search_unittest(self):
        self.driver.get("http://www.google.com")
        self.driver.find_element_by_name("xy").send_keys("Unit Testing" + Keys.ENTER)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\obaid\PycharmProjects\CS506SeleniumDemo\Reports"))