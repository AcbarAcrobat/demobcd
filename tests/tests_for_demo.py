import pytest
from fixture.application import Application


def test_upload_file(app):
    app.session.login()
    assert app.header_page
    app.at_page()
    app.create_tag()
    app.upload_file()
    assert app.see_upload_info()
    app.delete_file()
    app.destroy()

