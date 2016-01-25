from SeleniumPythonFramework.src.main.utils.Pages.HomePage import HomePage
from SeleniumPythonFramework.src.main.utils.Utils.DriverUtils import Wait_for_page_load
from SeleniumPythonFramework.src.main.utils.Utils.DriverUtils import Utils
from SeleniumPythonFramework.src.main.utils.Pages.LogIn.LogInPage import LogInPage
from SeleniumPythonFramework.src.main.utils.Pages.LogIn.SignUpPage import SignUpPage

__author__ = 'Gino'

MY_ACCOUNT_TEXT = "My Account"
STAGING_USER = "***"
STAGING_PASS = "***"


class HomePageActions(object):
    def __init__(self, testContext):
        self.test_context = testContext

    # TODO Fix with the new auth
    def load_home(self):
        self.test_context.driver.get(Utils.get_url(self.test_context.stage, HomePage.HOME_URL))
        print('cant load home')

    def click_log_in(self):
        with Wait_for_page_load(self.test_context.driver):
            HomePage.log_in_button(self.test_context.driver, self.test_context.stage).click()

    def click_sign_up(self):
        with Wait_for_page_load(self.test_context.driver):
            HomePage.sign_up_button(self.test_context.driver, self.test_context.stage).click()

    def click_pricing(self):
        with Wait_for_page_load(self.test_context.driver):
            HomePage.pricing_button(self.test_context.driver, self.test_context.stage).click()

    def click_show_examples(self):
        HomePage.how_it_works_try_button(self.test_context.driver, self.test_context.stage).click()
        self.test_context.driver.switch_to_alert()
        Utils.sleep(Utils.SMALL_WAIT)
        HomePage.show_examples_text(self.test_context.driver, self.test_context.stage).click()
        Utils.sleep(Utils.MEDIUM_WAIT)

    def click_highlighted_example(self):
        HomePage.highlighted_example(self.test_context.driver, self.test_context.stage).click()
        Utils.change_to_new_window(self.test_context.mobile, self.test_context.driver)
        Utils.sleep(Utils.LONG_WAIT)

    def try_url(self, URL):
        HomePage.try_url_text(self.test_context.driver, self.test_context.stage).send_keys(URL)
        HomePage.try_url_button(self.test_context.driver, self.test_context.stage).click()
        Utils.change_to_new_window(self.test_context.mobile, self.test_context.driver)
        Utils.sleep(Utils.MEDIUM_WAIT)

    def is_account_logged(self):
        return HomePage.my_account_button_text(self.test_context.driver, self.test_context.stage) == MY_ACCOUNT_TEXT

    def log_out(self):
        HomePage.my_account_button(self.test_context.driver, self.test_context.stage).click()
        with Wait_for_page_load(self.test_context.driver):
            HomePage.log_out_button(self.test_context.driver).click()
        self.test_context.logged_account = None
