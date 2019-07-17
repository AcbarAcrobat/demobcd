import time
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Application:

    def __init__(self):
        """These are launch artifacts"""
        self.Locators = Locators
        self.wd = WebDriver(executable_path="/home/tester/demobcd/drivers/chromedriver")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        """This is fast method to the open home page."""
        wd = self.wd
        wd.get("http://vm-biocad-filestorage.axmor.nsk/")

    def upload_file(self):
        wd = self.wd
        self.open_home_page()
        '''We find the download button and click on it'''
        wd.find_element(*Locators.UPLOAD_BUTTON).click()
        '''This is path to the file and uploaded it drag and drop method'''
        wd.find_element(*Locators.CHOOSE_BUTTON).send_keys("/home/tester/demobcd/file/VIDEO_FILE.mp4")
        time.sleep(1)
        '''In this we are opened file extended menu'''
        wd.find_element(*Locators.EXTENDED_BUTTON).click()
        '''Writing comment in the upload file form'''
        wd.find_element(*Locators.UPLOAD_COMMENT).send_keys("This is comment for DEMO")
        '''This is click on the tags dropdown menu'''
        wd.find_element(*Locators.SELECT_DROPDOWN_INDICATOR).click()
        '''Find value in the tags field'''
        wd.find_element(*Locators.INPUT_TEST_VALUE).send_keys("TEST")
        wd.find_element(*Locators.INPUT_TEST_VALUE).send_keys(Keys.DOWN + Keys.ENTER)
        '''click the video quality button'''
        wd.find_element(*Locators.VIDEO_QUALITY).click()
        '''click download button'''
        wd.find_element(*Locators.FINALLY_UPLOAD_BUTTON).click()
        '''wait delay after uploaded end'''
        time.sleep(3)

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
        wd.find_element(*Locators.TAGS_INPUT_FIELD).send_keys("TEST_TAGS")
        wd.find_element(*Locators.ADD_TAG).click()

    def at_page(self):
        return "FILES" in self.wd.title

    def delete_file(self):
        wd = self.wd
        wd.find_element(*Locators.UPLOAD_STATUS).click()
        self.check_upload_status()
        wd.find_element(*Locators.SEARCH_FIELD).send_keys("VIDEO")
        wd.find_element(*Locators.SEARCH_BUTTON).click()
        wd.find_element(*Locators.FILE_IN_GRID).click()
        wd.find_element(*Locators.DELETE_BUTTON).click()

    def check_upload_status(self):
        wd = self.wd
        try:
            upload_info = WebDriverWait(wd, 15).until(
                EC.text_to_be_present_in_element(*Locators.UPLOAD_INFO)
            )
        except TimeoutException:
            return False

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
