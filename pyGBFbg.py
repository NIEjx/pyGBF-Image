# 批量下载GBF游戏资源-召唤石
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

# chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover bg chara[extra] zoom[extra]
groupstack = -1
grouptop = 0
prefix1 = "http://game-a.granbluefantasy.jp/assets/img/sp/top/bg/million/bg_"
groupdir = "img\\bg"
#quest extra needs big step
groupstep = 50
grouplink = "link\\bg.txt"

MaxThread = 40

def bgimglist(groupid):
    list = []
    # 3040001000
    for index in range(groupstack+1, groupstack+1+groupstep):
        list.append(imgName(index, groupid, 4))
    return list

def mkdir(path):
    tmppath = os.getcwd()+"\\"+path
    try:
        os.makedirs(tmppath)
    except:
        pass
    return tmppath

class imgName:
    id = 0
    groupid = 0
    suffix = 1
    def __init__(self, id, groupid, suffix = 1):
        self.id = id
        self.groupid = groupid
        #self.dir = dir
        self.suffix = suffix
    def __str__(self):
        thisstr = "["+str(self.id)+","+str(self.groupid)+"]"
        return thisstr


def saveIndex(imgData):
    time.sleep(0.1)
    global groupstack
    global grouptop
    global groupdir
    with print_lock:
        imgName = str(imgData.id)
        dir = groupdir
        count = 0
        try:
            url = prefix1 + imgName +".jpg"
            #print(url)
            if(download.saveImg(url,dir)):
                count+=1
                if(SAVELINK):
                    with open(grouplink[imgData.groupid],"a") as linkfile:
                        linkfile.write(url+"\n")
        except:
            pass

        #update logic
        if(count >0):
            if(imgData.id > groupstack):
                print("update list " + groupdir)
                groupstack += groupstep
                simglist = []
                simglist = bgimglist(imgData.groupid)
                for iimg in simglist:
                    data_q.put(iimg)
                simglist.clear()
            if(imgData.id>grouptop):
                grouptop = imgData.id

def worker():
    while True:
        imgData1 = data_q.get()
        #print(imgData1)
        saveIndex(imgData1)
        data_q.task_done()

def main():
    #socket.setdefaulttimeout(10)
    global grouptop
    global groupstack
    if(sys.version_info.major != 3):
        print("This script only works for python3")
        return
    try:
        logdata = ""
        with open("img\\bg\\log.txt") as logfile:
            lines = logfile.readlines()
            logdata = lines[1]
        if (logdata != ""):
            data = logdata.split(',')
            numgroup = 2
            if (len(data) == numgroup):
                print("download start from latest")
                for i in range(0, numgroup):
                    groupstack = int(data[i])
                    grouptop = int(data[i])
    except:
        pass


    for x in range(MaxThread):
        t = threading.Thread(target = worker)
        t.daemon = True
        t.start()

    mkdir(groupdir)
    mkdir("link")
    start = time.time()
    simglist = []
    # bg
    simglist = bgimglist(0)
    for iimg in simglist:
        data_q.put(iimg)
    simglist.clear()

    data_q.join()
    print("entire job took:", time.time()-start)
    # today = str(datetime.date.today())
    with open("img\\bg\\log.txt", "w", encoding='utf-8') as logfile:
        istr = "bg\n"
        logfile.write(istr)
        istr = str(grouptop)+","
        logfile.write(istr)
        logfile.write("\n")

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