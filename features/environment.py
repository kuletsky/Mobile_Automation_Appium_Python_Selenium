from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait

from time import sleep


def mobile_driver_init(context, scenario_name):
    """
    :param context: Behave context
    """

    desired_capabilities = {
        "platformName": "Android",
        "automationName": "uiautomator2",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "appActivity": "com.hotake.hotake.MainActivity",
        "appPackage": "com.stunt.dev.application",
        "app": "/home/costa/code/QA/Projects/Mobile_Automation_Appium_Python_Selenium/mobile_app/app-dev-release.apk"
    }

    appium_server_url = 'http://127.0.0.1:4723'
    capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

    context.driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    context.driver.implicitly_wait(6)
    context.wait = WebDriverWait(context.driver, 10)

    # context.app = 
