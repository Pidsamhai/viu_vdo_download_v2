import urllib.request,hashlib,os,time,json,zipfile,shutil
from static_string import _FFMPEG_PATH , _ADS_BLOCK_URL , _ADS_BLOCK_PATH, _ORIGINAL_FFMPEG_MD5, _FFMPEG_URL,_CONTENT_PATH,_CACHE_PATH,_CACHE_FILE_PATH
from debug import version
from tqdm import tqdm
from art import tprint

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

class CheckFileContent():

    def __check_content_path(self):
        if(not os.path.isdir(_CONTENT_PATH)):
            os.mkdir(_CONTENT_PATH)

    def __clean_cache_file(self):
        if(os.path.isdir(_CACHE_PATH)):
            print('Clean Cache...')
            shutil.rmtree(_CACHE_PATH)
            print('Clean cache success !')

    def __check_cache_path(self):
        if(not os.path.isdir(_CACHE_PATH)):
            os.mkdir(_CACHE_PATH)

    def __download_file(self,url, output_path,update = False):
        trycount = 0
        status = False
        if(update):
            self.__check_cache_path()
        else:
            self.__check_content_path()
        while trycount < 4:
            try:
                with DownloadProgressBar(unit='B',
                                        unit_scale=True,
                                        miniters=1,
                                        desc=url.split('/')[-1]) as t:
                    urllib.request.urlretrieve(url,
                                            filename=output_path,
                                            reporthook=t.update_to)
                trycount = 4
                status = True
            except Exception as e:
                print(e)
                trycount += 1
                continue
        return status

    def __adblock_current_version(self):
        f = open(_ADS_BLOCK_PATH,'r')
        data = f.readlines()
        for i in data:
            if i.find('! Version') != -1:
                return int(i.split(':')[1].strip())
        
    def __md5_chk(self,f):
        hasher = hashlib.md5()
        a = open(f, 'rb')
        buff = a.read()
        md5 = hasher.update(buff)
        return hasher.hexdigest()

    def __dl_ads_block(self):
        self.__download_file(_ADS_BLOCK_URL,_ADS_BLOCK_PATH)

    def __dl_ffmpeg(self):
        self.__download_file(_FFMPEG_URL,_FFMPEG_PATH)

    def __unzip_update(self):
        print("Extrac Zip...")
        with zipfile.ZipFile(_CACHE_FILE_PATH,'r') as zip_ref:
            zip_ref.extractall(_CACHE_PATH)
        path = os.getcwd()+"\\updateServices.exe updatefile"
        os.system('"{}"'.format(path))

    def __check_program_version(self):
        git_url = 'https://api.github.com/repos/Pidsamhai/viu_vdo_download_v2/releases'
        req = urllib.request.Request(git_url)
        req.add_header('Accept','application/vnd.github.v3+json')
        data = urllib.request.urlopen(req).read()
        data = data.decode('utf8')
        abc = json.loads(data)
        v = abc[0]['tag_name'] 
        url = abc[0]['assets'][0]['browser_download_url']
        chl = abc[0]['body']
        chl = str(chl).replace('\n','').split('\r')
        if(abc[0]['tag_name'] != version()):
            tprint('UPDATE')
            print('     Fond new version !')
            print('     Version',v)
            print('     Change log\n') 
            for i in chl: print("     {}".format(i))
            c = 0
            while True:
                try:
                    c = str(input('\nDownloading new version... [y,n] : '))
                    break
                except ValueError as e:
                    continue

            if(c.lower() == 'y' or c == ''):
                if(self.__download_file(url,_CACHE_FILE_PATH,True)):
                    self.__unzip_update()

    def __check_adblock_content_and_version(self):
        print('Check Adsblock file...')
        if(not os.path.isfile(_ADS_BLOCK_PATH)):
            print('Adsblock not Fond !')
            self.__dl_ads_block()
        else:
            print('Adsblock Fond !')
            print('Check New Version...')
            new = self.__fetch_adblock_version()
            current = self.__adblock_current_version()
            if(new > current):
                self.__dl_ads_block()
        print('Ckeck Adsblock Complete')
        time.sleep(0.5)

    def __fetch_adblock_version(self):
        data = urllib.request.urlopen(_ADS_BLOCK_URL)
        for i in data:
            i = i.decode('utf8')
            if i.find("! Version") != -1:
                return int(i.split(':')[1].strip())

    def __check_ffmpeg_file(self):
        print("Check FFMPEG file...")
        if(not os.path.isfile(_FFMPEG_PATH)):
            print("ffmpeg.exe not found")
            print("download ffmpeg please wait...\n")
            self.__dl_ffmpeg()
        else:
            if(self.__md5_chk(_FFMPEG_PATH) != _ORIGINAL_FFMPEG_MD5):
                print("Hash File Error !!")
                print("download ffmpeg please wait...\n")
                self.__dl_ffmpeg()
        print("Check FFMPEG complete")
        time.sleep(0.5)
    
    def check_file(self):
        self.__clean_cache_file()
        self.__check_program_version()
        self.__check_adblock_content_and_version()
        self.__check_ffmpeg_file()
        return False