from selenium.webdriver.common.by import By


class AddRemoveElementsPage:

    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, '[onclick="addElement()"]')
    DELETE_BUTTON = (By.CLASS_NAME, "added-manually")
    TITLE_PAGE = (By.CSS_SELECTOR, "h3")
    LINK = (By.LINK_TEXT, 'Elemental Selenium')


    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_add_button(self):
        self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()

    def click_delete_button(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def get_number_of_delete_button(self):
        return len(self.browser.find_elements(*self.DELETE_BUTTON))

    def click_first_delete_button(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def is_add_button_displayed(self):
        return self.browser.find_element(*self.ADD_ELEMENT_BUTTON).is_displayed()

    def is_delete_button_displayed(self):
        return self.browser.find_element(*self.DELETE_BUTTON).is_displayed()

    def get_title_page(self):
        return self.browser.find_element(*self.TITLE_PAGE).text

    def is_link_displayed(self):
        return self.browser.find_element(*self.LINK).is_displayed()

    def click_link(self):
        self.browser.find_element(*self.LINK).click()