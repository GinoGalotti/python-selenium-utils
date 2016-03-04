import os
import threading
import unittest

from selenium import webdriver

from SeleniumPythonFramework.src.main.Actions.PageActionExample import HomePageActions
from SeleniumPythonFramework.src.main.Utils.common import environment_variables
from SeleniumPythonFramework.src.main.Utils.common_steps import on_platforms
from SeleniumPythonFramework.src.main.Utils.constants import TestingConstants
from SeleniumPythonFramework.src.main.Utils.driver_utils import set_mobile_view
from SeleniumPythonFramework.src.main.Utils.sauce_utils import SauceUtils
from SeleniumPythonFramework.src.main.Utils.testingbot_utils import TestingbotUtils
from SeleniumPythonFramework.src.main.Utils.world_context import WorldContext

sauce_utils = SauceUtils(environment_variables['sauce_user'], environment_variables['sauce_pass'],
                         environment_variables['tool'])
testingbot_utils = TestingbotUtils(environment_variables['testingbot_user'], environment_variables['testingbot_pass'],
                                   environment_variables['tool'])


@on_platforms(environment_variables['browser'])
class TestSmoke(unittest.TestCase):
    def setUp(self):

        if testingbot_utils.check_using_tool():
            self.tools_utils = testingbot_utils
            self.desired_capabilities = TestingbotUtils.add_extra_desired_capabilities(self.desired_capabilities,
                                                                                       environment_variables)
            driver = webdriver.Remote(
                command_executor=testingbot_utils.get_command_url(),
                desired_capabilities=self.desired_capabilities)

        elif sauce_utils.check_using_tool():
            # This values can't not be defined with Saucelab plugin
            self.tools_utils = sauce_utils
            self.desired_capabilities = SauceUtils.add_extra_desired_capabilities(self.desired_capabilities,
                                                                                  environment_variables)
            driver = webdriver.Remote(
                command_executor=sauce_utils.get_command_url(),
                desired_capabilities=self.desired_capabilities)
            if environment_variables['build']:
                self.tools_utils.update_build_name(self.test_context.driver.session_id, environment_variables['build'])

        else:
            driver = webdriver.Chrome(executable_path=os.path.realpath(environment_variables['chromedriver_local']))
            self.tools_utils = sauce_utils
            # driver = webdriver.PhantomJS()

        driver.implicitly_wait(15)

        # Needing for some concurrent testing?
        self.test_context = threading.local()
        self.test_context = WorldContext(driver, environment_variables['env'], environment_variables['mobile'])
        set_mobile_view(self.test_context.mobile, self.test_context.driver)

    # MAGIC TESTING
    # This have to adapt to the new webpage when present
    def test_try_out_magic_from_homepage(self):
        self.tools_utils.update_job_name(self.test_context.driver.session_id, self._testMethodName, ["magic"])

        # And we are in HOME
        home_page_actions = HomePageActions(test_context=self.test_context)
        home_page_actions.load_home()

        # When we write an url and click try it out
        home_page_actions.try_url(TestingConstants.MAGIC_TRY_OUT_URL_EXAMPLE["url"])

        # Then magic page is shown
        self.assertIn(TestingConstants.EXPECTED_URL_MAGIC, self.test_context.driver.current_url,
                      "magic url should be part " + TestingConstants.EXPECTED_URL_MAGIC)
        print("we are inside magic")

        # And the search is part of the URL
        self.assertIn(TestingConstants.MAGIC_TRY_OUT_URL_EXAMPLE["url_part"], self.test_context.driver.current_url,
                      "url should contain " + TestingConstants.MAGIC_TRY_OUT_URL_EXAMPLE["url_part"])

    def tearDown(self):
        self.test_context.driver.quit()
        self.tools_utils.update_job_status(self.test_context.driver.session_id)


if __name__ == "__main__":
    unittest.main()
