from art import tprint
from bs4 import BeautifulSoup as bs
import requests as rs
import os,ctypes
from subprocess import Popen, CREATE_NEW_CONSOLE
from lib import removeAds 
from lib import static_string as st
from lib import historyManager as history
from lib import movie_event as mv


def main():
    while(True):
        c = input('Select from history [h] , Input new url [u] : ')
        if(c.lower() == 'h' or c.lower() == 'H'):
            while True:
                history.getInstance()
                m = history.show()
                h_name,h_url = mv.selectHistory(m)
                if(h_name is not False and h_url is not False):
                    e = mv.fetchMovieAllEp(h_name,h_url)
                    mv.showAllEpisode(e)
                    e_name,e_url = mv.selectEpisode(e)
                    if(e_name is not False and e_url is not False):
                        pass 
        if(c.lower() == 'U' or c.lower() == 'u'):
            pass
    
    # if(not history.checkHistory("FUCK")):
    #     history.addNewHistory("FUCK","Hello")

if __name__ == "__main__":
    #os.system("cls")
    tprint("VIU    VDO    DOWNLOAD")
    main()
    #os.system('cls')
    tprint('GOOD  BYE')