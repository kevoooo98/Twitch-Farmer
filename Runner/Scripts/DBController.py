class DBController():

    def __init__(self):
        self.connection = MySQLdb.connect(
            host='127.0.0.1',
            db = 'twitchfarm',
            user='dbuser', passwd='geheim1'
        )
