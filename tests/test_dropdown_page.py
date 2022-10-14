from assertpy import soft_assertions, assert_that

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
    assert dropdown_page.is_value_selected("1")


def test_image(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.load_page()
    dropdown_page.is_image_displayed()
    with soft_assertions():
        assert_that(dropdown_page.is_image_displayed())
    sleep(3)