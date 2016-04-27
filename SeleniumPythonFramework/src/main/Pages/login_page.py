from selenium.webdriver.common.by import By

from SeleniumPythonFramework.src.main.Pages.common_page import CommonPage

__author__ = 'Gino'

# Production locations
EMAIL_FIELD = {"by": By.NAME, "locator": "username"}
PASSWORD_FIELD = {"by": By.NAME, "locator": "password"}
LOGIN_BUTTON = {"by": By.CSS_SELECTOR, "locator": ".btn-default"}

PATH = "/login"


class LogInPage(CommonPage):
    def __init__(self, **kwargs):
        super(LogInPage, self).__init__(page_url=PATH, **kwargs)

    def email_field(self):
        return self.get_element(EMAIL_FIELD)

    def password_field(self):
        return self.get_element(PASSWORD_FIELD)

    def login_button(self):
        return self.get_element(LOGIN_BUTTON)

    def login_account(self, user, password):
        self.email_field().send_keys(user)
        self.password_field().send_keys(password)

        with self.wait_for_page_load:
            self.login_button().click()
