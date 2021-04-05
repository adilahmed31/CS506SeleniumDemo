from PracticeExercise.Locators.locators import Locators
from selenium.webdriver.support.ui import Select

class SignUpPage():

    def __init__(self,driver):
        #These can also be called directly from within the methods using the locators class rather than being initialized in the contructor
        self.driver = driver
        self.title_radiobutton_name = Locators.title_radiobutton_name
        self.firstName_textbox_name = Locators.firstName_textbox_name
        self.lastName_testbox_name = Locators.lastName_testbox_name
        self.email_textbox_name = Locators.email_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.dayOfBirth_dropdown_name = Locators.dayOfBirth_dropdown_name
        self.monthOfBirth_dropdown_name = Locators.monthOfBirth_dropdown_name
        self.yearOfBirth_dropdown_name = Locators.yearOfBirth_dropdown_name
        self.firstNameForAddress_textbox_name = Locators.firstNameForAddress_textbox_name
        self.lastNameForAddress_textbox_name = Locators.lastNameForAddress_textbox_name
        self.address_textbox_name = Locators.address_textbox_name
        self.city_textbox_name = Locators.city_textbox_name
        self.state_dropdown_name = Locators.state_dropdown_name
        self.zip_textbox_name = Locators.zip_textbox_name
        self.country_dropdown_id = Locators.country_dropdown_id
        self.mobilephone_textbox_name = Locators.mobilephone_textbox_name
        self.addressAlias_textbox_name = Locators.addressAlias_textbox_name
        self.register_button_name = Locators.register_button_name

    def select_title(self,title):
        if(title == "Mr."):
            self.driver.find_element_by_name(self.title_radiobutton_name+"1").click()
        if(title == "Mrs."):
            self.driver.find_element_by_name(self.title_radiobutton_name+"2").click()

    def enter_first_name(self,firstName):
        self.driver.find_element_by_name(self.firstName_textbox_name).send_keys(firstName)

    def enter_last_name(self,lastName)
        self.driver.find_element_by_name(self.lastName_testbox_name).send_keys(lastName)

    def enter_email(self,email):
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def select_day_of_birth(self,day):
        day_of_birth = Select(self.driver.find_element_by_name(self.dayOfBirth_dropdown_name))
        day_of_birth.select_by_value(day)

    def select_month_of_birth(self,month):
        month_of_birth = Select(self.driver.find_element_by_name(self.monthOfBirth_dropdown_name))
        month_of_birth.select_by_value(month)

    def select_year_of_birth(self,year):
        year_of_birth = Select(self.driver.find_element_by_name(self.yearOfBirth_dropdown_name))
        year_of_birth.select_by_value(year)

    def enter_first_name_address(self,firstName):
        self.driver.find_element_by_name(self.firstNameForAddress_textbox_name_textbox_name).send_keys(firstName)

    def enter_last_name_address(self,lastName):
        self.driver.find_element_by_name(self.lastNameForAddress_textbox_name).send_keys(lastName)

    def enter_address(self,address):
        self.driver.find_element_by_name(self.address_textbox_name).send_keys(address)

    def enter_city(self,city):
        self.driver.find_element_by_name(self.city_textbox_name).send_keys(city)

    def select_state(self,state):
        day_of_birth = Select(self.driver.find_element_by_name(self.state_dropdown_name))
        day_of_birth.select_by_value(state)

    def enter_zip(self,zipcode):
        self.driver.find_element_by_name(self.zip_textbox_name).send_keys(zipcode)

    def select_country(self,country):
        country = Select(self.driver.find_element_by_id(self.country_dropdown_id))
        country.select_by_visible_text(country)

    def enter_mobilephone(self,mobilephone):
        self.driver.find_element_by_name(self.mobilephone_textbox_name).send_keys(mobilephone)

    def enter_address_alias(self,alias):
        self.driver.find_element_by_name(self.addressAlias_textbox_name).send_keys(alias)

    def click_button(self):
        self.driver.find_element_by_name(self.title_radiobutton_name).click()

    def enter_details(self, firstName, lastName, email, password, day, month, year, firstNameAddress, lastNameAddress, address, city, state, zipcode, country, mobilephone, alias):
        #self.select_title(title)
        self.enter_first_name(firstName)
        self.enter_last_name(lastName)
        self.enter_email(email)
        self.enter_password(password)
        self.select_day_of_birth(day)
        self.select_month_of_birth(month)
        self.select_year_of_birth(year)
        self.enter_first_name_address(firstNameAddress)
        self.enter_last_name_address(lastNameAddress)
        self.enter_address(address)
        self.enter_city(city)
        self.select_state(state)
        self.enter_zip(zipcode)
        self.select_country(country)
        self.enter_mobilephone(mobilephone)
        self.enter_address_alias(alias)
        self.click_button()