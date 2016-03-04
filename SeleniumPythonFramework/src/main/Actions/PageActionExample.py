from SeleniumPythonFramework.src.main.Utils.DriverUtils import Wait_for_page_load, sleep_small, sleep_medium, \
    sleep_long

from CommonActions import CommonActions
from SeleniumPythonFramework.src.main.Pages.HomePage import HomePage

__author__ = 'Gino'

MY_ACCOUNT_TEXT = "My Account"


class HomePageActions(CommonActions):
    def __init__(self, **kwargs):
        super(HomePageActions, self).__init__(**kwargs)
        self.home_page = self.init_page_object(HomePage)

    def click_log_in(self):
        with self.wait_for_page_load:
            self.home_page.log_in_button().click()
            self.change_to_new_window()

    def click_sign_up(self):
        with self.wait_for_page_load:
            self.home_page.sign_up_button().click()
            self.change_to_new_window()

    def click_pricing(self):
        with self.wait_for_page_load:
            self.home_page.pricing_button().click()

    def click_show_examples(self):
        self.home_page.how_it_works_try_button().click()
        self.switch_to_alert()
        sleep_small()
        self.home_page.show_examples_text().click()
        # self.change_to_new_window()
        sleep_medium()

    def click_highlighted_example(self):
        self.home_page.highlighted_example().click()
        self.change_to_new_window()
        sleep_long()

    def try_url(self, URL):
        self.home_page.try_url_text().send_keys(URL)
        self.home_page.try_url_button().click()
        self.change_to_new_window()
        sleep_medium()

    def is_account_logged(self):
        return self.home_page.my_account_button_text() == MY_ACCOUNT_TEXT

    def go_settings(self):
        self.home_page.my_account_button().click()
        with Wait_for_page_load(self.test_context.driver):
            self.home_page.log_out_button().click()

    def log_out(self):
        self.home_page.my_account_button().click()
        with self.wait_for_page_load:
            self.home_page.log_out_button().click()
        self.test_context.logged_account = None
