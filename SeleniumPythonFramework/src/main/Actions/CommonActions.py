from SeleniumPythonFramework.src.main.utils.DriverUtils import change_to_new_window


class CommonActions(object):
    def __init__(self, test_context):
        self.test_context = test_context

    def init_page_object(self, PageObject):
        return PageObject(driver=self.test_context.driver, env=self.test_context.stage, mobile=self.test_context.mobile)

    def go_to_url(self, url):
        self.test_context.driver.get(url)

    def change_to_new_window(self, jump=-1):
        change_to_new_window(self.test_context.driver, jump)

    def switch_to_alert(self):
        self.test_context.driver.switch_to_alert()
