import time
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.Locators = Locators
        self.wd = WebDriver(executable_path="/Users/arm/demobcd/drivers/chromedriver 2")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        #This is fast method to the open home page
        wd = self.wd
        wd.get("http://vm-biocad-filestorage.axmor.nsk/")

    def upload_file(self):
        wd = self.wd
        self.open_home_page()
        #For this we are find upload button and click for it
        wd.find_element(*Locators.UPLOAD_BUTTON).click()
        #This is path to the file and uploaded it drag and drop method
        wd.find_element(*Locators.CHOOSE_BUTTON).send_keys("/Users/arm/demobcd/file/VIDEO_FILE.mp4")
        time.sleep(1)
        #In this we are opened file extended menu
        wd.find_element(*Locators.EXTENDED_BUTTON).click()
        #Writing comment to the file
        wd.find_element(*Locators.UPLOAD_COMMENT).send_keys("This is comment for DEMO")
        #This is click on the tags dropdown menu
        wd.find_element(*Locators.SELECT_DROPDOWN_INDICATOR).click()
        #This is find tag
        wd.find_element(*Locators.INPUT_TEST_VALUE).send_keys("TEST")
        wd.find_element(*Locators.INPUT_TEST_VALUE).send_keys(Keys.DOWN + Keys.ENTER)
        wd.find_element(*Locators.VIDEO_QUALITY).click()
        wd.find_element(*Locators.LAST_DOWNLOAD_BUTTON).click()
        time.sleep(4)
        wd.refresh()

    def create_template(self):
        wd = self.wd
        wd.find_element(*Locators.TEMPLATES_LINK).click()
        wd.find_element(*Locators.CREATE_TEMPLATE).click()
        wd.find_element(*Locators.TEMPLATE_NAME).send_keys("Test name for demo Biocad")
        wd.find_element(*Locators.TEMPLATE_DESCRIPTION).send_keys("TEST_TAGS")
        wd.find_element(*Locators.ASSESS_BUTTON).click()
        wd.find_element(*Locators.SAVE_TEMPLATE).click()

    def create_tag(self):
        wd = self.wd
        wd.find_element(*Locators.TAGS_TOP_BAR).click()
        wd.find_element(*Locators.TAGS_INPUT).send_keys("TEST_TAGS")
        wd.find_element(*Locators.ADD_TAG).click()

    def at_page(self):
        return "FILES" in self.wd.title

    def delete_file(self):
        wd = self.wd
        time.sleep(3)
        wd.find_element(*Locators.SEARCH_FIELD).send_keys("VIDEO_FILE")
        wd.find_element(*Locators.SEARCH_BUTTON).click()
        wd.find_element(*Locators.FILE_IN_GRID).click()
        wd.find_element(*Locators.DELETE_BUTTON).click()

    def drop_down_menu(self):
        wd = self.wd
        try:
            dropdown_menu = WebDriverWait(wd, 10) \
                .until(EC.presence_of_element_located(*Locators.INPUT_TEST_VALUE))
            return dropdown_menu.is_displayed()
        except TimeoutException:
            return False

    def header_page(self):
        wd = self.wd
        try:
            profile_logo_element = WebDriverWait(wd, 10) \
                .until(EC.presence_of_element_located(By.CLASS_NAME, "b-screen__logo-title"))
            return profile_logo_element.is_displayed()
        except TimeoutException:
            return False

    def destroy(self):
        self.wd.quit()
