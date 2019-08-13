from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _find_element, _find_elements, _element_if_visible
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
        self.wd = WebDriver(executable_path="~/demobcd/drivers/chromedriver")
        self.wd.implicitly_wait(60)

    def __call__(self):
        wd = self.wd
        try:
            element_text = _find_element(wd, *Locators.UPLOAD_INFO).text
            return self.text in element_text
        except StaleElementReferenceException:
            return False


class visibility_of_all_elements_located(object):
    """ An expectation for checking that all elements are present on the DOM of a
    page and visible. Visibility means that the elements are not only displayed
    but also has a height and width that is greater than 0.
    locator - used to find the elements
    returns the list of WebElements once they are located and visible
    """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            elements = _find_elements(driver, self.locator)
            for element in elements:
                if _element_if_visible(element, visibility=False):
                    return False
            return elements
        except StaleElementReferenceException:
            return False


