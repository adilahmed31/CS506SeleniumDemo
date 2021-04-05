from SpikeDemo.Locators.locators import Locators

class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_name = Locators.login_username_textbox_name
        self.pasword_textbox_css_selector = Locators.login_password_textbox_css_selector
        self.login_button_name = Locators.login_button_name

    def enter_username(self,username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_css_selector(self.pasword_textbox_css_selector).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()