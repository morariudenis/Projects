from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
#chrome.get('https://formy-project.herokuapp.com/keypress')
#chrome.get('https://formy-project.herokuapp.com/')
#chrome.get('https://www.phptravels.net/')
chrome.get('https://formy-project.herokuapp.com/checkbox')
#chrome.find_element(By.ID, 'contact-link').click()

#chrome.find_element(By.ID, 'name').send_keys('Denis moRARIU')

#chrome.find_element(By.LINK_TEXT, 'submit_search').click()

#chrome.find_element(By.LINK_TEXT, 'Best Sellers').click()

#chrome.find_element(By.PARTIAL_LINK_TEXT, 'Page').click()

# input_list = chrome.find_elements(By.TAG_NAME, 'input')
# input_list[23].send_keys('ksadmcdak@jfna.com')

# chrome.find_element(By.XPATH, "//input[@id='checkout']").send_keys('25')

#chrome.find_element(By.XPATH, "//input[@id='checkbox-2']").click()


# # selector by Class - ia primul tot tp. - e ok doar daca avem clasa unica
# chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Andy')
#
# # gasim mai multe si punem in lista
# chrome.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys('Sinpetrean')


sleep(8)
chrome.quit()
