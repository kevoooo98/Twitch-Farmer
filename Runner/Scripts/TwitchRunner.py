from TwitchWebDriver import TwitchWebDriver
from DBController import DBController
import time

class TwitchRunner(TwitchWebDriver):

    __get_stream_query = 'SELECT * FROM streams ORDER BY watchtime desc;'
    __update_watchtime = 'UPDATE streams SET watchtime = %d WHERE ID_Stream = %d ;'
    __delete_stream = 'DELETE FROM streams WHERE ID_Stream = %d ;'

    def __init__(self):
        super().__init__()
        self.dbc = DBController()

    #hier wird der nächste zu schauende stream aus der Datenbank ausgewählt
    def get_stream(self):
        streams = self.dbc.fetch_query(self.__get_stream_query)
        if streams:
            for stream in streams:
                super().set_url(stream['url'])
                if super().is_live():
                    super().confirm_maturity()
                    self.watched_time = 0
                    self.watch_stream(stream)
            print('all streams watched')
            time.sleep(10)
        else:
            time.sleep(60)

        self.get_stream()


    #hier wird der Stream geschaut
    def watch_stream(self, streamdata):
        for i in range(12):
            super().farm_channelpoints()
            time.sleep(5)
        streamdata['watchtime'] = streamdata['watchtime']-1
        self.watched_time = self.watched_time+1

        if streamdata['watchtime'] <= 0 and streamdata['fav'] != b'\x01':
            self.delete_stream(streamdata)
        elif not(super().is_live()) or super().get_current_url() != streamdata['url'] or (self.watched_time == 15 and streamdata['fav'] != b'\x01'):
            self.update_streamdata(streamdata)
        elif self.watched_time == 15 and streamdata['fav'] == b'\x01':
            pass
        else:
            self.watch_stream(streamdata)

    def update_streamdata(self,streamdata):
        stmnt = (self.__update_watchtime %(streamdata['watchtime'], streamdata['ID_Stream']))
        print(stmnt)
        self.dbc.run_statement(stmnt)

    def delete_stream(self,streamdata):
        stmnt = (self.__delete_stream %(streamdata['ID_Stream']))
        self.dbc.run_statement(stmnt)

    def start (self):
        super().login()
        self.get_stream()
