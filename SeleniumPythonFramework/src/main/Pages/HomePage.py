from selenium.webdriver.common.by import By

from SeleniumPythonFramework.src.main.Pages.CommonPage import CommonPage

# Production locations
TRY_TEXT = {"by": By.ID, "locator": "url-input"}
TRY_BUTTON = {"by": By.ID, "locator": "get-data"}

PATH = ""


class HomePage(CommonPage):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(page_url=PATH, **kwargs)

    def try_url_text(self):
        return self.get_element(TRY_TEXT)

    def try_url_button(self):
        return self.get_element(TRY_BUTTON)

    def try_url(self, url):
        self.try_url_text().send_keys(url)
        try_button = self.try_url_button()
        with self.wait_for_page_load:
            try_button.click()
