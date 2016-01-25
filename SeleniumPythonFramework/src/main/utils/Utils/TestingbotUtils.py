__author__ = 'ginogalotti'

import sys

from testingbotclient import TestingBotClient


class TestingbotUtils(object):
    TESTINGBOT_URL = "http://%s:%s@hub.testingbot.com:4444/wd/hub"

    def __init__(self, user, password, tool):
        self.is_testingbot = (tool and tool.lower() == 'testingbot')
        if self.is_testingbot:
            self.user = user
            self.password = password
            self.testingbot_client = TestingBotClient(user, password)

    def get_command_url(self):
        url = self.TESTINGBOT_URL % (self.user, self.password)
        return url

    def update_build_name(self, session_id, build):
        return
        # Is there any way to set the build number?
        # if self.is_testingbot:
        # self.testingbot_client.tests.update_test(session_id, build_num=build)

    def update_job_name(self, session_id, name, tag=None):
        if self.is_testingbot:
            # This way allow us to use the same methods as Saucelabs
            self.testing_method_name = name

    def update_job_status(self, session_id):
        if self.is_testingbot:
            status = sys.exc_info() == (None, None, None)
            self.testingbot_client.tests.update_test(session_id, name=self.testing_method_name, passed=status)

    def check_using_tool(self):
        return self.is_testingbot

    @staticmethod
    def add_extra_desired_capabilities(desired_cap, env_variables):
        # Nothing to add
        desired_cap['screen-resolution'] = env_variables['default_resolution']
        if env_variables['build']:
            desired_cap["build"] = env_variables["build"]
        return desired_cap