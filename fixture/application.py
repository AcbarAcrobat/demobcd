# coding=utf-8
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Application:

    def __init__(self):
        """These are launch artifacts"""
        self.Locators = Locators
        self.wd = WebDriver(executable_path='../demobcd/drivers/chromedriver 2')
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        """This is fast method to the open home page."""
        wd = self.wd
        wd.get('http://vm-biocad-filestorage.axmor.nsk/')

    def test_upload_file(self):
        wd = self.wd
        '''We find the download button and click on it'''
        wd.find_element(*Locators.UPLOAD_BUTTON).click()
        '''This is path to the file and uploaded it drag and drop method'''
        wd.find_element(*Locators.CHOOSE_BUTTON).send_keys(my_file)
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
        time.sleep(1)

    def check_upload_status(self):
        wd = self.wd
        wd.implicitly_wait(0)
        try:
            wd.find_element(*Locators.UPLOAD_STATUS).click()
            elm = WebDriverWait(wd, 60).until(EC.visibility_of_any_elements_located((Locators.UPLOAD_INFO)))
            time.sleep(2)
            return elm
        except TimeoutException:
            return False

    def test_create_template(self):
        wd = self.wd
        wd.find_element(*Locators.TEMPLATES_LINK).click()
        wd.find_element(*Locators.CREATE_TEMPLATE).click()
        wd.find_element(*Locators.TEMPLATE_NAME).send_keys("Test name for demo Biocad")
        wd.find_element(*Locators.TEMPLATE_DESCRIPTION).send_keys("TEST_TAGS")
        wd.find_element(*Locators.ASSESS_BUTTON).click()
        wd.find_element(*Locators.SAVE_TEMPLATE).click()

    def test_delete_template(self):
        wd = self.wd
        wd.find_element(*Locators.TEMPLATES_LINK).click()
        wd.find_element(*Locators.DELETE_LAST_TEMPLATE).click()

    def test_create_tag(self):
        wd = self.wd
        wd.find_element(*Locators.TAGS_TOP_BAR).click()
        wd.find_element(*Locators.TAGS_INPUT_FIELD).send_keys("TEST_TAGS")
        wd.find_element(*Locators.ADD_TAG).click()

    def test_delete_tag(self):
        wd = self.wd
        wd.find_element(*Locators.TAGS_TOP_BAR).click()
        wd.find_element((Locators.DELETE_LAST_TAG)).click()

    def at_page(self):
        return "FILES" in self.wd.title

    def test_delete_file(self):
        wd = self.wd
        wd.find_element(*Locators.SEARCH_FIELD).send_keys("VIDEO")
        wd.find_element(*Locators.SEARCH_BUTTON).click()
        time.sleep(3)
        wd.find_element(*Locators.FILE_IN_GRID).click()
        wd.find_element(*Locators.DELETE_BUTTON).click()

    def header_page(self):
        wd = self.wd
        try:
            profile_logo_element = WebDriverWait(wd, 10) \
                .until(EC.presence_of_element_located(By.CLASS_NAME, 'b-screen__logo-title'))
            return profile_logo_element.is_displayed()
        except TimeoutException:
            return False

    def destroy(self):
        self.wd.quit()
