from selenium.webdriver.support.ui import Select
from SpikeDemo.Locators.locators import Locators
class SignUpPage():

    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_name = Locators.signup_username_textbox_name
        self.password_textbox_name = Locators.signup_password_textbox_name
        self.accounttype_dropdown_id = Locators.accounttype_dropdown_id
        self.paymenttype_dropdown_id = Locators.paymenttype_dropdown_id
        self.phonenumber_textbox_id = Locators.phonenumber_textbox_id
        self.address_textbox_name = Locators.address_textbox_name
        self.apartmentnumber_textbox_name = Locators.apartmentnumber_textbox_name
        self.city_textbox_name = Locators.city_textbox_name
        self.state_dropdown_id = Locators.state_dropdown_id
        self.zipcode_textbox_name = Locators.zipcode_textbox_name
        self.signup_button_name = Locators.zipcode_textbox_name

    def enter_username(self,username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_account_type(self,accounttype):
        account_type = Select(self.driver.find_element_by_id(self.accounttype_dropdown_id))
        account_type.select_by_value(accounttype)

    def enter_phonenumber(self, phonenumber):
        self.driver.find_element_by_id(self.phonenumber_textbox_id).send_keys(phonenumber)

    def enter_address(self,address):
        self.driver.find_element_by_name(self.address_textbox_name).send_keys(address)

    def enter_apartmentnumber(self, apartmentnumber):
        self.driver.find_element_by_name(self.apartmentnumber_textbox_name).send_keys(apartmentnumber)

    def enter_payment_type(self, paymenttype):
        payment_type = Select(self.driver.find_element_by_id(self.paymenttype_dropdown_id))
        payment_type.select_by_value(paymenttype)

    def enter_city(self,city):
        self.driver.find_element_by_name(self.city_textbox_name).clear()
        self.driver.find_element_by_name(self.city_textbox_name).send_keys(city)

    def enter_state(self,state):
        state_id = Select(self.driver.find_element_by_id(self.state_dropdown_id))
        state_id.select_by_value(state)

    def enter_zip(self,zip):
        self.driver.find_element_by_name(self.zipcode_textbox_name).clear()
        self.driver.find_element_by_name(self.zipcode_textbox_name).send_keys(zip)

    def enter_password(self,password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element_by_name(self.signup_button_name).click()

    def enter_all_details(self, username, password, phonenumber, accounttype, paymenttype, address, apartmentnumber, city, state, zipcode):
        self.enter_username(username)
        self.enter_password(password)
        self.enter_phonenumber(phonenumber)
        self.enter_account_type(accounttype)
        self.enter_payment_type(paymenttype)
        self.enter_address(address)
        self.enter_apartmentnumber(apartmentnumber)
        self.enter_city(city)
        self.enter_state(state)
        self.enter_zip(zipcode)
        self.click_submit_button()