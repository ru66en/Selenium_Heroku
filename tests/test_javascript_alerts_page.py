from pages.javascript_alerts_page import AlertsPage
from assertpy import assert_that
from time import sleep
from selenium.webdriver.common.keys import Keys


def test_alert_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_alert()
    alert_page.accept_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You successfully clicked an alert')


def test_confirm_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    alert_page.accept_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You clicked: Ok')


def test_confirm_dismiss(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    alert_page.cancel_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You clicked: Cancel')


def test_prompt_dismiss(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_prompt()
    alert_page.cancel_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You entered: null')


def test_prompt_accept_notext(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_prompt()
    alert_page.accept_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You entered:')


def test_prompt_accept_text(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_prompt()
    alert_page.insert_alert('test')
    alert_page.accept_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You entered: test')

