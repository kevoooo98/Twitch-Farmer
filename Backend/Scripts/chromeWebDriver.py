from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class chromeWebDriver():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def set_url (self, url):
        self.driver.get(url)

    def input_field (self, css_field, input):
        field = self.driver.find_element_by_css_selector(css_field)
        field.send_keys(input)

    def click_field (self, css_field):
        field = self.driver.find_element_by_css_selector(css_field)
        field.click()
