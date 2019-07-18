from common.configuration import Configuration as Config
from web_driver.driver import get_driver
from web_driver.driver import close_driver
from web_driver.find import Find
import time
import logging
from urllib.parse import urljoin
from hamcrest import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from contextlib import contextmanager
from fixture.locators import Locators


def see_text(self, text, element=None):
    with self._step(f"See text in {element}"):
        self._enable_implicit_wait()
        text_from_page = self.get_visible_text(element)
        self._disable_implicit_wait()
        assert_that(text_from_page, contains_string(text))


def get_visible_text(self, element=None):
    with self._step(f"Get visible text from {element}"):
        if element is not None:
            return self.grab_text_from(element)

        els = self._match(Find("body"))
        if len(els) == 0:
            return ''

        return els[0].text
