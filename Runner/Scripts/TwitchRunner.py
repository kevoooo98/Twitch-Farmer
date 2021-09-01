from TwitchWebDriver import TwitchWebDriver
from DBController import DBController
import time


class TwitchRunner(TwitchWebDriver):

    __get_stream_query = 'SELECT * FROM streams ORDER BY watchtime desc;'

    def __init__(self):
        super().__init__()

    #hier wird der nächste zu schauende stream aus der Datenbank ausgewählt
    def get_stream(self):
        #url aus db bekommen
        #url einsetzen
        pass

    #hier wird der Stream geschaut
    def watch_stream(self, streamdata):
        #stream 1 minute schauen
        #1 minute von watchtime abziehen
        #gucken ob channelpoints da sind
        #wenn channelpoints da sind twitchwebdriver.farmchannelpoints
        pass

    def start (self):
        super().login()
        self.get_stream()
