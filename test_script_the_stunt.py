from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from time import sleep

# test conect
desired_capabilities = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "platformVersion": "13",
    "deviceName": "emulator-5554",
    "appActivity": "com.hotake.hotake.MainActivity",
    "appPackage": "com.stunt.dev.application",
    "app": "/home/costa/code/QA/Projects/Mobile_Automation_Appium_Python_Selenium/mobile_app/app-dev-release.apk"
    }

appium_server_url = 'http://127.0.0.1:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)
# driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
sleep(20)
