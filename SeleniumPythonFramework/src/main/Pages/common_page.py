__author__ = 'Gino'

from SeleniumPythonFramework.src.main.Utils.driver_utils import Wait_for_page_load
from SeleniumPythonFramework.src.main.Utils.driver_utils import get_element_when_ready
from SeleniumPythonFramework.src.main.Utils.driver_utils import get_url


class CommonPage(object):
    def __init__(self, driver, env='staging', mobile=False, page_url=''):
        self.driver = driver
        self.env = env
        self.mobile = mobile
        self.page_url = get_url(page_url)

        self.wait_for_page_load = Wait_for_page_load(self.driver)

    def load_page(self):
        with self.wait_for_page_load:
            self.driver.get(self.page_url)

    def init_page_object(self, PageObject):
        return PageObject(driver=self.driver, env=self.env, mobile=self.mobile)

    def get_element(self, object, multiple=False):
        return get_element_when_ready(self.driver, object['by'], object['locator'], multiple_elements=multiple)
