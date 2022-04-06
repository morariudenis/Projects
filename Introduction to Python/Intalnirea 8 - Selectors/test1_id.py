# cel mai usor mod de a gasit elemente este rpooin id pt ca sunt unice

# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
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
chrome.get('https://formy-project.herokuapp.com/form')

# selector by ID
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Denis')

last_name = chrome.find_element(By.ID, 'last-name')
last_name.send_keys('Morariu')

job_title = chrome.find_element(By.ID, 'job-title')
job_title.send_keys('Automatic Tester')

sleep(5)
chrome.quit()