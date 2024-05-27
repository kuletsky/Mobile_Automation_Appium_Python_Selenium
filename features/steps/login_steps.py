from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then

from time import sleep


@when('Click Allow notification button')
def login(context):
    context.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()


@when('Click Get Started button')
def get_started(context):
    context.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Get Started"]').click()


@when('Put the phone number')
def put_phone_number(context):
    context.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').click()
    context.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('2199234500')


@when('Click Next button')
def next_button(context):
    context.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Next"]').click()
    sleep(4)


@when('Put the code')
def put_the_code(context):
    context.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').click()
    context.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('111111')


@then('Verify success login')
def verify_login(context):
    context.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Rooms"]')
    # print(actual_result)
