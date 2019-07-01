from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    LOGIN_INPUT = (By.ID, "login")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn-success")
    driver = None

    def __init__(self, driver):
        self.driver = driver


    def login_to_bcd(self):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys("superadmin")
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("gwRz7WWs6kXd")
        self.driver.find_element(*self.LOGIN_BUTTON).submit()

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*self.LOGIN_INPUT)).click()

    def at_page(self):
        return "FILES" in self.driver.title

    def open(self):
        self.driver.get("http://vm-biocad-filestorage.axmor.nsk:8085/")
        return self