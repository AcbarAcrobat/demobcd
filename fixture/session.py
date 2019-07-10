from fixture.locators import Locators


class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(*Locators.LOGIN_INPUT).clear()
        wd.find_element(*Locators.LOGIN_INPUT).send_keys("superadmin")
        wd.find_element(*Locators.PASSWORD_INPUT).clear()
        wd.find_element(*Locators.PASSWORD_INPUT).send_keys("gwRz7WWs6kXd")
        wd.find_element(*Locators.LOGIN_BUTTON).submit()

    # def click_login_button(app):
    #     wd = app.wd
    #     WebDriverWait(wd.app, 10).until(EC.presence_of_element_located(*Locators.LOGIN_INPUT)).click()