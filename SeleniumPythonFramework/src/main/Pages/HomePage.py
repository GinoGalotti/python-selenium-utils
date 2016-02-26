from selenium.webdriver.common.by import By

from SeleniumPythonFramework.src.main.Pages.CommonPage import CommonPage
from SeleniumPythonFramework.src.main.Utils.DriverUtils import wait_element_to_be_present

# Production locations
TRY_TEXT = {"by": By.ID, "locator": "url-input"}
TRY_BUTTON = {"by": By.ID, "locator": "get-data"}
HOW_IT_WORKS_TRY_BUTTON = {"by": By.XPATH, "locator": "//a[@class='btn btn-sm btn-ghost']"}
LOG_IN_BUTTON = {"by": By.LINK_TEXT, "locator": "Log in"}
SIGN_UP_BUTTON = {"by": By.LINK_TEXT, "locator": "Sign up"}
PRICING_BUTTON = {"by": By.LINK_TEXT, "locator": "Pricing"}
SHOW_EXAMPLES = {"by": By.XPATH, "locator": "//a[@class='cta btn-cta']"}
HIGHLIGHTED_EXAMPLE = {"by": By.XPATH, "locator": "//img[@class='example-img-img']"}

MY_ACCOUNT_BUTTON = {"by": By.XPATH, "locator": "//a/span[@class='button-text']"}

# Stage Locations
MY_ACCOUNT = {"by": By.XPATH, "locator": "//div[@class='split-dropdown-container']/a/span[@class='button-text']"}
LOG_OUT = {"by": By.XPATH,
           "locator": "//body[@id='home']/div[@class='nav-bar']/div[@class='nav-wrapper']/nav[@class='nav-collapsable nav-collapsable-0 closed']/ul/li[@class='button-wrapper split button primary open']/div[@class='split-dropdown-container']/ul/li[3]/a"}

HOME_URL = ""


class HomePage(CommonPage):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(page_url=HOME_URL, **kwargs)

    def try_url_text(self):
        return wait_element_to_be_present(self.driver, TRY_TEXT["by"], TRY_TEXT["locator"])

    def try_url_button(self):
        return wait_element_to_be_present(self.driver, TRY_BUTTON["by"], TRY_BUTTON["locator"])

    def how_it_works_try_button(self):
        return wait_element_to_be_present(self.driver, HOW_IT_WORKS_TRY_BUTTON["by"],
                                          HOW_IT_WORKS_TRY_BUTTON["locator"])

    # Top menu

    def my_account_button(self):
        return wait_element_to_be_present(self.driver, MY_ACCOUNT["by"], MY_ACCOUNT["locator"])

    def log_out_button(self):
        return wait_element_to_be_present(self.driver, LOG_OUT["by"], LOG_OUT["locator"])

    def log_in_button(self):
        return wait_element_to_be_present(self.driver, LOG_IN_BUTTON["by"], LOG_IN_BUTTON["locator"])

    def sign_up_button(self):
        return wait_element_to_be_present(self.driver, SIGN_UP_BUTTON["by"], SIGN_UP_BUTTON["locator"])

    def my_account_button_text(self):
        return wait_element_to_be_present(self.driver, MY_ACCOUNT_BUTTON["by"], MY_ACCOUNT_BUTTON["locator"])

    def pricing_button(self):
        return wait_element_to_be_present(self.driver, PRICING_BUTTON["by"], PRICING_BUTTON["locator"])

    def highlighted_example(self):
        return wait_element_to_be_present(self.driver, HIGHLIGHTED_EXAMPLE["by"], HIGHLIGHTED_EXAMPLE["locator"])

    def show_examples_text(self):
        return wait_element_to_be_present(self.driver, SHOW_EXAMPLES["by"], SHOW_EXAMPLES["locator"])
