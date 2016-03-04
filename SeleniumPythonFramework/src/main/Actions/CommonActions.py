from SeleniumPythonFramework.src.main.utils.driver_utils import change_to_new_window, Wait_for_page_load


class CommonActions(object):
    def __init__(self, test_context):
        self.test_context = test_context
        self.wait_for_page_load = Wait_for_page_load(self.test_context.driver)

    def load_page(self):
        with self.wait_for_page_load:
            self.go_to_url(self.home_page.page_url)

    def init_page_object(self, PageObject):
        return PageObject(driver=self.test_context.driver, env=self.test_context.stage, mobile=self.test_context.mobile)

    def go_to_url(self, url):
        self.test_context.driver.get(url)

    def change_to_new_window(self, jump=-1):
        change_to_new_window(self.test_context.driver, jump)

    def switch_to_alert(self):
        self.test_context.driver.switch_to_alert()
