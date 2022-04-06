import unittest
import HtmlTestRunner

from Tema_9 import Test3
from test3_alerts import Alerts
from test4_auth import Authentication
from test5_context_menu import ContextMenu
from test6_keys import Keyboard

class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test',
            report_name='Smoke Test Result'
        )

        runner.run(smoke_test)



'''
TEST1:
Verificati ca noul url e corect:
GIVEN: I am on heroku home page
WHEN: I click Login Button 
Then: I land on correct page: https://the-internet.herokuapp.com/login
'''

'''
TEST2:

GIVEN: I am on heroku home page
WHEN: I click on the form page
THEN: I verify that the page title is "....."
'''

'''
TEST3:

GIVEN: I am on heroku home page
WHEN: I click on the login button
THEN: I verify that the text on the element is correct

'''

'''
TEST4:

GIVEN: I am on heroku home page
WHEN: I click on the login button
THEN: I verify if Login Button is displayed
'''

'''
TEST5:

GIVEN: I am on heroku home page
WHEN: I click on the Elemental Selenium
THEN: I verify if link is correct

'''

'''
TEST6:

GIVEN: I am on heroku home page
WHEN: I click on the Login Button
THEN: I verify if error message is displayed

'''

'''
TEST7:

GIVEN: I am on heroku home page
WHEN: I click on the Login Button
THEN: I verify if error message displayed is correct: 'Your username is invalid!'
'''

'''
TEST8:

GIVEN: I am on heroku home page
WHEN: I click on the Login Button
THEN: I click X on the error message
THEN: I check if error disappeared 
'''

'''

TEST9:
Given: I am on 'https://the-internet.herokuapp.com/login' page
Then: I verify that the label is Username for the Username section
Then: I verify that the label is Password for the Password section
'''

'''

Test10
Given: I am on 'https://the-internet.herokuapp.com/login' page
When: I send keys "tomsmith" for username
And: I send keys "SuperSecretPassword!" for password
And: I click on LogIn button
And: I verify that the new URL contains "/secure"
And: I verify that the success message is displayed 
Then: I verify that the success message contains "Secure area!"

'''

'''
Test11

Given: I am on 'https://the-internet.herokuapp.com/login' page
When: I send keys "tomsmith" for username
And: I send keys "SuperSecretPassword!" for password
And: I click on LogIn button
And: I click on LogOut button
Then: I check if the new url is "https://the-internet.herokuapp.com/login"
'''