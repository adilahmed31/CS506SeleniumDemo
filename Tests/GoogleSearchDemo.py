from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Users\obaid\Downloads\chromedriver_win32\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("Selenium")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

driver.maximize_window()
driver.refresh()

time.sleep(3)
driver.close()

driver.quit()