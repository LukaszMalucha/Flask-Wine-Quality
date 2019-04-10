from behave import *
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.base_page import BasePageLocators
from tests.acceptance.locators.sommeliers_page import SommeliersPageLocators

use_step_matcher('re')


@given('I wait for the page to load')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(
        expected_conditions.visibility_of_element_located(BasePageLocators.PAGE)
    )


@given('I wait for the dropdown to load')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(
        expected_conditions.visibility_of_element_located(BasePageLocators.DROPDOWN)
    )

@given('I wait for the quality chart to load')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(
        expected_conditions.visibility_of_element_located(BasePageLocators.QUALITY_CHART)
    )

@given('I wait for the sommeliers page to load')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(
        expected_conditions.visibility_of_element_located(SommeliersPageLocators.SCORES)
    )

@given('I wait for the download code template to finish')
def step_impl(context):
    time.sleep(1)