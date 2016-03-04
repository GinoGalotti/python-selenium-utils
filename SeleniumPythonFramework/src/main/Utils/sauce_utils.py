__author__ = 'Gino'

import sys

from sauceclient import SauceClient


class SauceUtils(object):
    SAUCE_URL = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"

    def __init__(self, user, password, tool):
        self.is_sauce = (tool and tool.lower() == 'sauce')
        if self.is_sauce:
            self.user = user
            self.password = password
            self.sauce_client = SauceClient(user, password)

    def get_command_url(self):
        url = self.SAUCE_URL % (self.user, self.password)
        return url

    def update_build_name(self, session_id, build):
        if self.is_sauce:
            self.sauce_client.jobs.update_job(session_id, build_num=build)

    def update_job_name(self, session_id, name, tag=None):
        if self.is_sauce:
            self.sauce_client.jobs.update_job(session_id, name=name)
            if tag:
                self.sauce_client.jobs.update_job(session_id, tags=tag)

    def update_job_status(self, session_id):
        if self.is_sauce:
            status = sys.exc_info() == (None, None, None)
            self.sauce_client.jobs.update_job(session_id, passed=status)

    def check_using_tool(self):
        return self.is_sauce

    @staticmethod
    def add_extra_desired_capabilities(desired_cap, env_variables):
        desired_cap['screenResolution'] = env_variables['default_resolution']
        desired_cap['videoUploadOnPass'] = env_variables['video_upload_on_pass']
        desired_cap['commandTimeout'] = env_variables['command_timeout']
        return desired_cap
