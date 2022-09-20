from pages.login_page import LoginPage
from assertpy import assert_that, soft_assertions
from pages.secure_page import SecurePage
from time import sleep


def test_check_logout_functionality(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    secure_page.click_logout()
    with soft_assertions():
        assert_that(browser.current_url == login_page.URL)
        assert_that(login_page.get_flash_message() == 'You logged out of the secure area!')
    sleep(5)

def test_secure_page(browser):
    login_page = LoginPage(browser)
    login_page.load_page()
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page = SecurePage(browser)
    with soft_assertions():
        assert_that(browser.current_url).is_equal_to(secure_page.URL)
        assert_that(secure_page.get_welcome_message()).is_equal_to('Welcome to the Secure Area. When you are done click logout below.')
        assert_that(secure_page.is_flash_text_displayed())