from PracticeExercise.Locators.locators import Locators

class SearchPage():

    def __init__(self,driver):
        self.driver=driver
        self.search_textbox_name = Locators.search_textbox_name
        self.search_button_name = Locators.search_button_name

    def search(self,query):
        self.driver.find_element_by_name(self.search_textbox_name).send_keys(query)
        self.driver.find_element_by_name(self.search_button_name).click()