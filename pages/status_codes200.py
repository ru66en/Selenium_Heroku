from selenium.webdriver.common.by import By


class StatusCodes200:
    SUBTITLE_TEXT = (By.CSS_SELECTOR, 'h3')
    TEXT = (By.CSS_SELECTOR, 'div > p')
    LINK_HERE = (By.CSS_SELECTOR, '[href="/status_codes"]')

    URL = 'https://the-internet.herokuapp.com/status_codes/200'


    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def is_text_displayed(self):
        return self.browser.find_element(*self.TEXT).is_displayed()

    def click_link_here(self):
        self.browser.find_element(*self.LINK_HERE).click()

    def current_url(self):
        return self.browser.current_url

