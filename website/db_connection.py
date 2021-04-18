import pymysql
from pymysql import cursors

def connect():
    try: 
        connect = pymysql.connect(
        user = 'root', password = 'tt156383', host = 'localhost', database = 'movieGenie', 
        )
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        return connect, cursor
    except:
        print('Could not connect to database')
        return None





