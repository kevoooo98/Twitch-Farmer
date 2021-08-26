from chromeWebDriver import chromeWebDriver
import pyotp
import time

class TwitchWebDriver(chromeWebDriver):

    __uname = 'kevoooo98'
    __pass = 'H3nni33!!'
    __uname_field = '.XFvNK'
    __pass_field = '.jsFUlW'
    __2FA_field = '.XFvNK'
    __2FA_submit_field = '.gDHEzq'
    __conf_login_btn = '.eyrwSW'
    __login_btn = '.cAHINR'


    def __init__(self, url):
        super().__init__()
        super().set_url(url)

    def login (self):
        super().click_field(self.__login_btn)
        time.sleep(3)
        
        super().input_field(self.__uname_field, self.__uname)
        time.sleep(3)

        super().input_field(self.__pass_field, self.__pass)
        time.sleep(3)

        super().click_field(self.__conf_login_btn)
        time.sleep(3)

        totp = pyotp.TOTP('M2HWAU3U3MJMEBF52PGLXPQYKGKFSA267JUAZMBAOIBSMSE4OGVQ')
        super().input_field(self.__2FA_field, totp.now())
        super().click_field(self.__2FA_submit_field)
