from tests.acceptance.locators.classifier_build_page import ClassifierBuildPageLocators
from tests.acceptance.page_model.base_page import BasePage


class ClassifierBuildPage(BasePage):
    @property
    def url(self):
        return super(ClassifierBuildPage, self).url + '/classifier_build'

    @property
    def page(self):
        return self.driver.find_element(*ClassifierBuildPageLocators.PAGE)

    @property
    def charts(self):
        return self.driver.find_elements(*ClassifierBuildPageLocators.CHART)

    @property
    def download(self):
        return self.driver.find_element(*ClassifierBuildPageLocators.DOWNLOAD)

    @property
    def navigation(self):
        return self.driver.find_elements(*ClassifierBuildPageLocators.NAV_LINKS)

