# 批量下载GBF武器立绘
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
import pyGBFmainchara as mainchara
import pyGBFexchara as exchara

dirname = os.getcwd()
print_lock = threading.Lock()
data_q = Queue()
SAVELINK = False
DEBUG = False

# chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover bg chara[extra] zoom[extra]
groupstack = [-1,-1,-1,-1,-1]
grouptop =   [0,0,0,0,0]
prefix1 = "http://game-a.granbluefantasy.jp/assets/img/sp/"
groupstr = ["assets/npc/b/302","assets/npc/b/303","assets/npc/b/304","assets/npc/b/371","assets/npc/b/399",
            "quest/scene/character/body/302","quest/scene/character/body/303","quest/scene/character/body/304","","quest/scene/character/body/399",
            "assets/npc/zoom/302","assets/npc/zoom/303","assets/npc/zoom/304","assets/npc/zoom/371","assets/npc/zoom/399",
            "assets/npc/my/302","assets/npc/my/303","assets/npc/my/304","assets/npc/my/371",""]
# chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover
groupdir = ["img\\chara\\r","img\\chara\\sr","img\\chara\\ssr","img\\chara\\skin","img\\chara\\extra",
            "img\\quest\\r","img\\quest\\sr","img\\quest\\ssr","","img\\quest\\extra",
            "img\\zoom\\r","img\\zoom\\sr","img\\zoom\\ssr","img\\zoom\\skin","img\\zoom\\extra",
            "img\\cover\\r","img\\cover\\sr","img\\cover\\ssr","img\\cover\\skin",""]
#r sr ssr skin extra
groupstep = [20,20,20,20,50]
grouplink = ["link\\chara-r.txt","link\\chara-sr.txt","link\\chara-ssr.txt","link\\chara-skin.txt","link\\chara-ex.txt",
             "link\\quest-r.txt","link\\quest-sr.txt","link\\quest-ssr.txt","","link\\quest-ex.txt",
             "link\\zoom-r.txt","link\\zoom-sr.txt","link\\zoom-ssr.txt","link\\zoom-skin.txt","link\\zoom-ex.txt",
             "link\\cover-r.txt","link\\cover-sr.txt","link\\cover-ssr.txt","link\\cover-skin.txt",""]
explist = ["","_angry","_cutin","_eye",
           "_joy","_laugh3","_laugh2","_laugh",
           "_mood","_mortifying","_surprise_fe","_sad",
           "_suddenly","_serious","_surprise","_shy",
           "_think","_weak","_01","_02","_03"]
suflist = ["_01","_02","_03"]
MaxThread = 40

def imglist(groupid):
    list = []
    # 3040001000_01
    truegroup = groupid
    for index in range(groupstack[groupid]+1, groupstack[groupid]+1+groupstep[groupid]):
        list.append(imgName(index, groupid, 0))
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
    #dirid = 0
    suffix = 1
    def __init__(self, id, groupid, suffix = 1):
        self.id = id
        self.groupid = groupid
        #self.dirid = dirid
        self.suffix = suffix
    def __str__(self):
        thisstr = "["+ str(self.id)+","+str(self.groupid)+"]"
        return thisstr

def saveIndex(imgData):
    time.sleep(0.1)
    with print_lock:
        imgName = str(imgData.id).zfill(4)+"000"
        gid = imgData.groupid
        count = 0
        # book
        for isuf in suflist:
            try:
                url = prefix1 + groupstr[gid] + imgName + isuf+ ".png"
                if(download.saveImg(url,groupdir[gid])):
                    count+=1
                    if(SAVELINK):
                        #print(grouplink[imgData.groupid])
                        #print(imgData.url)
                        with open(grouplink[gid],"a") as linkfile:
                            linkfile.write(url+"\n")
            except:
                pass
        # zoom
        for isuf in suflist:
            try:
                url = prefix1 + groupstr[10+gid] + imgName + isuf+ ".png"
                if(download.saveImg(url,groupdir[10+gid])):
                    count+=1
                    if(SAVELINK):
                        #print(grouplink[imgData.groupid])
                        #print(imgData.url)
                        with open(grouplink[10+gid],"a") as linkfile:
                            linkfile.write(url+"\n")
            except:
                pass
        # quest
        if(gid != 3):
            for iexp in explist:
                try:
                    url = prefix1 + groupstr[5 + gid] + imgName + iexp + ".png"
                    if (download.saveImg(url, groupdir[5 + gid])):
                        count += 1
                        if (SAVELINK):
                            # print(grouplink[imgData.groupid])
                            # print(imgData.url)
                            with open(grouplink[5 + gid], "a") as linkfile:
                                linkfile.write(url + "\n")
                except:
                    pass
        # cover
        if(gid != 4):
            for isuf in suflist:
                try:
                    url = prefix1 + groupstr[15 + gid] + imgName + isuf + ".png"
                    if (download.saveImg(url, groupdir[15 + gid])):
                        count += 1
                        if (SAVELINK):
                            # print(grouplink[imgData.groupid])
                            # print(imgData.url)
                            with open(grouplink[15 + gid], "a") as linkfile:
                                linkfile.write(url + "\n")
                except:
                    pass


        #update logic
        if(count >0 ):
            if(imgData.id > groupstack[gid]):
                print("update list " + groupdir[gid])
                groupstack[gid] += groupstep[gid]
                print(gid)
                print(groupstack[gid])
                simglist = []
                simglist = imglist(gid)
                for iimg in simglist:
                    data_q.put(iimg)
                simglist.clear()
            if(imgData.id>grouptop[gid]):
                grouptop[gid] = imgData.id


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
        with open("img\\log.txt") as logfile:
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
        if(idir!= ""):
            mkdir(idir)

    start = time.time()
    simglist = []
    # init
    for index in range(0,5):
        simglist = imglist(index)
        for iimg in simglist:
            data_q.put(iimg)
        simglist.clear()

    data_q.join()
    print("entire job took:", time.time()-start)
    # today = str(datetime.date.today())
    with open("img\\log.txt", "w", encoding='utf-8') as logfile:
        istr = "[r|sr|ssr|skin|extra] [chara|quest|zoom|cover]\n"
        logfile.write(istr)
        for ilog in grouptop:
            istr = str(ilog)+","
            logfile.write(istr)
        logfile.write("\n")


if __name__ == '__main__':
  main()
  mainchara.main()
  exchara.main()
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