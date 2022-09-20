from selenium.webdriver.common.by import By

class SecurePage:

    WELCOME_TEXT = (By.CSS_SELECTOR, 'h4')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[class="button secondary radius"]')
    FLASH_TEXT = (By. ID, 'flash')


    URL = "https://the-internet.herokuapp.com/secure"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_welcome_message(self):
        return self.browser.find_element(*self.WELCOME_TEXT).text

    def click_logout(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click()

    def is_flash_text_displayed(self):
        return self.browser.find_element(*self.FLASH_TEXT).is_displayed()