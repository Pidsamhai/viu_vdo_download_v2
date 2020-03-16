import hashlib
import urllib.request
from static_string import _FFMPEG_PATH as _FFMPEG_FULL_PATH
from tqdm import tqdm
import os,time

_FFMPEG_DL_PATH = os.getcwd()+"\\ffmpeg\\ffmpeg.exe"
_FFMPEG_PATH = "./ffmpeg/"

ffmpeg_url = "https://raw.githubusercontent.com/Pidsamhai/viu_vdo_download/master/ffmpeg.exe"
original_ffmpeg_md5 = "dbc422ac98c4b8260c9882465254a232"


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    if(not os.path.isdir(_FFMPEG_PATH)):
        os.makedirs(_FFMPEG_PATH)
    with DownloadProgressBar(unit='B',
                             unit_scale=True,
                             miniters=1,
                             desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url,
                                   filename=output_path,
                                   reporthook=t.update_to)


def md5_chk(f):
    hasher = hashlib.md5()
    a = open(f, 'rb')
    buff = a.read()
    md5 = hasher.update(buff)
    return hasher.hexdigest()


def check_file():
    print("Check content file...")
    if(not os.path.isfile(_FFMPEG_FULL_PATH)):
        print("ffmpeg.exe not found")
        print("download ffmpeg please wait...\n")
        download_url(ffmpeg_url,_FFMPEG_DL_PATH)
    elif(os.path.exists(_FFMPEG_FULL_PATH)):
        if(md5_chk(_FFMPEG_FULL_PATH) != original_ffmpeg_md5):
            print("download ffmpeg please wait...\n")
            download_url(ffmpeg_url,_FFMPEG_DL_PATH)
    else:
        print("Check complete")
        time.sleep(0.5)
        return False