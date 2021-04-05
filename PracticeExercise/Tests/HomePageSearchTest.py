from PracticeExercise.Pages.SearchPage import SearchPage
from selenium import webdriver
import unittest
import HtmlTestRunner


class HomePageSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Replace path with local path or add chromedriver to environment variable PATH
        cls.driver = webdriver.Chrome(r"C:\Users\obaid\PycharmProjects\CS506SeleniumDemo\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testSearchResults(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        search = SearchPage(driver)
        search.search("chiffon")
        #Create element object for product list and search within the list
        product_list = driver.find_element_by_xpath("//body/div[@id='page']/div[2]/div[1]/div[3]/div[2]/ul[1]")
        search_results = product_list.find_elements_by_partial_link_text("Printed Chiffon Dr")
        print(search_results)
        isFound = len(search_results) > 0
        self.assertEqual(isFound, True, "Product Not Found")

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