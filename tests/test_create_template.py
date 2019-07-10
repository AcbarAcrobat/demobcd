# import pytest
# from src.pages.header_page import HeaderPage
# from src.pages.login_page import LoginPage
# from src.pages.main_page import MainPage
# import time
#
# @pytest.mark.usefixtures("get_driver")
# class TestUpload:
#
#     def test_upload_file(self):
#         self.login_page = LoginPage(self.driver)
#         self.header_page = HeaderPage(self.driver)
#         self.main_page = MainPage(self.driver)
#         self.login_page.open()
#         assert self.login_page.at_page()
#         self.login_page.login_to_bcd()
#         assert self.header_page.at_page()
#         time.sleep(3)
#         self.main_page.click_download_button()
#
#
#
#
#
