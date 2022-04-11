from behave import *


# given!, when!, and, but, then! - sintaxa gherkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificarea din test

@given('sign in: I am a user on jules sing in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()


@when('sign in: I set my email "(email)"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)


@when('sing in: I set my pass ("password")')
def step_impl(context, password):
    context.sign_in_page.set_pass(password)


@when('sing in: I click login button')
def step_impl(context):
    context.sign_in_page.click_login_btn()


@when('sing in: I click forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_pswd_link()
