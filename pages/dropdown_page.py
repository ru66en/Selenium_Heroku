from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DropdownPage:
    SUBTITLE = (By.CSS_SELECTOR, 'h3')
    SELECT_OPTION = (By.ID, 'dropdown')
    GREEN_IMAGE = (By.CSS_SELECTOR, '[alt="Fork me on GitHub"]')

    URL = 'https://the-internet.herokuapp.com/dropdown'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_subtitle(self):
        return self.browser.find_element(*self.SUBTITLE).text

    def is_image_displayed(self):
        self.browser.find_element(*self.GREEN_IMAGE).is_displayed()

    def select_option(self, option):
        select_option = Select(self.browser.find_element(*self.SELECT_OPTION))
        select_option.select_by_visible_text(option)

    def is_value_selected(self, value):
        return self.browser.find_element(By.CSS_SELECTOR, f'[value="{value}"][selected="selected"]').is_displayed()





