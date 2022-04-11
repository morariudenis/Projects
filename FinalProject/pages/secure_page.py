from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from login_page import Login_page
from pages.base_page import BasePage

# Secure page https://the-internet.herokuapp.com/secure
# Sa contina mesajul de succes si verificare ca e displayed
# Sa contina logout_btn si click pe el

class Secure_page(BasePage):

    FORM_AUTHENTICATION = (By.XPATH, '//a[text()="Form Authentication"]')
    USER_INPUT = (By.XPATH, '//input[@id="username"]')
    PASS_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//i')
    # LOGIN = Login_page.user_login()
    LOGOUT_BUTTON = (By.XPATH, '//a[@class="button secondary radius"]')
    SUCCESS = (By.XPATH, '//div[@class="flash success"]')

    def navigate_to_home_page(self):
        self.driver.get('https://the-internet.herokuapp.com')

        # DESI AM IMPORTAT CLASA CU LOGIN PAGE SA IAU DIRECT DE ACOLO CE AM NEVOIE
         # PENTRU LOGIN.. NU STIU CUM TREBUIE SA APELEZ CLASA SI METODA CA SA O POT FOLOSI

    def navigate_to_form_authentication(self):
        self.driver.find_element(*self.FORM_AUTHENTICATION).click()


    def set_username(self, username):
        self.driver.find_element(*self.USER_INPUT).send_keys(username)

    def set_pass(self, password):
        self.driver.find_element(*self.PASS_INPUT).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def success_visible(self):
        cuv = self.driver.find_element(By.XPATH, '//div[@id="flash"]').text
        if cuv.__contains__('secure area!'):
            print('Textul contine: secure area!')

    def success_displayed(self):
            elem = self.driver.find_element(*self.SUCCESS)
            if elem.is_displayed():
                print('Success text e vizibil')
