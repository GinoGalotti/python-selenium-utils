import os
import json
import requests
import threading

from selenium import webdriver
from SeleniumPythonFramework.src.main.Utils.common import environment_variables
from SeleniumPythonFramework.src.main.Utils.driver_utils import pick_window_size, PageBuilder

# This is needed to deal with Compatibility tools
# from UI.SeleniumPythonFramework.src.main.utils.testingbot_utils import TestingbotUtils


# testingbot_utils = TestingbotUtils(env_variables['testingbot_user'], env_variables['testingbot_pass'],
#                                    env_variables['tool'])


def before_all(context):
    context.env = environment_variables['env']
    print("using config for the environment:- {}".format(environment_variables['env']))

    with open('users.json') as f:
        context.users = json.load(f)[context.env]

def before_scenario(context, scenario):
    # if testingbot_utils.check_using_tool():
        #     context.tools_utils = testingbot_utils
        #     desired_capabilities = TestingbotUtils.add_extra_desired_capabilities(env_variables_dict['browser'])

        #     driver = webdriver.Remote(
        #         command_executor=testingbot_utils.get_command_url(),
        #         desired_capabilities=desired_capabilities)
        # context.tools_utils.update_job_name(self.test_context.driver.session_id, self._testMethodName, ["login"])
        # else:

    # setup context for steps
    driver = webdriver.Chrome(executable_path=os.path.realpath(environment_variables['chromedriver_local']))

    driver.implicitly_wait(15)

    # Needed for some concurrent testing?
    context.driver = driver
    context.is_mobile = environment_variables['mobile']
    context.page_builder = PageBuilder(context)

    pick_window_size(context.is_mobile, context.driver)

def after_scenario(context, scenario):
    # tidy up and pubnub channel subscription
    context.driver.quit()

