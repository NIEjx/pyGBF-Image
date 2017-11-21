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
groupstack = [-1,-1,-1,-1]
grouptop = [0,0,0,0]
prefix1 = "http://game-a.granbluefantasy.jp/assets/img/sp/assets/summon/b/"
groupstr = ["201","202","203","204"]
# chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover
groupdir = ["img\\summon\\N","img\\summon\\R","img\\summon\\SR","img\\summon\\SSR"]
#quest extra needs big step
groupstep = [20,20,20,20]
grouplink = ["link\\smm-n.txt","link\\smm-r.txt","link\\smm-sr.txt","link\\smm-ssr.txt"]

MaxThread = 40

def smmimglist(groupid):
    list = []
    # 3040001000
    for index in range(groupstack[groupid]+1, groupstack[groupid]+1+groupstep[groupid]):
        list.append(imgName(index, groupid, 2))
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
    with print_lock:
        imgName = groupstr[imgData.groupid] + str(imgData.id).zfill(4)+"000"
        dir = groupdir[imgData.groupid]
        count = 0
        try:
            url = prefix1 + imgName +".png"
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
            if(imgData.id > groupstack[imgData.groupid]):
                print("update list " + groupdir[imgData.groupid])
                groupstack[imgData.groupid] += groupstep[imgData.groupid]
                simglist = []
                simglist = smmimglist(imgData.groupid)
                for iimg in simglist:
                    data_q.put(iimg)
                simglist.clear()
            if(imgData.id>grouptop[imgData.groupid]):
                grouptop[imgData.groupid] = imgData.id

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
        with open("img\\summon\\log.txt") as logfile:
            lines = logfile.readlines()
            logdata = lines[1]
        if (logdata != ""):
            data = logdata.split(',')
            numgroup = len(groupstack) + 1
            if (len(data) == numgroup):
                print("download start from latest")
                for i in range(0, numgroup):
                    groupstack[i] = int(data[i])
                    grouptop[i] = int(data[i])
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
    # summon stone
    for index in range(0,4):
        simglist = smmimglist(index)
        for iimg in simglist:
            data_q.put(iimg)
        simglist.clear()

    data_q.join()
    print("entire job took:", time.time()-start)
    # today = str(datetime.date.today())
    with open("img\\summon\\log.txt", "w", encoding='utf-8') as logfile:
        istr = "summon[n/r/sr/ssr]\n"
        logfile.write(istr)
        for ilog in grouptop:
            istr = str(ilog)+","
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