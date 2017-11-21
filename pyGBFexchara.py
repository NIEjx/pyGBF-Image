# 批量下载GBF剧情任务编外半身立绘
from queue import Queue
import os

import time
import threading
import urllib.request
import urllib.error
import datetime
import sys
sys.path.append(".")
import pyDownload as download


dirname = os.getcwd()
print_lock = threading.Lock()
data_q = Queue()
SAVELINK = False
DEBUG = False

prefix1 = "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/"

groupstr = ["3040070000_unarmed",
            "3040070000_unarmed2",
            "3040070000_cockpit",
            "3040028000_cockpit"]
explist = ["","_joy","_think","_mood",
           "_laugh3","_laugh2","_laugh",
           "_eye","_mortifying","_surprise_fe",
           "_weak","_sad","_suddenly",
           "_surprise","_angry","_cutin",
           "_shy","_01","_02","_03"]
# chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover
groupdir = ["img\\quest\\exorder"]
grouplink = ["link\\quest-exo.txt"]

MaxThread = 40


def mkdir(path):
    tmppath = os.getcwd()+"\\"+path
    try:
        os.makedirs(tmppath)
    except:
        pass
    return tmppath

def saveIndex(imgData):
    time.sleep(0.1)
    with print_lock:
        for iexp in explist:
            dir = groupdir[0]
            count = 0
            try:
                url = prefix1 + imgData +iexp+ ".png"
                if(download.saveImg(url,dir)):
                    count+=1
                    if(SAVELINK):
                        #print(grouplink[imgData.groupid])
                        #print(imgData.url)
                        with open(grouplink[0],"a") as linkfile:
                            linkfile.write(url+"\n")
            except:
                pass

def worker():
    while True:
        imgData1 = data_q.get()
        #print(imgData1)
        saveIndex(imgData1)
        data_q.task_done()

def main():
    #socket.setdefaulttimeout(10)
    if(sys.version_info.major != 3):
        print("This script only works for python3")
        return
    try:
        logdata = ""
        with open("img\\exo-log.txt") as logfile:
            lines = logfile.readlines()
            # if(len(lines) == len(groupstr)):
            #     print("Already the latest!")
            #     return
            # elif(len(groupdir)>len(lines)):
            #     lastpoint = len(lines)
    except:
        pass

    for x in range(MaxThread):
        t = threading.Thread(target = worker)
        t.daemon = True
        t.start()

    for idir in groupdir:
        mkdir(idir)
    mkdir("link")
    start = time.time()
    simglist = []
    # init
    for istr in groupstr:
        data_q.put(istr)

    data_q.join()
    print("entire job took:", time.time()-start)
    # today = str(datetime.date.today())
    with open("img\\exo-log.txt", "w", encoding='utf-8') as logfile:
        for ilog in groupstr:
            istr = str(ilog)+","
            logfile.write(istr)
            logfile.write("\n")


if __name__ == '__main__':
  main()
  os.system("pause")

#appendix
#weapon
#http://game-a1.granbluefantasy.jp/assets/img/sp/assets/weapon/m/1040001600.jpg
#http://game-a.granbluefantasy.jp/assets/img/sp/assets/weapon/b/1040001600.png
#http://game-a.granbluefantasy.jp/assets/img/sp/assets/weapon/ls/1040500300.jpg
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