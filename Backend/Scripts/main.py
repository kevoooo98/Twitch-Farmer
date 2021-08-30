from TwitchWebDriver import TwitchWebDriver
import time

twd = TwitchWebDriver('https://twitch.tv')
twd.login()
time.sleep(10)
