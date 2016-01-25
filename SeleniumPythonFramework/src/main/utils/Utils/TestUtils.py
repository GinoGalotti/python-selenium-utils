__author__ = 'ginogalotti'
import random
import string
from random import randint

from SeleniumPythonFramework.src.main.utils.Utils.Constants import FrameworkConstants


class TestUtils(object):
    @staticmethod
    def generate_random_name(prefix="namerand"):
        return prefix + str(randint(100, 200))

    @staticmethod
    def generate_random_email(prefix="mailrand", length=6, domain="4null.com"):
        random_name = ''.join(random.choice(string.ascii_letters) for i in range(length))
        return prefix + random_name + "@" + domain

    @staticmethod
    def is_production_test(env):
        return env == FrameworkConstants.PRODUCTION_ENV
