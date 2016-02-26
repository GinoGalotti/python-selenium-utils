__author__ = 'ginogalotti'

from SeleniumPythonFramework.src.main.Utils.DriverUtils import get_url


class CommonPage(object):
    def __init__(self, driver, env='staging', mobile=False, page_url=""):
        self.driver = driver
        self.env = env
        self.mobile = mobile
        self.page_url = get_url(env, page_url)
