from appium.webdriver.common.appiumby import AppiumBy
from behave import when, then

from time import sleep

BTN_ALLOW = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
BTN_GET_STARTED = (AppiumBy.XPATH, '//android.view.View[@content-desc="Get Started"]')
BTN_NEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="Next"]')
INPUT_FIELD = (AppiumBy.XPATH, '//android.widget.EditText')
TAG_ROOM = (AppiumBy.XPATH, '//android.view.View[@content-desc="Rooms"]')


@when('Click Allow notification button')
def login(context):
    context.driver.find_element(*BTN_ALLOW).click()


@when('Click Get Started button')
def get_started(context):
    context.driver.find_element(*BTN_GET_STARTED).click()


@when('Put the phone number')
def put_phone_number(context):
    context.driver.find_element(*INPUT_FIELD).click()
    context.driver.find_element(*INPUT_FIELD).send_keys('2199234500')


@when('Click Next button')
def next_button(context):
    context.driver.find_element(*BTN_NEXT).click()
    sleep(6)


@when('Put the code')
def put_the_code(context):
    context.driver.find_element(*INPUT_FIELD).click()
    context.driver.find_element(*INPUT_FIELD).send_keys('111111')


@then('Verify success login')
def verify_login(context):
    context.driver.find_element(*TAG_ROOM)
    # print(actual_result)
