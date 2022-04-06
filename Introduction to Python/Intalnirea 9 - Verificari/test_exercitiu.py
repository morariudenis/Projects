import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test2(unittest.TestCase):
    # elementele din pagina
    # in loc sa le scriem de n ori in teste, le trecem aici o sg data
    CONTACT_US = (By.XPATH, '//a[text()="Contact us"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submitMessage"]')
    ERROR_MESSAGE = (By.XPATH, '//ol/li')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('http://automationpractice.com/index.php') # url de start
        self.chrome.implicitly_wait(5)
        self.chrome.find_element(*self.CONTACT_US).click() # dam click pe contact us

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'http://automationpractice.com/index.php?controller=contact'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_page_title(self):
        actual = self.chrome.title
        expected = 'Contact us - My Store'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_elem_visible(self):
        self.chrome.find_element(*self.SUBMIT_BUTTON).click()
        elem = self.chrome.find_element(*self.SUBMIT_BUTTON)
        self.assertTrue(elem.is_displayed(), 'Submit btn nu e vizibil')