from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from log_files.logger import logger

from app.apllication import Application
from time import sleep


def mobile_driver_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ### BROWSERSTACK ###
    bs_user = 'kuletsky_D18EAl'
    bs_key = 'cjrUnYqkUDR8xPwnqxXj'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        # 'os': 'OS X',
        # 'osVersion': 'Monterey',
        'deviceName': 'Pixel 7',
        "realMobile": "true",
        'browserName': 'Chrome',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    ### ANDROID STUDIO EMULATOR SDK ###
    # desired_capabilities = {
    #     "platformName": "Android",
    #     "automationName": "uiautomator2",
    #     "platformVersion": "13",
    #     "deviceName": "Android Emulator",
    #     "appActivity": "com.hotake.hotake.MainActivity",
    #     "appPackage": "com.stunt.dev.application",
    #     "app": "/home/costa/code/QA/Projects/Mobile_Automation_Appium_Python_Selenium/mobile_app/app-dev-release.apk"
    # }
    #
    # appium_server_url = 'http://127.0.0.1:4723'
    # capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
    # context.driver = webdriver.Remote(appium_server_url, options=capabilities_options)

    # wait parameters
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('Started scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    mobile_driver_init(context, scenario.name)


def before_step(context, step):
    print('Started step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed: {step}')
        context.driver.save_screenshot(f'step_failed_screens/{step}.png')
        print('Step failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
