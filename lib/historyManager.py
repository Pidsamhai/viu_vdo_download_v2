import sqlite3 as sqlite
import os

_DATABASE_NAME = "movie_history"
_DATABASE_FILE_NAME = "movie.db"
_DATABASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'..',".history/{}".format(_DATABASE_FILE_NAME)))
_DEBUG = True

# intitial database
def getInstance():
    sql = """
    CREATE TABLE IF NOT EXISTS {0} ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        url TEXT
    )""".format(_DATABASE_NAME)
    debug(sql)
    # check database is exist
    if(not os.path.exists(_DATABASE_PATH)):
        f = open(_DATABASE_PATH,"w+")
        debug("create file")
    else:
        debug("file is exist")
    # open data base
    conn = sqlite.connect(_DATABASE_PATH)
    c = conn.cursor()
    # execute sql create table
    c.execute(sql)
    conn.close()

# return boolean
# param string Movie name & url
def checkHistory(movieName):
    sql = "SELECT * FROM {0} WHERE name = '{1}'".format(_DATABASE_NAME,movieName)
    conn = sqlite.connect(_DATABASE_PATH)
    c = conn.cursor()
    if len(c.execute(sql).fetchall()) == 0:
        debug("not fond")

# return boolean
# param string Movie name & url
def addNewHistory(moviename):
    pass

def debug(any):
    if _DEBUG :
        print("{}".format(any))