from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then


@when('Allow notification')
def allow_notification(context):
    context.driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
    