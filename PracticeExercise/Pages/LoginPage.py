from PracticeExercise.Locators.locators import Locators

class LoginPage():

    def __init__(self,driver):
        self.driver=driver


    def login(self,email,password):
        self.driver.find_element_by_name(Locators.login_email_textbox_name).send_keys(email)
        self.driver.find_element_by_name(Locators.login_password_textbox_name).send_keys(password)
        self.driver.find_element_by_name(Locators.login_button_name).click()