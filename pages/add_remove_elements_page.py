from selenium.webdriver.common.by import By


class AddRemoveElementsPage:
    TITLE_PAGE_TEXT = (By.CSS_SELECTOR, 'h3')
    ADD_BUTTON = (By.CSS_SELECTOR, '[onclick="addElement()"]')
    DELETE_BUTTON = (By.CLASS_NAME, 'added-manually')
    SELENIUM_LINK = (By.LINK_TEXT, 'Elemental Selenium')

    URL = 'https://the-internet.herokuapp.com/add_remove_elements/'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_page_text(self):
        return self.browser.find_element(*self.TITLE_PAGE_TEXT).text

    def click_add_element_button(self):
        self.browser.find_element(*self.ADD_BUTTON).click()

    def click_delete_button(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def is_add_button_displayed(self):
        return self.browser.find_element(*self.ADD_BUTTON).is_displayed()

    def is_delete_button_displayed(self):
        return self.browser.find_element(*self.DELETE_BUTTON).is_displayed()

    def is_link_displayed(self):
        return self.browser.find_element(*self.SELENIUM_LINK).is_displayed()

    def get_link_text(self):
        return self.browser.find_element(*self.SELENIUM_LINK).text

    def click_link(self):
        self.browser.find_element(*self.SELENIUM_LINK).click()
