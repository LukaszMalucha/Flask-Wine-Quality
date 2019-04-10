from selenium.webdriver.common.by import By

from tests.acceptance.locators.managedb_page import ManagedbPageLocators
from tests.acceptance.page_model.base_page import BasePage


class ManagedbPage(BasePage):
    @property
    def url(self):
        return super(ManagedbPage, self).url + '/manage_db'

    @property
    def add_template_form(self):
        return self.driver.find_element(*ManagedbPageLocators.ADD_TEMPLATE)

    @property
    def submit_algorithm(self):
        return self.driver.find_element(*ManagedbPageLocators.SUBMIT_TEMPLATE)

    def add_template_form_field(self, name):
        return self.add_algorithm_form.find_element(By.NAME, name)
