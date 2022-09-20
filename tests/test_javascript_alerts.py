from pages.javascript_alerts_page import AlertsPage
from assertpy import assert_that
from time import sleep


def test_alert_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_alert()
    sleep(2)
    alert_page.accept_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You successfully clicked an alert')
    sleep(5)


def test_confirm_accept(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_confirm()
    sleep(2)
    alert_page.accept_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You clicked: Ok')
    sleep(3)


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
    sleep(2)
    alert_page.accept_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You entered:')
    sleep(3)


def test_prompt_accept_text(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_prompt()
    alert_page.insert_alert('Java Alerts')
    alert_page.accept_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You entered: Java Alerts')

def test_prompt_accept_mytext(browser):
    alert_page = AlertsPage(browser)
    alert_page.load_page()
    alert_page.open_prompt()
    sleep(2)
    alert_page.accept_alert()
    assert_that(alert_page.get_alert_result()).is_equal_to('You entered:')
    sleep(3)