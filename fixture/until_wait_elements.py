from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _find_element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture.application import Application
from fixture.locators import Locators


class text_to_be_present_in_element(object):
    """ An expectation for checking if the given text is present in the
    specified element.
    locator, text
    """

    def __init__(self, Locators, locator, app, text_):
        self.Locators = Locators
        self.locator = locator
        self.app = app
        self.text = text_
        self.wd = WebDriver(executable_path="~/drivers/chromedriver 2")
        self.wd.implicitly_wait(60)

    def __call__(self):
        wd = self.wd
        try:
            element_text = _find_element(wd, *Locators.UPLOAD_INFO).text
            return self.text in element_text
        except StaleElementReferenceException:
            return False



