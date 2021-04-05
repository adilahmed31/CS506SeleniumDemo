from PracticeExercise.Pages.SearchPage import SearchPage
from selenium import webdriver
import unittest
import HtmlTestRunner


class HomePageSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\obaid\PycharmProjects\CS506SeleniumDemo\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testSearchResults(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        search = SearchPage(driver)
        search.search("chiffon")
        product_list = driver.find_element_by_class_name("product_list grid row")
        isFound = product_list.find_elements_by_partial_link_text("Printed Chiffon Dr").size() > 0
        self.assertEqual(isFound, true, "Product Not Found")

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\obaid\PycharmProjects\CS506SeleniumDemo\PracticeExercise\Reports"))