from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from fixture.session import SessionHelper
from fixture.locators import Locators
from src.pages.header_page import HeaderPage

class Application:

    def __init__(self):
        self.Locators = Locators
        self.header_page = HeaderPage
        self.wd = WebDriver(executable_path="/home/tester/demobiocad/drivers/chromedriver")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://vm-biocad-filestorage.axmor.nsk/")

    def upload_file(self):
        wd = self.wd
        wd.find_element(*Locators.DOWNLOAD_BUTTON).click()
        wd.find_element(*Locators.CHOOSE_BUTTON).send_keys("/home/tester/demobiocad/file/Attila - Villain.mp4")
        wd.find_element(*Locators.LAST_DOWNLOAD_BUTTON).click()

    def create_template(self):
        wd = self.wd
        wd.find_element()

    def destroy(self):
        self.wd.quit()

    def at_page(self):
        return "FILES" in self.wd.title