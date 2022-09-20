from pages.login_page import LoginPage
import pytest
from assertpy import assert_that, soft_assertions
from pages.secure_page import SecurePage


@pytest.mark.pozitive
def test_check_login_functionality(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    assert_that("Welcome to the Secure Area. When you are done click logout below." == secure_page.get_welcome_message())
    assert_that(browser.current_url == secure_page.URL)


def test_invalid_error(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.click_login()
    assert_that(login_page.is_error_text_displayed())


data_list = [
    ('tomsmith', 'password1234', 'Your password is invalid!'),
    ('smithtom', 'password1234', 'Your username is invalid!'),
    ('smithtom', 'SuperSecretPassword!', 'Your username is invalid!'),
    ('', '', 'Your username is invalid!'),
    ('tomsmith', '', 'Your password is invalid!'),
    ('', 'SuperSecretPassword!', 'Your username is invalid!'),
]

@pytest.mark.parametrize('username, password, message', data_list)
def test_negative_login(browser, username, password, message):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login(username, password)
    assert_that(login_page.get_flash_message()).contains(message)


def test_login_page(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    with soft_assertions():
        assert_that(login_page.get_current_url()).ends_with("/login")
        assert_that(login_page.is_image_displayed())
        assert_that(login_page.URL).is_equal_to(browser.current_url)