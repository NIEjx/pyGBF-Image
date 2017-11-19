# 批量下载GBF武器立绘
from queue import Queue
import os

import time
import threading
import urllib.request
import urllib.error
import datetime
import sys

dirname = os.getcwd()
print_lock = threading.Lock()
data_q = Queue()
SAVELINK = False
DEBUG = False

def saveImg(url,dir):
        imgName = url.split('/')[-1]
        #dir = dirname+"\\"+groupdir[imgData.groupid]
        print("downloading:"+imgName)
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
            }
            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request)
            img = response.read()

            if(os.path.isfile(dir + "\\" + imgName) == False):
                with open(dir+"\\"+imgName,'wb') as file:
                    file.write(img)
            else:
                pass
            return True
        except OSError as err:
            print("not exist!")
            with open(dir+"\\err.txt","a",encoding='utf-8') as errfile:
                errstr = "error:"+ url +" not exist\n"
                if(DEBUG):
                    errstr += "  err " + str(format(err)) + "\n"
                errfile.write(errstr)
            pass
            return False

def main():
    print("hello")


if __name__ == '__main__':
  main()
  os.system("pause")

#appendix
#image set
#character origin zoom
#skin
#3710001000
# http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/zoom/3040010000_01.png
#http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/b/3030007000_01.png
#class
#http://game-a1.granbluefantasy.jp/assets/img/sp/assets/leader/job_change/120001_wa_1_01.png
#http://game-a1.granbluefantasy.jp/assets/img/sp/cjs/job_release_180001_1_c.png
#quest character 2 3 4 99
#http://game-a1.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3040022000.png
#summon 1 2 3 4
#http://game-a.granbluefantasy.jp/assets/img/sp/assets/summon/b/2030011000.png
#mypage class&sr
#http://game-a1.granbluefantasy.jp/assets/img/sp/assets/npc/my/3040058000_02.png
#http://game-a1.granbluefantasy.jp/assets/img/sp/assets/leader/my/140201_kn_1_01.png
#not used
#http://game-a1.granbluefantasy.jp/assets/img/sp/assets/npc/npc_evolution/main/3040071000_02.png