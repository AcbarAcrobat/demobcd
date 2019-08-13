from selenium.webdriver.common.by import By


class Locators:
    # login page locators
    LOGIN_FIELD = (By.ID, "login")
    SUBMIT_BUTTON = (By.CLASS_NAME, "btn-success")
    PASSWORD_FIELD = (By.ID, "password")
    # main page locators
    SEARCH_FIELD = (By.XPATH, "//input[@id = 'filename']")
    SEARCH_BUTTON = (By.XPATH, "//span[text() = 'Поиск' or text() = 'Search']")
    UPLOAD_BUTTON = (By.XPATH, "//span[contains(@class, 'hastext') and contains(., 'Загрузить') or contains(., 'Upload')]")
    CHOOSE_BUTTON = (By.XPATH, "//input[@type = 'file']")
    FILES_GRID = (By.XPATH, "//div[@class = 'files_grid']")
    FILE_IN_GRID = (By.XPATH, "//span[text() = 'VIDEO_FILE.mp4']")
    UPLOAD_STATUS = (By.XPATH,"//*[name()='svg' and contains(@class, 'svg-inline--fa fa-arrow')]")
    UPLOAD_INFO = (By.XPATH, "//div[contains(@class, 'uploading-file-size')][contains(., 'success') or contains(., 'успешно загружен')]")
    # upload form locators
    EXTENDED_BUTTON = (By.XPATH, "//div[@class = 'uploadFile__prev_filename_size']/following-sibling::button")
    UPLOAD_COMMENT = (By.ID, "comment")
    ADD_TAG = (By.XPATH, "//span[text() = 'Add' or text() = 'Добавить']")
    TAGS_INPUT_FIELD = (By.ID, "tag")
    INPUT_TEST_VALUE = (By.XPATH, "//input[contains(@id, 'react-select')]")
    PUT_TEST_VALUE = (By.XPATH, "//div[contains(@class, 'select__value-container')]")
    SELECT_DROPDOWN_INDICATOR = (By.XPATH, "//div[contains(@class, 'select__dropdown-indicator')]")
    VIDEO_QUALITY = (By.XPATH, "//label[text() = 'Низкое' or text() = 'Low']")
    FINALLY_UPLOAD_BUTTON = (By.XPATH, "//span[text()='Загрузить' or text() = 'Upload']")
    # top bar locators
    TAG_LINK = (By.XPATH, "//a[contains(@href,'tags')]")
    TAGS_TOP_BAR = (By.XPATH, "//a[contains(@href,'/tags')]")
    TEMPLATES_LINK = (By.XPATH, "//a[contains(@href,'templates')]")
    FILES_LINK = (By.XPATH, "//a[contains(@href,'files')]")
    # templates page
    CREATE_TEMPLATE = (By.XPATH, "//span[text() = 'Create template' or text() = 'Создать шаблон']")
    TEMPLATE_NAME = (By.ID, "templateName")
    TEMPLATE_DESCRIPTION = (By.ID, "pattern")
    SAVE_TEMPLATE = (By.XPATH, "//span[text() = 'Save' or text()='Сохранить']")
    ASSESS_BUTTON = (By.XPATH, "(//label[contains(., 'Всем') or contains(., 'All')])")
    DELETE_LAST_TEMPLATE = (By.XPATH, "(//div[contains(@class, 'grid__cell-ico')]/following-sibling::*)[last()-3]")
    # tags page
    DELETE_LAST_TAG = (By.XPATH, "(//button[contains(@class, 'delete_tag')])[1]")
    # main page actions forms
    DELETE_BUTTON = (By.XPATH, "//span[text() = 'Delete' or text() = 'Удалить']")
