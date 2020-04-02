import sqlite3 as sqlite
import os
from art import tprint
import debug as debug
from movie_model import MovieHistory

from static_string import _DATABASE_FILE_NAME,_DATABASE_NAME,_DATABASE_PATH


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
    os.system("cls")
    tprint("History     Select")
    conn = sqlite.connect(_DATABASE_PATH)
    c = conn.cursor()
    #print(list(c.execute("SELECT * FROM {}".format(_DATABASE_NAME))))
    movie_histry = []
    for index,k in enumerate(c.execute("SELECT * FROM {}".format(_DATABASE_NAME)),1):
         print("[{0}] {1}".format(index,k[1]))
         name = k[1]
         url = k[2]
         pk = k[0]
         m = MovieHistory()
         m.name = name
         m.url = url
         m.primarykey = pk
         movie_histry.append(m)
    conn.close()
    print("\n")
    return movie_histry if len(movie_histry) > 0 else False

# return boolean
# param string Movie name & url
def checkHistory(movieName):
    try:
        print("Check movie in history ...\n")
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
    except Exception as e:
        getInstance()

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
        print("Added {} to history\n".format(moviename))
    else:
        print("Cancel ...\n")
        debug("NO")

def upDateHistory(moviename, url,oldname,pk):
    c = input("You want to update {} to {} [y/n] : ".format(oldname,moviename))
    if (c.lower() == 'yes' or c.lower() == 'y'):
        sql = "UPDATE {table} SET name = '{name}',url = '{url}' WHERE id = '{pk}'".format(
            table=_DATABASE_NAME, name=moviename, url=url,pk=pk)
        debug(sql)
        conn = sqlite.connect(_DATABASE_PATH)
        conn.cursor().execute(sql)
        conn.commit()
        conn.close()
        print("Update {} to history\n".format(moviename))
    else:
        print("Cancel ...\n")
        #debug("NO")

def deleteHistory(moviename,moviename_pk):
    c = input("You want to detele {} from history [y/n] : ".format(moviename))
    if (c.lower() == 'yes' or c.lower() == 'y'):
        sql = "DELETE FROM {table}  WHERE id = '{id}'".format(
            table=_DATABASE_NAME, id=moviename_pk)
        debug(sql)
        conn = sqlite.connect(_DATABASE_PATH)
        conn.cursor().execute(sql)
        conn.commit()
        conn.close()
        print("Delete {} from history\n".format(moviename))
    else:
        print("Cancel ...\n")
        #debug("NO")


def selectHistory(m:list):
    i = ''
    while True:
        try:
            i = int(input("Select movie [number] [Enter (0) to Main menu]: "))
        except ValueError:
            continue
        if i >= 0 and i <= len(m):
            break
    return m[i - 1] if i != 0 else False

def edit_submenu(e:MovieHistory):
    os.system("cls")
    print(e.name+"\n")
    print("[e] Edit")
    print("[d] Delete")
    print("[E] Exit")
    c = input(": ")
    if(c == "E"): 
        return
    if(c.lower() == "e"):
        name = input("Enter name [default  {}] : ".format(e.name))
        if(name == None or name == ''):
            name = e.name
        print(name)
        url = input("Enter url [default  {}] : ".format(e.url))
        if(url == None or url == ''):
            url = e.url
        upDateHistory(name,url,e.name,e.primarykey)
    if(c.lower() == "d"):
        deleteHistory(e.name,e.primarykey)


def editmenu():
    while(True):
        os.system('cls')
        tprint("History Editter")
        m = show()
        if(m != False):
            h = selectHistory(m)
            if(h != False):
                edit_submenu(h)
            else:
                break

def debug(any):
    if _DEBUG:
        print("{}".format(any))
