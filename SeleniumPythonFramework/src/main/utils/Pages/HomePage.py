__author__ = 'ginogalotti'

from selenium.webdriver.common.by import By

from SeleniumPythonFramework.src.main.utils.Utils.DriverUtils import Utils


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


class HomePage():
    HOME_URL = ""

    @staticmethod
    def try_url_text(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, TRY_TEXT["by"], TRY_TEXT["locator"])

    @staticmethod
    def try_url_button(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, TRY_BUTTON["by"], TRY_BUTTON["locator"])

    @staticmethod
    def how_it_works_try_button(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, HOW_IT_WORKS_TRY_BUTTON["by"],
                                                HOW_IT_WORKS_TRY_BUTTON["locator"])

    # Top menu
    @staticmethod
    def my_account_button(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, MY_ACCOUNT["by"], MY_ACCOUNT["locator"])

    @staticmethod
    def log_out_button(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, LOG_OUT["by"], LOG_OUT["locator"])

    @staticmethod
    def log_in_button(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, LOG_IN_BUTTON["by"], LOG_IN_BUTTON["locator"])

    @staticmethod
    def sign_up_button(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, SIGN_UP_BUTTON["by"], SIGN_UP_BUTTON["locator"])

    @staticmethod
    def my_account_button_text(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, MY_ACCOUNT_BUTTON["by"], MY_ACCOUNT_BUTTON["locator"])

    @staticmethod
    def pricing_button(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, PRICING_BUTTON["by"], PRICING_BUTTON["locator"])

    @staticmethod
    def highlighted_example(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, HIGHLIGHTED_EXAMPLE["by"], HIGHLIGHTED_EXAMPLE["locator"])

    @staticmethod
    def show_examples_text(driver, env="staging", mobile=False):
        return Utils.wait_element_to_be_present(driver, SHOW_EXAMPLES["by"], SHOW_EXAMPLES["locator"])