__author__ = 'ginogalotti'

import sys
import os
import ast

from Constants import FrameworkConstants


SAUCE_URL = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"


def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = type(name, (base_class,), d)

    return decorator


# This should be an enum at Python 3.4
def get_environment_variables():
    desired_cap_default = "[ {'platform': 'WIN7', 'browserName': 'firefox', 'version': '24' }, {'platform': 'MAVERICKS', 'browserName': 'chrome', 'version': '46' }]"

    # Params defined on ENV variables
    env_variables_dict = dict()
    env_variables_dict['sauce_user'] = os.getenv('SAUCE_USER_NAME', "qaimport")
    env_variables_dict['sauce_pass'] = os.getenv('SAUCE_API_KEY', "5e913b11-3c04-4c65-916d-1d8cac30caa4")
    env_variables_dict['tool'] = os.getenv('TESTING_TOOL', None)
    env_variables_dict['chromedriver_local'] = FrameworkConstants.MAC_CHROMEDRIVER_PATH
    if env_variables_dict['tool'] and env_variables_dict['tool'].lower() == "docker":
        env_variables_dict['chromedriver_local'] = FrameworkConstants.LINUX_CHROMEDRIVER_PATH
    env_variables_dict['browser'] = get_browsers(os.getenv('TESTING_BROWSERS', desired_cap_default),
                                                 env_variables_dict['tool'])
    env_variables_dict['mobile'] = get_bool(os.getenv('TESTING_MOBILE', 'False'))
    env_variables_dict['build'] = os.getenv('BUILD_ID', None)
    env_variables_dict['project'] = os.getenv('TESTING_PROJECT_NAME', 'import.io')
    env_variables_dict['env'] = os.getenv('TESTING_ENV', 'staging')
    env_variables_dict['default_resolution'] = os.getenv('SELENIUM_SCREEN_RESOLUTION', "1600x1200")
    env_variables_dict['video_upload_on_pass'] = get_bool(os.getenv('SELENIUM_VIDEO_UPLOAD_PASS', 'False'))
    env_variables_dict['command_timeout'] = os.getenv('SAUCE_COMMAND_TIMEOUT', 120)
    env_variables_dict['testingbot_user'] = os.getenv('TESTINGBOT_NAME', "2676672c2da58b2119c44405507723d2")
    env_variables_dict['testingbot_pass'] = os.getenv('TESTINGBOT_API', "b0d46c605cd4ae4a9be3f9de3ac1074d")

    return env_variables_dict


def get_browsers(browser, tool):
    if not tool:
        return [1]
    else:
        return ast.literal_eval(browser)


def get_bool(value):
    return value.lower() == 'true'


def is_sauce(tool):
    return (tool and tool.lower() == 'sauce')


def is_testingbot(tool):
    return (tool and tool.lower() == 'testingbot')