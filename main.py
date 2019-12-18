from art import tprint
from bs4 import BeautifulSoup as bs
import requests as rs
import os,ctypes
from subprocess import Popen, CREATE_NEW_CONSOLE
from lib import removeAds 
from lib import static_string as st
from lib import historyManager as history


def main():
    history.getInstance()
    history.checkHistory("Araya")
    input("Input.....")

if __name__ == "__main__":
    os.system("cls")
    tprint("VIU    VDO    DOWNLOAD")
    main()
    os.system('cls')
    tprint('GOOD  BYE')