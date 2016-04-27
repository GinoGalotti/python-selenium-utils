__author__ = 'Gino'

import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import domain

# Parametrizing the sleep allow me to set run "more defensive" tests when I don' care about speed
SMALL_WAIT = float(os.getenv('SELENIUM_SMALL_WAIT', 2))
MEDIUM_WAIT = float(os.getenv('SELENIUM_MEDIUM_WAIT', 4))
LONG_WAIT = float(os.getenv('SELENIUM_LONG_WAIT', 7))
EXTRA_LONG_WAIT = float(os.getenv('SELENIUM_EXTRA_LONG_WAIT', 11))


class Wait_for_page_load(object):
    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        wait_for(self.page_has_loaded)

class PageBuilder(object):
    def __init__(self, context):
        self.driver = context.driver
        self.env = context.env
        self.mobile = context.is_mobile

    def get_page(self, page_object):
        return page_object(driver=self.driver, env=self.env, mobile=self.mobile)

def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 14:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception('Timeout waiting for {}'.format(condition_function.__name__))


def wait_for_condition_to_be_bigger(condition_function, number):
    start_time = time.time()
    while time.time() < start_time + 14:
        if condition_function() > number:
            return True
        else:
            time.sleep(0.1)
    raise Exception('Timeout waiting for {}'.format(condition_function.__name__))


def wait_for_element_to_be_present(driver, element, timeout=20):
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((element['by'], element['locator']))
    )


# WORK IN PROGRESS

def get_element_when_ready(driver, by, locator, timeout=5, multiple_elements=False, retry=True):
    if element_is_visible(driver, by, locator, timeout):
        if multiple_elements:
            return driver.find_elements(by, locator)
        else:
            return driver.find_element(by, locator)
    else:
        if retry:
            return get_element_when_ready(driver, by, locator, timeout, multiple_elements, retry=False)
        else:
            return False


def element_is_visible(driver, by, locator, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
        return True
    except TimeoutException:
        return False


def element_is_not_visible(driver, by, locator, timeout=8):
    try:
        WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((by, locator)))
        return False
    except TimeoutException:
        return False


def set_window_size_big(driver):
    SIZE_BIG = (1200, 900)
    driver.set_window_size(SIZE_BIG[0], SIZE_BIG[1])


def set_window_size_small(driver):
    SIZE_SMALL = (900, 600)
    driver.set_window_size(SIZE_SMALL[0], SIZE_SMALL[1])


def pick_window_size(mobile, driver):
    if mobile:
        set_window_size_small(driver)
    else:
        set_window_size_big(driver)


def get_url(url):
    stage_url = (get_domain() + url)
    return stage_url


def get_feeds_url(url):
    stage_url = (get_domain(prefix="feeds.") + url)
    return stage_url


def get_lightning_url(url):
    stage_url = (get_domain(prefix="lightning.") + url)
    stage_url = stage_url.replace("https", "http")  # Otherwise it gets redirected
    return stage_url


def get_dashboard_url(url):
    stage_url = (get_domain(prefix="dash.") + url)
    return stage_url


def get_api_url(url):
    stage_url = (get_domain(prefix="api.") + url)
    return stage_url


def get_domain(prefix=""):
    return "https://{0}{1}".format(prefix, domain)


def scroll_down_til_the_end(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def change_to_new_window(driver, jump=-1):
    driver.switch_to_window(driver.window_handles[jump])


def sleep(seconds):
    time.sleep(seconds)


def sleep_small():
    time.sleep(SMALL_WAIT)


def sleep_medium():
    time.sleep(MEDIUM_WAIT)


def sleep_long():
    time.sleep(LONG_WAIT)


def sleep_extra_long():
    time.sleep(EXTRA_LONG_WAIT)


def wait_for_alert(driver, alert_message='Time our waiting for alert', maximum_wait=3):
    # WebDriverWait(driver, maximum_wait).until(EC.alert_is_present(), alert_message)
    wait_for(EC.alert_is_present())


def is_safari(driver):
    return driver.name.lower() == 'safari'
