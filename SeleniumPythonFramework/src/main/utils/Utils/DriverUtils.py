__author__ = 'Gino'

import time
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


small_wait = os.getenv('SELENIUM_SMALL_WAIT', 3)
medium_wait = os.getenv('SELENIUM_MEDIUM_WAIT', 7)
long_wait = os.getenv('SELENIUM_LONG_WAIT', 10)
extra_long_wait = os.getenv('SELENIUM_EXTRA_LONG_WAIT', 14)


class Wait_for_page_load(object):
    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        Utils.wait_for(self.page_has_loaded)


class Utils():
    SMALL_WAIT = float(os.getenv('SELENIUM_SMALL_WAIT', 3))
    MEDIUM_WAIT = float(os.getenv('SELENIUM_MEDIUM_WAIT', 7))
    LONG_WAIT = float(os.getenv('SELENIUM_LONG_WAIT', 11))
    EXTRA_LONG_WAIT = float(os.getenv('SELENIUM_EXTRA_LONG_WAIT', 17))

    # WORK IN PROGRESS
    @staticmethod
    def wait_element_to_be_present(driver, by, locator, timeout=5, multiple_elements=False, retry=True):
        if Utils.element_is_visible(driver, by, locator, timeout):
            if multiple_elements:
                return driver.find_elements(by, locator)
            else:
                return driver.find_element(by, locator)
        else:
            if retry:
                return Utils.wait_element_to_be_present(driver, by, locator, timeout, multiple_elements, retry=False)
            else:
                return False

    @staticmethod
    def element_is_visible(driver, by, locator, timeout):
        try:
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

    @staticmethod
    def element_is_not_visible(driver, by, locator, timeout=8):
        try:
            WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((by, locator)))
            return False
        except TimeoutException:
            return False

    @staticmethod
    def set_window_size_big(driver):
        SIZE_BIG = (1200, 900)
        driver.set_window_size(SIZE_BIG[0], SIZE_BIG[1])

    @staticmethod
    def set_window_size_small(driver):
        SIZE_SMALL = (900, 600)
        driver.set_window_size(SIZE_SMALL[0], SIZE_SMALL[1])

    @staticmethod
    def set_mobile_view(mobile, driver):
        if mobile:
            Utils.set_window_size_small(driver)
        else:
            Utils.set_window_size_big(driver)

    @staticmethod
    def wait_for(condition_function):
        start_time = time.time()
        while time.time() < start_time + 14:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception('Timeout waiting for {}'.format(condition_function.__name__)
                        )

    @staticmethod
    def get_url(stage, url):
        stage_url = (Utils.get_stage_url(stage) + url)
        print("getting url ", stage_url)
        return stage_url

    @staticmethod
    def get_stage_url(stage):
        PRODUCTION_ENV = "http://import.io/"
        STAGE_ENV = "https://staging-owl.com/"

        if (stage == "production"):
            return PRODUCTION_ENV
        if (stage == "staging"):
            return STAGE_ENV

    @staticmethod
    def scroll_down_til_the_end(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    @staticmethod
    def change_to_new_window(mobile, driver, jump=-1):
        driver.switch_to_window(driver.window_handles[jump])
        # Utils.set_mobile_view(mobile, driver)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    @staticmethod
    def wait_for_alert(driver, alert_message='Time our waiting for alert', maximum_wait=3):
        # WebDriverWait(driver, maximum_wait).until(EC.alert_is_present(), alert_message)
        Utils.wait_for(EC.alert_is_present())

    @staticmethod
    def is_safari(driver):
        return driver.name.lower() == 'safari'