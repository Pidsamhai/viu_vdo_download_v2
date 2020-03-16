# -*- coding: utf-8 -*-
from art import tprint
from bs4 import BeautifulSoup as bs
import requests as rs
import os,ctypes
from movie_model import Episode
from subprocess import Popen, CREATE_NEW_CONSOLE
import adremove
import debug
from movie_model import MovieHistory
from static_string import _VIU_BASE_URL
import historyManager as history
import movie_event as mv
from time import sleep

def mainmenu():
    print('     ##### MENU #####\n')
    print('     [h] Select from history')
    print('     [u] Enter new url ')
    print('     [e] Edit history ')
    print('     [E] Exit \n')

def main():
    while(True):
        os.system("cls")
        tprint("VIU    VDO    DOWNLOAD")
        print("     Version {}".format(debug.version()))
        print("     Build Date {}".format(debug.buildDate()))
        print("     License {}\n".format(debug.copyRight()))

        # init menu
        mainmenu()

        c = input('     : ')

        if(c == 'E'):
            break
        if(c == 'e'):
            history.editmenu()            
            
        if(c.lower() == 'h' or c.lower() == 'H'):

            while True:
                history.getInstance()
                m = history.show()
                if(m == False):
                    input("No record in history press any key ..............")
                    break
                h = mv.selectHistory(m)
                if(h is not False):
                    name,e = mv.fetchMovieAllEp(h.name,h)
                    if(name!=False and e != False):
                        while True:
                            mv.showAllEpisode(e)
                            ep = mv.selectEpisode(e)
                            if(ep is not False):
                                full_viu_url = mv.parsheUrl(_VIU_BASE_URL + ep.url)
                                ep_i = mv.getEpisodeInfo(name=ep.name,url=full_viu_url)
                                mv.showDlmenu(ep_i)
                            else:
                                break
                else:
                    break

        if(c.lower() == 'U' or c.lower() == 'u'):
            os.system("cls")
            tprint("VIU    VDO    DOWNLOAD")
            url = input("Enter url [Enter (e) to exit] : ")
            h = MovieHistory(name="",url=url)
            if(not url.lower() == "e" or not url.upper() == "E"):
                name,e = mv.fetchMovieAllEp("",h=h)
                if(name !=None and e != None):
                    if(not history.checkHistory(movieName=name)):
                        history.addNewHistory(moviename=name,url=url)
                    while True:
                        mv.showAllEpisode(e)
                        ep = mv.selectEpisode(e)
                        if(ep is not False):
                            full_viu_url = mv.parsheUrl(_VIU_BASE_URL + ep.url)
                            ep_i = mv.getEpisodeInfo(name=ep.name,url=full_viu_url)
                            mv.showDlmenu(ep_i)
                        else:
                            break


if __name__ == "__main__":
    import check_content_file 
    stat = True
    while stat:
        stat = check_content_file.check_file()
    main()
    os.system('cls')
    tprint('GOOD  BYE')
    sleep(1)