import random
import string
import sys
from random import randint

from constants import FrameworkConstants


def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = type(name, (base_class,), d)

    return decorator


def is_sauce(tool):
    return (tool and tool.lower() == 'sauce')


def is_testingbot(tool):
    return (tool and tool.lower() == 'testingbot')


def random_string_with_prefix(prefix="rand"):
    return prefix + str(randint(0, 10000000))


def generate_random_email(prefix="mailrand", length=6, domain="4test.test"):
    random_name = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return prefix + random_name + "@" + domain
