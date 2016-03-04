__author__ = 'Gino'
import ast
import json
import os
import platform

STAGING_ENV = "staging"
PRODUCTION_ENV = "production"
MAC_CHROMEDRIVER_PATH = "chromedriver/chromedriverMac"
LINUX_CHROMEDRIVER_PATH = "chromedriver/chromedriverLinux64"
WINDOWS_CHROMEDRIVER_PATH = "chromedriver/chromedriver.exe"


# This should be an enum in Python 3.4
def get_environment_variables():
    # This allow us to specify multiple browsers when using a Selenium grid
    desired_cap_default = "[ {'platform': 'WIN7', 'browserName': 'firefox', 'version': '24' }, {'platform': 'MAVERICKS', 'browserName': 'chrome', 'version': '46' }]"

    # Params defined on ENV variables
    env_variables_dict = dict()

    env_variables_dict['tool'] = os.getenv('TESTING_TOOL', None)
    env_variables_dict['chromedriver_local'] = os.getenv('CHROMEDRIVER_LOCAL', get_chromedriver_per_platform())
    if env_variables_dict['tool'] and env_variables_dict['tool'].lower() == "docker":
        env_variables_dict['chromedriver_local'] = LINUX_CHROMEDRIVER_PATH
    env_variables_dict['browser'] = get_browsers(os.getenv('TESTING_BROWSERS', desired_cap_default),
                                                 env_variables_dict['tool'])
    env_variables_dict['mobile'] = get_bool(os.getenv('TESTING_MOBILE', 'False'))
    env_variables_dict['build'] = os.getenv('BUILD_ID', None)
    env_variables_dict['project'] = os.getenv('TESTING_PROJECT_NAME', 'PROJECT_NAME')
    env_variables_dict['env'] = os.getenv('TESTING_ENV', 'production')

    # Not needed if we're not using tools
    # env_variables_dict['default_resolution'] = os.getenv('SELENIUM_SCREEN_RESOLUTION', "1600x1200")
    # env_variables_dict['video_upload_on_pass'] = get_bool(os.getenv('SELENIUM_VIDEO_UPLOAD_PASS', 'False'))
    # env_variables_dict['command_timeout'] = os.getenv('SAUCE_COMMAND_TIMEOUT', 120)
    # env_variables_dict['testingbot_user'] = os.getenv('TESTINGBOT_NAME', "TESTINGBOT_NAME")
    # env_variables_dict['testingbot_pass'] = os.getenv('TESTINGBOT_API', "TESTINGBOT_API")
    # env_variables_dict['sauce_user'] = os.getenv('SAUCE_USER_NAME', "SAUCE_NAME")
    # env_variables_dict['sauce_pass'] = os.getenv('SAUCE_API_KEY', "SAUCE_API")

    return env_variables_dict


def get_bool(value):
    return value.lower() == 'true'


def get_chromedriver_per_platform():
    system = platform.system()

    return {
        'Darwin': MAC_CHROMEDRIVER_PATH,
        'Linux': LINUX_CHROMEDRIVER_PATH,
        'Windows': WINDOWS_CHROMEDRIVER_PATH
    }[system]


def get_browsers(browser, tool):
    # This allow us to trick on_platform
    if not tool:
        return [1]
    else:
        return ast.literal_eval(browser)


def load_users(env):
    filename = "users.json"
    return load_json_key(filename, env)


def load_json_key(file, key):
    with open(file) as f:
        config = json.load(f)
    if key in config:
        return config[key]
    # log.warn('Using default configuration from {0} because key [{1}] is undefined.'.format(filename, env))
    return config['default']


environment_variables = get_environment_variables()
user_map = load_users(environment_variables['env'])
is_production = environment_variables['env'] == 'production'

if environment_variables['env'] == 'production':
    domain = "luisgalottiqa.atlassian.net"
