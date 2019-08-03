import pytest
from fixture.application import Application
from fixture.locators import Locators
import time
from selenium.webdriver.common.keys import Keys


def test_upload_file(app):
    wd = app.wd
    app.session.login()
    '''We find the download button and click on it'''
    wd.find_element(*Locators.UPLOAD_BUTTON).click()
    '''This is path to the file and uploaded it drag and drop method'''
    wd.find_element(*Locators.CHOOSE_BUTTON).send_keys('/Users/arm/demobcd/file/VIDEO_FILE.mp4')
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