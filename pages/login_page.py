from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class LoginPage:

    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, 'radius')
    LOGIN_PAGE_SUBTITLE = (By.CSS_SELECTOR, 'h2')
    LONG_TEXT = (By.CLASS_NAME, 'subheader')
    FLASH_TEXT = (By.ID, 'flash-messages')
    IMAGE = (By.CSS_SELECTOR, '[alt="Fork me on GitHub"]')
    FLASH_LOGOUT_TEXT = (By.ID, 'flash')


    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, browser):
       self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def insert_password(self, password):
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def insert_username(self, username):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)

    def click_login(self):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(Keys.ENTER)
        #send_keys(Keys.CONTROL + "a")

    def login(self, username, password):
        self.insert_username(username)
        self.insert_password(password)
        self.click_login()

    def is_error_text_displayed(self):
        return self.browser.find_element(*self.FLASH_TEXT).is_displayed()

    def is_login_button_displayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()

    def is_login_subtitle_displayed(self):
        return self.browser.find_element(*self.LOGIN_PAGE_SUBTITLE).is_displayed()

    def is_long_text_displayed(self):
        return self.browser.find_element(*self.LONG_TEXT).is_displayed()

    def is_image_displayed(self):
        return self.browser.find_element(*self.IMAGE).is_displayed()

    def get_flash_message(self):
        return self.browser.find_element(*self.FLASH_TEXT).text

    def get_current_url(self):
        return self.browser.current_url

    def get_flash_logout_text(self):
        return self.browser.find_element(*self.FLASH_LOGOUT_TEXT).text