from behave import then, when

from SeleniumPythonFramework.src.main.Utils.constants import TestingConstants


@then('I should be redirected to dashboard')
def step_impl(context):
    assert_we_are_on_dashboard(context.driver.current_url)


@when('I run the extractor')
def step_impl(context):
    assert_we_are_on_dashboard(context.driver.current_url)
    assert_page_is_dashboard(context.current_page)

    assert context.current_page.click_run_and_check_started(), "It should correctly start the run"


@then('The run should correctly finish')
def step_impl(context):
    assert_we_are_on_dashboard(context.driver.current_url)
    assert_page_is_dashboard(context.current_page)

    assert context.current_page.check_las_run_finished(), "Last run should end in time"


def assert_we_are_on_dashboard(path):
    assert TestingConstants.PATH_AFTER_LOGIN in path, "After logging in we're expecting {0} in path".format(
        TestingConstants.PATH_AFTER_LOGIN)
