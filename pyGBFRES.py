# 批量下载GBF游戏资源
from queue import Queue
import os

import time
import threading
import urllib.request
import urllib.error
import datetime
import sys
sys.path.append(".")
import pyGBFchara as charadl
import pyGBFbg as bgdl
import pyGBFclass as classdl
import pyGBFsummon as summondl
import pyGBFweapon as weapondl

dirname = os.getcwd()
print_lock = threading.Lock()
data_q = Queue()
SAVELINK = False
DEBUG = False

MaxThread = 40

def mkdir(path):
    tmppath = os.getcwd()+"\\"+path
    try:
        os.makedirs(tmppath)

    except:
        pass
    return tmppath

def main():
    #socket.setdefaulttimeout(10)
    if(sys.version_info.major != 3):
        print("This script only works for python3")
        return

    start = time.time()
    try:
        print("download chara")
        charadl.main()
    except:
        pass

    try:
        print("download background")
        bgdl.main()
    except:
        pass

    try:
        print("download class/job")
        classdl.main()
    except:
        pass

    try:
        print("download summon stone")
        summondl.main()
    except:
        pass

    try:
        print("download weapon")
        weapondl.main()
    except:
        pass

    print("entire job took:", time.time()-start)



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