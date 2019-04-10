from selenium.webdriver.common.by import By

from tests.acceptance.locators.sommeliers_page import SommeliersPageLocators
from tests.acceptance.page_model.base_page import BasePage


class SommeliersPage(BasePage):
    @property
    def url(self):
        return super(SommeliersPage, self).url + '/sommeliers'

    @property
    def page(self):
        return self.driver.find_element(*SommeliersPageLocators.PAGE)

    @property
    def download(self):
        return self.driver.find_element(*SommeliersPageLocators.DOWNLOAD)

    @property
    def scores(self):
        return self.driver.find_elements(*SommeliersPageLocators.SCORES)

    @property
    def navigation(self):
        return self.driver.find_elements(*SommeliersPageLocators.NAV_LINKS)

    @property
    def form_rate(self):
        return self.driver.find_element(*SommeliersPageLocators.FORM_RATE)

    def form_field(self, name):
        return self.form_rate.find_element(By.NAME, name)
