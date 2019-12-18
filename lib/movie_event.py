from lib import removeAds as ads
from bs4 import BeautifulSoup as bs
from lib import movie_model as md
import os
_ADS_BLOCK_NAME = "easylist-thailand.txt"
_ADS_BLOCK_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..',
                 "ads_block_content/{}".format(_ADS_BLOCK_NAME)))


def selectHistory(m=""):
    i = ''
    while True:
        try:
            i = int(input("Select movie [number] : "))
        except ValueError:
            continue
        if i >= 0 and i <= len(m): 
            break
    return (m[i - 1].name, m[i - 1].url) if i!= 0 else (False,False)


def selectEpisode(e=""):
    i = ''
    while True:
        try:
            i = int(input("Select Episode [number] [back enter (0) ] : "))
        except ValueError:
            continue
        if(i >= 0 and i <= len(e)):
            break
    return (e[i - 1].name, e[i - 1].url) if i != 0 else (False,False) 


def fetchMovieAllEp(name, url):
    episode = []
    html = ads.removeAds(url, _ADS_BLOCK_PATH)
    s = bs(html, "html.parser")
    for ultag in s.find_all('ul',
                            {'class': 'video-alllist clearfix common-panel'}):
        for litag in ultag.find_all('li'):
            for a in litag.find_all('a'):
                title_name = a['title'].replace('ตอนที่', "EP")
                title_name = title_name.replace('Watch Online on Viu', "")
                e = md.Episode(name=title_name, url=a['href'])
                episode.append(e)
    return episode[::-1]  # revert sort asc defore desc


def showAllEpisode(e):
    for ep in e:
        print(ep.name)