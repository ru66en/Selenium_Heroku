from pages.status_codes200 import StatusCodes200
from pages.status_codes_page import StatusCodes
from time import sleep


def test_link200(browser):
    status_page = StatusCodes(browser)
    status_page.load_page()
    status_page.click_link200()
    status_page200 = StatusCodes200(browser)
    assert status_page.current_url() == 'https://the-internet.herokuapp.com/status_codes/200'
    assert status_page200.is_text_displayed()
    status_page200.click_link_here()
    assert status_page200.current_url() == 'https://the-internet.herokuapp.com/status_codes'


def test_link301(browser):
    status_page = StatusCodes(browser)
    status_page.load_page()
    status_page.click_link301()
    assert status_page.current_url() == 'https://the-internet.herokuapp.com/status_codes/301'


def test_link404(browser):
    status_page = StatusCodes(browser)
    status_page.load_page()
    status_page.click_link404()
    assert status_page.current_url() == 'https://the-internet.herokuapp.com/status_codes/404'


def test_link500(browser):
    status_page = StatusCodes(browser)
    status_page.load_page()
    status_page.click_link500()
    assert status_page.current_url() == 'https://the-internet.herokuapp.com/status_codes/500'


def test_click_link_here(browser):
    status_page = StatusCodes(browser)
    status_page.load_page()
    status_page.click_link_here()
    assert status_page.current_url() == 'http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml'


def test_page_elements(browser):
    status_page = StatusCodes(browser)
    status_page.load_page()
    assert status_page.get_subtitle_text() == 'Status Codes'
    assert status_page.is_text_displayed()
    assert status_page.URL == 'https://the-internet.herokuapp.com/status_codes'
    assert status_page.is_200_displayed()
    assert status_page.is_301_displayed()
    assert status_page.is_404_displayed()
    assert status_page.is_500_displayed()



