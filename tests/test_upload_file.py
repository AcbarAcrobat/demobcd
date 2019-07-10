import pytest
from fixture.application import Application
from src.pages.header_page import HeaderPage


def test_upload_file(app):
    app.session.login()
    assert app.header_page
    app.at_page()
    app.upload_file()
    app.destroy()

def test_delete_file(app):
    pass