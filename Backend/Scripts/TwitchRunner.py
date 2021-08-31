from TwitchWebDriver import TwitchWebDriver
import time


class TwitchRunner(TwitchWebDriver):

    def __init__(self):
        super().__init__()
        self.arg = arg

    #hier wird der nächste zu schauende stream aus der Datenbank ausgewählt
    def get_stream(self):
        #url aus db bekommen
        #url einsetzen
        pass

    #hier wird der Stream geschaut
    def watch_stream(self):
        #stream 1 minute schauen
        #1 minute von watchtime abziehen
        #gucken ob channelpoints da sind
        #wenn channelpoints da sind twitchwebdriver.farmchannelpoints
        pass

    def start (self):
        self.twd = TwitchWebDriver()
        selftwd.login()
        #get_stream()
