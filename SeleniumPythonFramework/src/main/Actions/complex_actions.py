from SeleniumPythonFramework.src.main.Pages.lightning_home_page import LightningHomePage
from SeleniumPythonFramework.src.main.Pages.lightning_page import LightningPage
from SeleniumPythonFramework.src.main.Utils.driver_utils import Wait_for_page_load
from SeleniumPythonFramework.src.main.Utils.driver_utils import change_to_new_window, wait_for_element_to_be_present

__author__ = 'Gino'


# This helps us as an utils, doing complex and repetitive actions
class ComplexActions():
    def __init__(self, context, **kwargs):
        self.driver = context.driver
        self.page_builder = context.page_builder
        self.wait_for_page_load = Wait_for_page_load(self.driver)

    def change_to_new_window(self, jump=-1):
        change_to_new_window(self.driver, jump)

    def switch_to_alert(self):
        self.driver.switch_to_alert()

    def try_url_and_wait_for_load(self, url):
        lightning_home_page = self.page_builder.get_page(LightningHomePage)
        lightning_page = self.page_builder.get_page(LightningPage)
        lightning_home_page.load_page()
        lightning_home_page.try_url(url)
        wait_for_element_to_be_present(self.driver, lightning_page.element_when_i_am_ready())
