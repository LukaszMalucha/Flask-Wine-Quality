from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def page(self):
        return self.driver.find_element(*BasePageLocators.PAGE)

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def download(self):
        return self.driver.find_element(*BasePageLocators.DOWNLOAD)

    @property
    def dropdown(self):
        return self.driver.find_element(*BasePageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*BasePageLocators.DROPDOWN_LINKS)

    @property
    def quality_chart(self):
        return self.driver.find_element(*BasePageLocators.QUALITY_CHART)


