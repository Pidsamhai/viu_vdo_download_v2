# -*- coding: utf-8 -*-
from art import tprint
from bs4 import BeautifulSoup as bs
import requests as rs
import os,ctypes
from movie_model import Episode
from subprocess import Popen, CREATE_NEW_CONSOLE
import adremove
from static_string import _VIU_BASE_URL
import historyManager as history
import movie_event as mv


def main():
    while(True):
        os.system("cls")
        tprint("VIU    VDO    DOWNLOAD")
        c = input('Select from history [h] , Input new url [u] : ')
        if(c.lower() == 'h' or c.lower() == 'H'):

            while True:
                history.getInstance()
                m = history.show()
                if(m == False):
                    input("No record in history press any key ..............")
                    break
                h_name,h_url = mv.selectHistory(m)
                if(h_name is not False and h_url is not False):
                    name,e = mv.fetchMovieAllEp(h_name,h_url)
                    if(name !=None and e != None):
                        while True:
                            mv.showAllEpisode(e)
                            e_name,e_url = mv.selectEpisode(e)
                            if(e_name is not False and e_url is not False):
                                full_viu_url = mv.parsheUrl(_VIU_BASE_URL + e_url)
                                ep_i = mv.getEpisodeInfo(name=e_name,url=full_viu_url)
                                mv.showDlmenu(ep_i)
                            else:
                                break
                else:
                    break

        if(c.lower() == 'U' or c.lower() == 'u'):

            os.system("cls")
            tprint("VIU    VDO    DOWNLOAD")
            url = input("Enter url [Enter (e) to exit] : ")
            if(not url.lower() == "e" or not url.upper() == "E"):
                name,e = mv.fetchMovieAllEp("",url=url)
                if(name !=None and e != None):
                    if(not history.checkHistory(movieName=name)):
                        history.addNewHistory(moviename=name,url=url)
                    while True:
                        mv.showAllEpisode(e)
                        e_name,e_url = mv.selectEpisode(e)
                        if(e_name is not False and e_url is not False):
                                    full_viu_url = mv.parsheUrl(_VIU_BASE_URL + e_url)
                                    ep_i = mv.getEpisodeInfo(name=e_name,url=full_viu_url)
                                    mv.showDlmenu(ep_i)
                        else:
                            break


if __name__ == "__main__":
    main()
    os.system('cls')
    tprint('GOOD  BYE')