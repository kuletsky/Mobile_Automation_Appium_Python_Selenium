from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from time import sleep

# test wikipedia
desired_capabilities = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "platformVersion": "11",
    "deviceName": "Android Emulator",
    "appActivity": "org.wikipedia.main.MainActivity",
    "appPackage": "org.wikipedia",
    "app": "/home/costa/code/QA/Projects/Mobile_Automation_Appium_Python_Selenium/mobile_app/org.wikipedia.apk"
}

appium_server_url = 'http://127.0.0.1:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(50)

# click Skip onboarding
driver.find_element(AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()

# click on Search icon
# driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Search Wikipedia"]').click()

# search input
# driver.find_element().send_keys('')