from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HeaderPage:

    def __init__(self, wd):
        wd = self.wd

    def at_page(self):
        try:
            profile_logo_element = WebDriverWait(self.wd, 10) \
                .until(EC.presence_of_element_located(By.CLASS_NAME, "b-screen__logo-title "))
            return profile_logo_element.is_displayed()
        except TimeoutException:
            return False


class Grid:


    def __init__(self,wd):
        self.wd = wd

    def grid_page(self):
        try:
            page_grid = WebDriverWait(self.wd, 10) \
                .until(EC.presence_of_element_located(By.XPATH, "//div[@class = 'files_grid']"))
            return page_grid.is_displayed()
        except TimeoutException:
            return False