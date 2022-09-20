# from pages.add_remove_elements_page import AddRemoveElementsPage
# from assertpy import assert_that, soft_assertions
# import pytest
# from time import sleep
#
#
# def test_check_add_remove_page(browser):
#     add_remove_page = AddRemoveElementsPage(browser)
#     add_remove_page.load_page()
#     assert add_remove_page.get_title_page_text() == 'Add/Remove Elements', 'Check URL is ok'
#     assert add_remove_page.is_add_button_displayed(), 'Check Add Button is displayed'
#     sleep(5)
#
#
# def test_add_and_remove_button_functionality(browser):
#     add_remove_page = AddRemoveElementsPage(browser)
#     add_remove_page.load_page()
#     add_remove_page.click_add_element_button()
#     assert add_remove_page.is_delete_button_displayed()
#     sleep(5)
#
# def test_url(browser):
#     add_remove_page = AddRemoveElementsPage(browser)
#     add_remove_page.load_page()
#     assert browser.current_url == add_remove_page.URL, 'Check URL is ok'
#     sleep(5)
#
# def test_selenium_link(browser):
#     add_remove_page = AddRemoveElementsPage(browser)
#     add_remove_page.load_page()
#     add_remove_page.is_link_displayed()
#     assert add_remove_page.get_link_text() == 'Elemental Selenium'

from assertpy import assert_that, soft_assertions
from pages.add_remove_elements_page import AddRemoveElementsPage
import pytest
from time import sleep


def test_check_add_element_functionality(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    add_remove_page.click_add_element_button()
    assert_that(add_remove_page.is_add_button_displayed())


def test_link(browser):
    link_check = AddRemoveElementsPage(browser)
    link_check.load_page()
    assert_that(link_check.is_link_displayed())
    sleep(2)
    link_check.click_link()
    browser.switch_to.window(browser.window_handles[1])
    assert_that('http://elementalselenium.com/' == browser.current_url)
    sleep(5)


def test_check_add_remove_elements_page(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()
    with soft_assertions():
        assert_that(add_remove_page.get_title_page_text()).is_equal_to("Add/Remove Elements")
        assert_that(add_remove_page.is_add_button_displayed())
        assert_that(add_remove_page.URL == browser.current_url)
        sleep(5)


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





# __________________________________________

# @pytest.mark.skip




