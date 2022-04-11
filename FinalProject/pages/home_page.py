from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Impementati 3 pagini in noul proiect BDD cu POM
# Home page https://the-internet.herokuapp.com/
# Sa aiba cel putin 3 elemente inlcusiv Form Authentication
# Sa contina metode de click pe ele
# Login page https://the-internet.herokuapp.com/login
# Sa contina user, pass, login_btn si metode pt interactiune cu ele
# Secure page https://the-internet.herokuapp.com/secure
# Sa contina mesajul de succes si verificare ca e displayed
# Sa contina logout_btn si click pe el

class Home_page(Browser):

    FORM_AUTHENTICATION = (By.XPATH, '//a[text()="Form Authentication"]')
    USER_INPUT = (By.XPATH, '//input[@id="username"]')
    PASS_INPUT = (By.XPATH, '//input[@id="password"]')
    FILE_UPLOAD = (By.XPATH, '//a[text()="File Upload"]')
    GEOLOCATION = (By.XPATH, '//a[text()="Geolocation"]')
    def navigate_to_home_page(self):
        self.driver.get('https://the-internet.herokuapp.com')

    def click_form_authentication(self):
        self.driver.find_element(*self.FORM_AUTHENTICATION).click()

    def click_file_upload(self):
        self.driver.find_element(*self.FILE_UPLOAD).click()

    def click_geolocation(self):
        self.driver.find_element(*self.GEOLOCATION).click()






