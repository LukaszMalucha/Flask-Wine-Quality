from tests.acceptance.locators.classifier_fit_page import ClassifierFitPageLocators
from tests.acceptance.page_model.base_page import BasePage


class ClassifierFitPage(BasePage):
    @property
    def url(self):
        return super(ClassifierFitPage, self).url + '/classifier_fit'

    @property
    def download(self):
        return self.driver.find_element(*ClassifierFitPageLocators.DOWNLOAD)

    @property
    def navigation(self):
        return self.driver.find_elements(*ClassifierFitPageLocators.NAV_LINKS)

