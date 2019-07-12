from selenium.webdriver.common.by import By


class Locators:

    LOGIN_INPUT = (By.ID, "login")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn-success")
    UPLOAD_BUTTON = (By.XPATH, "//span[text()='Загрузить файл' or text() = 'Upload file']")
    CHOOSE_BUTTON = (By.XPATH, "//input[@type = 'file']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    LAST_DOWNLOAD_BUTTON = (By.XPATH, "//span[text()='Загрузить' or text() = 'Upload']")
    TEMPLATES_LINK = (By.XPATH, "//a[contains(@href,'templates')]")
    TAG_LINK = (By.XPATH, "//a[contains(@href,'tags')]")
    FILES_GRID = (By.XPATH, "//div[@class = 'files_grid']")
    SEARCH_FIELD = (By.XPATH, "//input[@id = 'filename']")
    SEARCH_BUTTON = (By.XPATH, "//span[text() = 'Поиск' or text() = 'Search']")
    FILE_IN_GRID = (By.XPATH, "//span[text() = 'VIDEO_FILE.mp4']")
    DELETE_BUTTON = (By.XPATH, "//span[text() = 'Delete' or text() = 'Удалить']")
    CREATE_TEMPLATE = (By.XPATH, "//span[text() = 'Create template' or text() = 'Создать шаблон']")
    TEMPLATE_NAME = (By.ID, "templateName")
    ASSESS_BUTTON = (By.XPATH, "//label[@for = 'quality-To all']")
    SAVE_TEMPLATE = (By.XPATH, "//span[text() = 'Save']")
    DELETE_TEMPLATE = (By)