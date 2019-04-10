from selenium.webdriver.common.by import By


class SommeliersPageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS =  By.ID, 'navigation'
    PAGE = By.ID, 'page-index'
    FORM_RATE = By.ID, 'form-rate'
    SCORES = By.ID, 'score'
