from behave import *
from selenium import webdriver


from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.classifier_build_page import ClassifierBuildPage
from tests.acceptance.page_model.classifier_fit_page import ClassifierFitPage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.managedb_page import ManagedbPage
from tests.acceptance.page_model.signup_page import SignupPage
from tests.acceptance.page_model.sommeliers_page import SommeliersPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')  ## path to chromedriver
    page = BasePage(context.driver)
    context.driver.get(page.url)


@given('I am on the signup page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = SignupPage(context.driver)
    context.driver.get(page.url)


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = LoginPage(context.driver)
    context.driver.get(page.url)


@given('I am on the manage db page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = ManagedbPage(context.driver)
    context.driver.get(page.url)

@given('I am on the classifier build page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = ClassifierBuildPage(context.driver)
    context.driver.get(page.url)


@given('I am on the classifier fit page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = ClassifierFitPage(context.driver)
    context.driver.get(page.url)


@given('I am on the sommeliers page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = SommeliersPage(context.driver)
    context.driver.get(page.url)





@then('I am on the homepage')
def step_impl(context):
    expected_url = BasePage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the signup page')
def step_impl(context):
    expected_url = SignupPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the login page')
def step_impl(context):
    expected_url = LoginPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the manage db page')
def step_impl(context):
    expected_url = ManagedbPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the classifier build page')
def step_impl(context):
    expected_url = ClassifierBuildPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the classifier fit page')
def step_impl(context):
    expected_url = ClassifierFitPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the sommeliers page')
def step_impl(context):
    expected_url = SommeliersPage(context.driver).url
    assert context.driver.current_url == expected_url
