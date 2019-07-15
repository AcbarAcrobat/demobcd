from fixture.locators import Locators


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(*Locators.LOGIN_FIELD).clear()
        wd.find_element(*Locators.LOGIN_FIELD).send_keys("superadmin")
        wd.find_element(*Locators.PASSWORD_FIELD).clear()
        wd.find_element(*Locators.PASSWORD_FIELD).send_keys("gwRz7WWs6kXd")
        wd.find_element(*Locators.SUBMIT_BUTTON).submit()
