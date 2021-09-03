from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

class chromeWebDriver():

    def __init__(self):
        options = Options();
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def set_url (self, url):
        browser = self.driver.get(url)
        time.sleep(10)

    def get_current_url(self):
        return self.driver.current_url

    def input_field (self, css_field, input):
        field = self.get_field(css_field)
        field.send_keys(input)

    def click_field (self, css_field):
        field = self.get_field(css_field)
        field.click()

    def field_exists (self, css_field):
        try:
            self.get_field(css_field)
        except NoSuchElementException:
            return False
        return True

    def field_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def get_field (self, css_field):
        return self.driver.find_element_by_css_selector(css_field)
