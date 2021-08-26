from chromeWebDriver import chromeWebDriver
import pyotp
import time

class TwitchWebDriver(chromeWebDriver):

    __uname = 'kevoooo98'
    __totp_key = 'M2HWAU3U3MJMEBF52PGLXPQYKGKFSA267JUAZMBAOIBSMSE4OGVQ'
    __first_i_field = '.XFvNK'
    __second_i_field = '.jsFUlW'
    __2FA_submit_field = '.gDHEzq'
    __conf_login_btn = '.eyrwSW'
    __login_btn = '.cAHINR'


    def __init__(self):
        super().__init__()
        super().set_url('https://twitch.tv')

    def login (self):
        super().click_field(self.__login_btn)
        time.sleep(3)

        super().input_field(self.__first_i_field, self.__uname)
        time.sleep(3)

        super().input_field(self.__second_i_field, self.__pass)
        time.sleep(3)

        super().click_field(self.__conf_login_btn)
        time.sleep(3)

        totp = pyotp.TOTP(self.__totp_key)
        super().input_field(self.__first_i_field, totp.now())
        super().click_field(self.__2FA_submit_field)

    def farm_channelpoints(self):
        pass
