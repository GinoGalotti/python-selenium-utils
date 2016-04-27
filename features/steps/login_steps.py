from SeleniumPythonFramework.src.main.Pages.login_page import LogInPage
from SeleniumPythonFramework.src.main.Utils.common_steps import generate_random_email
from SeleniumPythonFramework.src.main.Utils.constants import TestingConstants
from behave import when, given, then


@given('I am the user called "{name}"')
def step_impl(context, name):
    context.current_user = context.users['users'][name]
    print("current user is:- {}".format(context.current_user))


@given('I am a new user')
def step_impl(context):
    user = {"email": generate_random_email(), "password": TestingConstants.DEFAULT_PASSWORD}
    context.current_user = user


@given('I am logged via web')
@when('I login via web')
def step_impl(context):
    context.current_page = context.page_builder.get_page(LogInPage)
    context.current_page.load_page()

    context.current_page.login_account(context.current_user['email'], context.current_user['password'])

    # Next page in most cases will be Dashboard (not for old account, but we don't care abut 'em)
    context.current_page = context.page_builder.get_page(NextPage)
    assert TestingConstants.PATH_AFTER_LOGIN in context.driver.current_url, "After logging in we're expecting {0} in path".format(
        TestingConstants.PATH_AFTER_LOGIN)


@then('I delete the user')
def step_impl(context):
    api_session = ApiSession()
    api_session.delete_account(context.current_user['email'], context.current_user['password'])


def assert_page_is_login(page_object):
    assert isinstance(page_object, LogInPage)