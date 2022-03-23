import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Implementati o clasa Login care sa mosteneasca unittest.TestCase
#
# Gasiti elementele in partea de sus folosind ce selectors doriti voi
#

class Test2(unittest.TestCase):
    # elementele din pagina
    # in loc sa le scriem de n ori in teste, le trecem aici o sg data
    FORM_AUTHENTICATION= (By.XPATH, '//a[text()="Form Authentication"]')
    LOGIN_BUTTON = (By.XPATH, '//i')
    LOGOUT_BUTTON = (By.XPATH, '//a[@class="button secondary radius"]')
    H2_BUTTON = (By.XPATH, '//h2')
    ELEM_BUTTON = (By.XPATH, '//a[text()="Elemental Selenium"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@id="flash"]')
    X_BUTTON = (By.XPATH, '//a[@class="close"]')
    LISTA = (By.XPATH, '//label')
    SUCCESS = (By.XPATH, '//div[@class="flash success"]')
# setUp()
# Initializati driver
# Navigati catre https://the-internet.herokuapp.com
# Dati click pe Form Authentication
#
# tearDown()
# Quit browser
#
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com') # url de start
        self.chrome.implicitly_wait(5)
        self.chrome.find_element(*self.FORM_AUTHENTICATION).click() # dam click pe contact us

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.chrome.quit()
# Test1
# Verificati ca noul url e corect
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')
#
# Test2
# Verificati ca page title e corect
#
    def test_page_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')
# Test3
# Verificati textul de pe elementul xpath=//h2 e corect
#
    def test_text_h2(self):
        actual = self.chrome.find_element(*self.H2_BUTTON).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Text is incorrect')
# Test4
# Verificati ca butonul de login este displayed
#
    def test_elem_visible(self):
        elem = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(elem.is_displayed(), 'Login button nu e vizibil')
# Test5
# Verificati ca atributul href al linkului ‘Elemental Selenium’ e corect
#
    def test_elem_atribute(self):
        actual = self.chrome.find_element(*self.ELEM_BUTTON).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'Submit btn href attribute is wrong')
# Test6
# Lasati goale user si pass
# Click login
# Verifica ca eroarea e displayed
#     def test_error_display(self):
#         # verificam ca apare exceptia NoSuchElementException
#         self.chrome.find_element(*self.LOGIN_BUTTON).click()
#         try:
#             self.chrome.find_element(*self.ERROR_MESSAGE)
#         except NoSuchElementException:
#             pass
#
# Test7
# Completeaza cu user si pass invalide
# Click login
# Verifica ca mesajul de pe eroare e corect
#
    def test_error_message(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        print(actual)
        expected = 'Your username is invalid!'
        self.assertEqual(expected, actual, 'Error message is wrong')
# Test8
# Lasati goale user si pass
# Click login
# Apasa x la eroare
# Verifica ca eroarea a disparut
    def test_x(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.X_BUTTON).click()
        try:
            self.chrome.find_element(*self.ERROR_MESSAGE)
        except NoSuchElementException:
            pass

# Test9
# Ia ca o lista toate //label
# Verifica textul ca textul de pe ele sa fie cel asteptat (Username si Password)
# Aici e ok sa avem 2 asserturi

    def test_label(self):
        input_list = self.chrome.find_elements(*self.LISTA)
        actual1 = input_list[0].text
        expected1 = 'Username'
        self.assertEqual(expected1, actual1, 'Error message is wrong')
        actual2 = input_list[1].text
        expected2 = 'Password'
        self.assertEqual(expected2, actual2, 'Error message is wrong')

#
# Test10
# Completeaza cu user si pass valide
# Click login
# Verifica ca noul url CONTINE /secure
# Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
# Verifica ca elementul cu clasa=’flash succes’ este displayed
# Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’
#
    def test_new_url(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(self.chrome, 5).until(EC.url_changes('https://the-internet.herokuapp.com/login'))
        WebDriverWait(self.chrome, 5).until(EC.url_contains('/secure'))
        try:
            WebDriverWait(self.chrome, 5).until(EC.url_contains('/secure'))
        except TimeoutException:
            self.assertTrue(False, 'Am asteptat 5 secunde dar url nu se incarca sau nu e corect')
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((By.ID, 'flash')))
        try:
            WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((By.ID, 'flash')))
        except TimeoutException:
            self.assertTrue(False, 'Am asteptat 5 secunde dar url nu se incarca sau nu e corect')

        # elem = self.chrome.find_element(By.PARTIAL_LINK_TEXT, 'secure area')
        # self.assertTrue(elem.is_displayed(), 'Nu contine')
        # try:
        #     self.chrome.find_element(By.PARTIAL_LINK_TEXT, 'secure area')
        # except NoSuchElementException:
        #     self.assertTrue(False, 'Nu contine')
        cuv = self.chrome.find_element(By.XPATH, '//div[@id="flash"]').text
        if cuv.__contains__('secure area!'):
            print('Textul contine: secure area!')
            # try:
            #     self.chrome.find_element(*self.SUCCESS)
            # except NoSuchElementException:
            #     pass

    # Test11
# Completeaza cu user si pass valide
# Click login
# Click logout
# Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login
#

    def test_page(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        try:
            WebDriverWait(self.chrome, 5).until(EC.url_to_be('https://the-internet.herokuapp.com/login'))
        except TimeoutException:
            self.assertTrue(False, 'Am asteptat 5 secunde dar url nu se incarca sau nu e corect')


# BONUS
# Test12 - brute force password hacking
# Completeaza user tomsmith
# Gaseste elementul //h4 si ia tot textul de pe el
# Ia textu de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola
# Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi pe login
# La final testul trebuie sa imi printeze fie
# 	‘Nu am reusit sa gasesc parola’
# 	‘Parola secreta este [parola]’


    def test_12(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        text = self.chrome.find_element(By.TAG_NAME, 'h4').text
        text = text.split()
        for i in range(len(text)):
            self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
            self.chrome.find_element(By.ID, 'password').send_keys(text[i])
            self.chrome.find_element(*self.LOGIN_BUTTON).click()
            #
            actual = self.chrome.current_url
            expected = 'https://the-internet.herokuapp.com/secure'
            # self.assertEqual(expected, actual, 'parola gresita')
            if actual == expected:
                print(f'parola buna e {text[i]}')
            else:
                print('parola gresita')
            # WebDriverWait(self.chrome, 5).until(EC.url_matches('https://the-internet.herokuapp.com/login'))
        # print(text[1])
        #try:
        #     WebDriverWait(self.chrome, 1).until(EC.url_to_be('https://the-internet.herokuapp.com/login'))
        # except TimeoutException:
        #     self.assertTrue(False, 'Nu am gasit parola')
        #     print(f'Parola e {text[i]}')



