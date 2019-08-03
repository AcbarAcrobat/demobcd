# coding=utf-8
from fixture.locators import Locators
import time
import allure


def test_create_template(app):
    wd = app.wd
    app.session.login()
    with allure.step("Create template with click to template link"):
        wd.find_element(*Locators.TEMPLATES_LINK).click()
    with allure.step("Just test"):
        wd.find_element(*Locators.CREATE_TEMPLATE).click()
    with allure.step("At under that we are send keys in comment field"):
        wd.find_element(*Locators.TEMPLATE_NAME).send_keys("Test name for demo Biocad")
    wd.find_element(*Locators.TEMPLATE_DESCRIPTION).send_keys("TEST_TAGS")
    wd.find_element(*Locators.ASSESS_BUTTON).click()
    wd.find_element(*Locators.SAVE_TEMPLATE).click()
    time.sleep(1)
    app.test_delete_template()
