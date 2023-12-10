from chromeWebDriver import chromeWebDriver
from selenium.webdriver.common.action_chains import ActionChains
import pyotp
import time
import os

class TwitchWebDriver(chromeWebDriver):

    __uname = os.environ.get('USER')
    __pass = os.environ.get('PASS')
    __totp_key = os.environ.get('2FA_KEY')
    __first_i_field = '.ScInputBase-sc-vu8u7d-0'
    __second_i_field = '.ScInput-sc-29xfhag-0'
    __2fa_i_field = ''
    __2FA_submit_field = '.gDHEzq'
    __conf_login_btn = '.eyrwSW'
    __login_btn = ".//button[@data-a-target='login-button']"
    __channel_status_indicator = "//div[@class='Layout-sc-nxg1ff-0 fkQgeT']"
    __channel_points_btn = '.fERWGf'
    __mature_button = '.euIPFy'

    def __init__(self):
        super().__init__()
        super().set_url('https://twitch.tv')

    def login (self):
        if (super().field_exists_by_xpath(self.__login_btn)):
            super().click_field_by_xpath(self.__login_btn)
            time.sleep(5)

            super().click_field(self.__first_i_field)
            time.sleep(0.2)
            super().input_field(self.__first_i_field, self.__uname)
            time.sleep(4)

            super().click_field(self.__second_i_field)
            time.sleep(0.2)
            super().input_field(self.__second_i_field, self.__pass)
            time.sleep(4)

            super().click_field(self.__conf_login_btn)
            time.sleep(60)

            totp = pyotp.TOTP(self.__totp_key)
            super().click_field(self.__first_i_field)
            time.sleep(2)
            super().input_field(self.__first_i_field, totp.now())
            super().click_field(self.__2FA_submit_field)
            time.sleep(12)

    def farm_channelpoints(self):
        if super().field_exists(self.__channel_points_btn):
            super().click_field(self.__channel_points_btn)

    def is_live(self):
        return super().field_exists_by_xpath(self.__channel_status_indicator)

    def confirm_maturity(self):
        if super().field_exists(self.__mature_button):
            super().click_field(self.__mature_button)
