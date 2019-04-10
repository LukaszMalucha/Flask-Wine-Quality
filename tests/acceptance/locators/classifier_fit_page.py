from selenium.webdriver.common.by import By


class ClassifierFitPageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS =  By.ID, 'navigation'
    PAGE = By.ID, 'page-index'
    DOWNLOAD = By.ID, 'button-download'
