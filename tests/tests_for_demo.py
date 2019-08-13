import pytest
from fixture.application import Application


def test_upload_file(app):
    app.session.login()
    assert app.header_page
    app.at_page()
    app.test_create_tag()
    app.test_upload_file()
    app.check_upload_status()
    app.test_delete_file()
    app.test_delete_tag()
    app.destroy()

