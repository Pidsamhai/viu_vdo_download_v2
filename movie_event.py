import removeAds as ads
from bs4 import BeautifulSoup as bs
from movie_model import Episode, Movie
import debug as de
from static_string import _ADS_BLOCK_PATH, _LANG, _LANG_E, _VDO_PATH, _SUBTITLE_PATH, _GRAB_VDO_BASE_URL, _FFMPEG_PATH
import requests as rs
from subprocess import Popen, CREATE_NEW_CONSOLE, CREATE_NEW_PROCESS_GROUP
import subprocess
import os
from art import tprint


def selectHistory(m=""):
    i = ''
    while True:
        try:
            i = int(input("Select movie [number] [Enter (0) to Main menu]: "))
        except ValueError:
            continue
        if i >= 0 and i <= len(m):
            break
    return (m[i - 1].name, m[i - 1].url) if i != 0 else (False, False)


def selectEpisode(e=""):
    print("\n")
    i = ''
    while True:
        try:
            i = int(input("Select Episode [number] [back enter (0) ] : "))
        except ValueError:
            continue
        if (i >= 0 and i <= len(e)):
            break
    return (e[i - 1].name, e[i - 1].url) if i != 0 else (False, False)


def fetchMovieAllEp(name = "", url=""):
    print("\n")
    episode = []
    try:     
        html = ads.removeAds(url, _ADS_BLOCK_PATH)
    except Exception:
        input("Url Error ........")
        return None, None
    s = bs(html, "html.parser")
    title = s.find("title")
    name = str(title.string).split('｜')[0].strip()
    #debug(name)
    for ultag in s.find_all('ul',
                            {'class': 'video-alllist clearfix common-panel'}):
        for litag in ultag.find_all('li'):
            for a in litag.find_all('a'):
                title_name = a['title'].replace('ตอนที่', "EP")
                title_name = title_name.replace('Watch Online on Viu', "")
                e = Episode(name=title_name, url=a['href'])
                episode.append(e)
    if(len(episode) != 0):
        return name,episode[::-1]  # revert sort asc defore desc
    else:
        input("No Data .......")
        return None , None


def showAllEpisode(e):
    os.system("cls")
    tprint("VIU    VDO    DOWNLOAD")
    for index, ep in enumerate(e, 1):
        print("[{0}] {1}".format(index, ep.name))


def getEpisodeInfo(name, url):
    response = ads.removeAds(url, _ADS_BLOCK_PATH)
    subtitle = []
    episode = Movie()
    episode.epName = name
    s = bs(response, "html.parser")
    for tbody in s.find_all('tbody'):
        for tr in tbody.find_all('tr'):
            for td in tr.find_all('td'):
                if (td.text == 'ffmpeg code'):  #get FFmpeg code
                    print("GET ffmpeg...", end="\r")
                    ffmpeg_url = td.find('a')
                    ffmpeg_html = ads.removeAds(ffmpeg_url['href'],
                                                _ADS_BLOCK_PATH)
                    ff = bs(ffmpeg_html, "html.parser")
                    ffmpeg_dl_url = ff.find('code').text
                    episode.dl_url = ffmpeg_dl_url
                    #debug(ffmpeg_dl_url)
                    print("GET ffmpeg......OK")
                # get subtitle
                if (td.text.strip() in _LANG):
                    index = _LANG.index(td.text.strip())
                    print("GET {} Subtitle Url...".format(_LANG_E[index]),
                          end="\r")
                    for a in tr.find_all('a'):
                        lang_title = _LANG_E[index] if a['href'].find(
                            "vtt?") >= 0 else _LANG_E[index] + " vtt"
                        subtitle.append((lang_title, a['href']))
    episode.subtitle = subtitle
    #debug("SUB =>{}".format(len(set(subtitle))))
    return episode


def dlVdo(command, ep_name):
    print("INFO => ", (not os.path.exists(_VDO_PATH)))
    if not os.path.exists(_VDO_PATH):
        print(os.makedirs(_VDO_PATH))
    command = command.replace("ffmpeg", "")
    command = command.split(" ")
    news = _VDO_PATH + "\\" + command[len(command) - 1].replace('"', '')
    news = '"{}"'.format(news)
    command[len(command) - 1] = news
    command = " ".join(command)
    path = os.path.dirname(os.path.realpath(__file__)) + '\\ffmpeg\\ffmpeg.exe'
    p1 = subprocess.Popen(_FFMPEG_PATH + command,
                          creationflags=CREATE_NEW_CONSOLE)  #Popen('ls')


def dlSub(url, file_name, lang, extension):
    file_name = file_name.replace(':', '')
    if not os.path.exists(_SUBTITLE_PATH):
        os.makedirs(_SUBTITLE_PATH)
    with open(
            "{}/{}({}).{}".format(_SUBTITLE_PATH, file_name, lang, extension),
            "wb") as file:
        response = rs.get(url)
        #print(response.text)
        file.write(response.content)
        file.close()


def showDlmenu(m: Movie):
    while (True):
        os.system('cls')
        tprint("Download        Menu")
        print(m.epName + "\n")
        print("1 Download Vdo only")
        print("2 Download Subtitle only")
        print("3 Download Vdo and Subtitle")
        print("4 Exit To Episode Select")
        c = ''
        while True:
            try:
                c = int(input(" : "))
            except ValueError:
                continue
            if (c >= 0 and c <= 4):
                break
        if c == 1:
            dlVdo(m.dl_url, m.epName)
        if c == 2:
            os.system('cls')
            print("Select Langauge\n")
            for i, j in enumerate(m.subtitle, start=1):
                print(i, j[0])
            print("{} Down load all".format(len(m.subtitle) + 1))
        if(c == 4):
            break
            idx = ''
            while True:
                try:
                    idx = int(input(" : "))
                except ValueError:
                    continue
                if (idx >= 0 and idx <= len(m.subtitle) + 1):
                    break
            if (idx != 0 and idx < len(m.subtitle) + 1):
                dlSub(
                    url=m.subtitle[idx - 1][1], file_name= m.epName,lang= m.subtitle[idx - 1][0],
                    extension= "srt" if m.subtitle[idx - 1][0].find('vtt') != -1 else "vtt")
            if(idx == len(m.subtitle) + 1):
                for i in range(idx):
                   dlSub(
                    url= m.subtitle[i - 1][1],file_name= m.epName,lang= m.subtitle[i - 1][0],
                    extension= "srt" if m.subtitle[i - 1][0].find('vtt') != -1 else "vtt")


def parsheUrl(url):
    url = url.replace("/", "%2F")
    url = url.replace(":", "%3A")
    return _GRAB_VDO_BASE_URL + url


def debug(any):
    if de.debug:
        print("{}".format(any))