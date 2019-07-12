import time
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Application:

    def __init__(self):
        self.Locators = Locators
        self.wd = WebDriver(executable_path="/Users/arm/demobcd/drivers/chromedriver 2")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://vm-biocad-filestorage.axmor.nsk/")

    def upload_file(self):
        wd = self.wd
        wd.find_element(*Locators.UPLOAD_BUTTON).click()
        wd.find_element(*Locators.CHOOSE_BUTTON).send_keys("/Users/arm/demobcd/file/VIDEO_FILE.mp4")
        wd.find_element(*Locators.LAST_DOWNLOAD_BUTTON).click()

    def create_template(self):
        wd = self.wd
        wd.find_element()

    def destroy(self):
        self.wd.quit()

    def at_page(self):
        return "FILES" in self.wd.title

    def delete_file(self):
        wd = self.wd
        time.sleep(3)
        wd.find_element(*Locators.SEARCH_FIELD).send_keys("VIDEO_FILE")
        wd.find_element(*Locators.SEARCH_BUTTON).click()
        wd.find_element(*Locators.FILE_IN_GRID).click()
        wd.find_element(*Locators.DELETE_BUTTON).click()

    def create_template(self):
        wd = self.wd
        wd.find_element(*Locators.TEMPLATES_LINK).click()
        wd.find_element()

    def header_page(self):
        wd = self.wd
        try:
            profile_logo_element = WebDriverWait(wd, 10) \
                .until(EC.presence_of_element_located(By.CLASS_NAME, "b-screen__logo-title"))
            return profile_logo_element.is_displayed()
        except TimeoutException:
            return False
