from assertpy import assert_that, soft_assertions
from pages.add_remove_elements_page import AddRemoveElementsPage
import pytest


def test_check_add_element_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.click_add_button()
    assert_that(add_remove_page.is_add_button_displayed())


def test_check_add_remove_elements_page(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    with soft_assertions():
        assert_that(add_remove_page.get_title_page()).is_equal_to("Add/Remove Elements")
        assert_that(add_remove_page.is_add_button_displayed())
        assert_that(add_remove_page.URL == browser.current_url)


def test_link(browser):
    link_check = AddRemoveElementsPage(browser)
    link_check.load_page()
    assert_that(link_check.is_link_displayed())
    link_check.click_link()
    browser.switch_to.window(browser.window_handles[1])
    assert_that('http://elementalselenium.com/' == browser.current_url)


def test_add_page(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.click_add_button()
    assert_that(add_remove_page.get_number_of_delete_button()).is_equal_to(1)
    add_remove_page.click_delete_button()
    assert_that(add_remove_page.get_number_of_delete_button()).is_equal_to(0)


#create suite smoke
@pytest.mark.smoke
def test_remove_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    for i in range(10):
        add_remove_page.click_add_button()
        assert_that(add_remove_page.get_number_of_delete_button()).is_equal_to(i+1)
    for i in range(10):
        add_remove_page.click_first_delete_button()
        assert_that(add_remove_page.get_number_of_delete_button()).is_equal_to(10 - i - 1)