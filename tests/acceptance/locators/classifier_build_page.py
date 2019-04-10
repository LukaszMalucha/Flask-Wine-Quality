from selenium.webdriver.common.by import By


class ClassifierBuildPageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS =  By.ID, 'navigation'
    PAGE = By.ID, 'page-index'
    DOWNLOAD = By.ID, 'button-download'
    CHART = By.CLASS_NAME, 'img-responsive'
