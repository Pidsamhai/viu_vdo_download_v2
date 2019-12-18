import sqlite3 as sqlite
import os
from lib import debug
from lib import movie_model as md

_DATABASE_NAME = "movie_history"
_DATABASE_FILE_NAME = "movie.db"
_DATABASE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..',
                 ".history/{}".format(_DATABASE_FILE_NAME)))
_DEBUG = debug.debug()

# intitial database


def getInstance():
    sql = """
    CREATE TABLE IF NOT EXISTS {0} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        url TEXT
    )""".format(_DATABASE_NAME)
    # check database is exist
    if (not os.path.exists(_DATABASE_PATH)):
        f = open(_DATABASE_PATH, "w+")
        debug("create file")
    else:
        debug("file is exist")
    # open data base
    conn = sqlite.connect(_DATABASE_PATH)
    c = conn.cursor()
    # execute sql create table
    c.execute(sql)
    conn.close()


def show():
    print("HISTORY : \n")
    conn = sqlite.connect(_DATABASE_PATH)
    c = conn.cursor()
    #print(list(c.execute("SELECT * FROM {}".format(_DATABASE_NAME))))
    movie_histry = []
    for index,k in enumerate(c.execute("SELECT * FROM {}".format(_DATABASE_NAME)),1):
         print("[{0}] {1}".format(index,k[1]))
         name = k[1]
         url = k[2]
         m = md.MovieHistory(name=name,url=url)
         movie_histry.append(m)
    conn.close()
    print("\n")
    return movie_histry
    


# return boolean
# param string Movie name & url
def checkHistory(movieName):
    sql = "SELECT * FROM {0} WHERE name = '{1}'".format(
        _DATABASE_NAME, movieName)
    conn = sqlite.connect(_DATABASE_PATH)
    c = conn.cursor()
    if len(c.execute(sql).fetchall()) == 0:
        conn.close()
        return False
    else:
        conn.close()
        return True


# return boolean
# param string Movie name & url


def addNewHistory(moviename, url):
    c = input("You want to add {} to history [y/n] : ".format(moviename))
    if (c.lower() == 'yes' or c.lower() == 'y'):
        sql = "INSERT INTO {table} (name, url) VALUES ('{name}','{url}')".format(
            table=_DATABASE_NAME, name=moviename, url=url)
        debug(sql)
        conn = sqlite.connect(_DATABASE_PATH)
        conn.cursor().execute(sql)
        conn.commit()
        conn.close()
    else:
        debug("NO")


def debug(any):
    if _DEBUG:
        print("{}".format(any))
