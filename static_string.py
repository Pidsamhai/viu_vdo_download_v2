import os
_GRAB_VDO_BASE_URL = 'https://www.grabvdo.com/?url='
_VIU_BASE_URL = "https://www.viu.com"
_BASE_FFMPEG_URL = "https://www.grabvdo.com"

## langauge
_ORIGINAL_FFMPEG_MD5 = "dbc422ac98c4b8260c9882465254a232"
_LANG = ['简体中文','English','繁體中文','Indo','ภาษาไทย']
_LANG_E = ['Simplified Chinese','English','traditional Chinese','Indo','Thai']

_CONTENT_PATH = os.getcwd() + "\\.content\\"
_CACHE_PATH = os.getcwd() + "\\.cache\\"

_CACHE_FILE_PATH = _CACHE_PATH + 'update.zip'

_DATABASE_NAME = "movie_history"
_DATABASE_FILE_NAME = "movie.db"
_DATABASE_PATH =  _CONTENT_PATH + _DATABASE_FILE_NAME


_ADS_BLOCK_FILE_NAME = "easylist-thailand.txt"
_FFMPEG_FILE_NAME = "ffmpeg.exe"

_ADS_BLOCK_PATH = _CONTENT_PATH +  _ADS_BLOCK_FILE_NAME
_FFMPEG_PATH = _CONTENT_PATH +  _FFMPEG_FILE_NAME

_VDO_PATH = "./output/"
_SUBTITLE_PATH = _VDO_PATH

# Content File
_ADS_BLOCK_URL = "https://adblock-thai.github.io/thai-ads-filter/subscription.txt"
_FFMPEG_URL = "https://raw.githubusercontent.com/Pidsamhai/viu_vdo_download/master/ffmpeg.exe"

# Github version Url