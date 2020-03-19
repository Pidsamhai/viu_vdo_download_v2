import psutil,os,shutil

def main(url):
    flag = True 
    _CACHE_PATH = os.getcwd() + "\\.cache\\"
    while flag:
        for proc in psutil.process_iter():
            try:
                processName = proc.name()
                if(processName == 'main.exe'):
                    os.system('taskkill /f /im {}'.format(proc.name()))
                flag = False
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        else:
            pass

    print("Coppy File")

    try:
        shutil.copyfile(_CACHE_PATH + 'main.exe',os.getcwd()+'\\main.exe')
    except Exception as e:
        print(e)

    os.system(os.getcwd()+"\\main.exe")

if __name__ == "__main__":
    import sys
    url = sys.argv
    print(url[1])
    main(url)
    
