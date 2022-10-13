from selenium.webdriver.common.by import By


class StatusCodes:
    LINK_200 = (By.CSS_SELECTOR, '[href="status_codes/200"]')
    LINK_301 = (By.CSS_SELECTOR, '[href="status_codes/301"]')
    LINK_404 = (By.CSS_SELECTOR, '[href="status_codes/404"]')
    LINK_500 = (By.CSS_SELECTOR, '[href="status_codes/500"]')
    SUBTITLE_TEXT = (By.CSS_SELECTOR, 'h3')
    TEXT = (By.CSS_SELECTOR, 'div > p:nth-child(2)')
    LINK_HERE = (By.CSS_SELECTOR, '[href="http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml"]')


    URL = 'https://the-internet.herokuapp.com/status_codes'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_link200(self):
        self.browser.find_element(*self.LINK_200).click()

    def click_link301(self):
        self.browser.find_element(*self.LINK_301).click()

    def click_link404(self):
        self.browser.find_element(*self.LINK_404).click()

    def click_link500(self):
        self.browser.find_element(*self.LINK_500).click()

    def get_subtitle_text(self):
        return self.browser.find_element(*self.SUBTITLE_TEXT).text

    def is_text_displayed(self):
        return self.browser.find_element(*self.TEXT).is_displayed()

    def click_link_here(self):
        self.browser.find_element(*self.LINK_HERE).click()

    def current_url(self):
        return self.browser.current_url

    def is_200_displayed(self):
        return self.browser.find_element(*self.LINK_200).is_displayed()

    def is_301_displayed(self):
        return self.browser.find_element(*self.LINK_301).is_displayed()

    def is_404_displayed(self):
        return self.browser.find_element(*self.LINK_404).is_displayed()

    def is_500_displayed(self):
        return self.browser.find_element(*self.LINK_500).is_displayed()



