from pages.login_page import LoginPage
from pages.forgot_password_page import Forgot_password_page
from pages.sign_in_page import Sign_in_page
from pages.home_page import Home_page
from pages.secure_page import Secure_page
from browser import Browser

def before_all(context):

    context.browser = Browser()
    context.login_page = LoginPage()
    context.forgot_password_page = Forgot_password_page()
    context.home_page = Home_page()
    context.sign_in_page = Sign_in_page()
    context.secure_page = Secure_page()

def after_all(context):
    context.browser.close()

    # contextul este o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
    # before all = BDD
    # after all = BDD
    # de fiecare data cand adaugam o noua pagina in proiect o vom adauga in context