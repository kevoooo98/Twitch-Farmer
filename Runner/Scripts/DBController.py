import pymysql.cursors

class DBController():

    def __init__(self):
        pass


    def fetch_query(self, query):
        con = self.get_connection()
        with con:
            with con.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result

    def run_statement(self, query):
        con = self.get_connection()
        with con:
            with con.cursor() as cursor:
                cursor.execute(query)
            con.commit()

    def get_connection(self):
        return pymysql.connect(
            host='database',
            db = 'twitchfarm',
            user='dbuser', passwd='geheim1',
            cursorclass=pymysql.cursors.DictCursor
        )
