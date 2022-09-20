from pages.dropdown_page import DropdownPage
from time import sleep


def test_subtitle_displayed(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    assert dropdown_page.get_subtitle() == 'Dropdown List'


def test_select_option(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.select_option('Option 1')
    sleep(5)


def test_image(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.is_image_displayed()
