from selenium.webdriver.common.by import By


class Locators:


    LOGIN_INPUT = (By.ID, "login")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn-success")
    DOWNLOAD_BUTTON = (By.XPATH, "//span[text()='Загрузить файл']")
    CHOOSE_BUTTON = (By.XPATH, "//input[@type = 'file']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    LAST_DOWNLOAD_BUTTON = (By.XPATH, "//span[text()='Загрузить']")
    TEMPLATES_LINK = (By.XPATH, "//a[contains(@href,'templates')]")
    TAG_LINK = (By.XPATH, "//a[contains(@href,'tags')]")
    FILES_GRID = (By.XPATH, "//div[@class = 'files_grid']")