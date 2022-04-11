from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Login_page(Browser):

    FORM_AUTHENTICATION = (By.XPATH, '//a[text()="Form Authentication"]')
    USER_INPUT = (By.XPATH, '//input[@id="username"]')
    PASS_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//i')
    ELEM_SELENIUM_BUTTON = (By.XPATH, '//a[text()="Elemental Selenium"]')

    def navigate_to_home_page(self):
        self.driver.get('https://the-internet.herokuapp.com')

    def navigate_to_form_authentication(self):
        self.driver.find_element(*self.FORM_AUTHENTICATION).click()

    def set_username(self, username):
        self.driver.find_element(*self.USER_INPUT).send_keys(username)

    def set_pass(self, password):
        self.driver.find_element(*self.PASS_INPUT).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_elem_selenium(self):
        self.driver.find_element(*self.ELEM_SELENIUM_BUTTON).click()

    def user_login(self, username, password):
        self.navigate_to_form_authentication()
        self.set_username(username)
        self.set_pass(password)
        self.click_login_btn()
