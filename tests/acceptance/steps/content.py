from behave import *
from pathlib import Path

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.classifier_build_page import ClassifierBuildPage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.managedb_page import ManagedbPage
from tests.acceptance.page_model.signup_page import SignupPage
from tests.acceptance.page_model.sommeliers_page import SommeliersPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


@then('I can see there is a quality chart on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.quality_chart.is_displayed()

@then('I can see there is a signup form on the page')
def step_impl(context):
    page = SignupPage(context.driver)
    assert page.form.is_displayed()


@then('I can see there is a login form on the page')
def step_impl(context):
    page = LoginPage(context.driver)
    assert page.form.is_displayed()


@then('I can see there is the add template form displayed on the page')
def step_impl(context):
    page = ManagedbPage(context.driver)
    assert page.add_template_form.is_displayed()


@then('I can see there are six charts displayed on the page')
def step_impl(context):
    page = ClassifierBuildPage(context.driver)
    charts = page.charts
    assert len(charts) == 6

@then('I can see there is the rate form displayed on the page')
def step_impl(context):
    page = SommeliersPage(context.driver)
    assert page.form_rate.is_displayed()


@then('There three sommelier scores are displayed')
def step_impl(context):
    page = SommeliersPage(context.driver)
    assert len(page.scores) == 3

@then('I downloaded the code template')
def step_impl(context):
    file = Path('.....Downloads\\dataset_describe.py')  ## specify
    assert file.exists()





