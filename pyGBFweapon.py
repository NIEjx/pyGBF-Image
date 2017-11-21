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


dirname = os.getcwd()
print_lock = threading.Lock()
data_q = Queue()
SAVELINK = False
DEBUG = False

# chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover bg chara[extra] zoom[extra]
groupstack = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
              -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,]
grouptop =   [0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0]
prefix1 = "http://game-a1.granbluefantasy.jp/assets/img/sp/assets/weapon/"
groupstr = ["100","101","102","103","104","105","106","107","108","109",
            "200","201","202","203","204","205","206","207","208","209",
            "300","301","302","303","304","305","306","307","308","309",
            "400","401","402","403","404","405","406","407","408","409"]
# chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover
groupdir = ["img\\weapon\\n","img\\weapon\\r","img\\weapon\\sr","img\\weapon\\ssr"]
#quest extra needs big step
groupstep = [20,20,20,20,20,20,20,20,20,20,
             20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
             20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
             20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
grouplink = ["link\\wp-n.txt","link\\wp-r.txt","link\\wp-sr.txt","link\\wp-ssr.txt"]

MaxThread = 40

def wpimglist(groupid):
    list = []
    # 3040001000_01
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
        imgName = "10"+ groupstr[imgData.groupid] + str(imgData.id).zfill(3)+"00"
        iddir = imgData.groupid //10
        dir = groupdir[iddir]
        count = 0
        try:
            url = prefix1 + "m/" + imgName +".jpg"
            if(download.saveImg(url,dir+"\\m")):
                count+=1
                if(SAVELINK):
                    #print(grouplink[imgData.groupid])
                    #print(imgData.url)
                    with open(grouplink[iddir],"a") as linkfile:
                        linkfile.write(url+"\n")
        except:
            pass

        try:
            url = prefix1 + "b/" + imgName +".png"
            if(download.saveImg(url,dir+"\\b")):
                count+=1
                if(SAVELINK):
                    #print(grouplink[imgData.groupid])
                    #print(imgData.url)
                    with open(grouplink[iddir],"a") as linkfile:
                        linkfile.write(url+"\n")
        except:
            pass

        try:
            url = prefix1 + "ls/" + imgName +".jpg"
            if(download.saveImg(url,dir+"\\ls")):
                count+=1
                if(SAVELINK):
                    #print(grouplink[imgData.groupid])
                    #print(imgData.url)
                    with open(grouplink[iddir],"a") as linkfile:
                        linkfile.write(url+"\n")
        except:
            pass
        #update logic
        if(count >0 ):
            if(imgData.id > groupstack[imgData.groupid]):
                print("update list " + groupdir[iddir])
                groupstack[imgData.groupid] += groupstep[imgData.groupid]
                simglist = []
                simglist = wpimglist(imgData.groupid)
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
        with open("img\\weapon\\log.txt") as logfile:
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
        mkdir(idir+"\\m")
        mkdir(idir + "\\b")
        mkdir(idir + "\\ls")
    mkdir("link")

    start = time.time()
    simglist = []
    # init
    for index in range(0,40):
        simglist = wpimglist(index)
        for iimg in simglist:
            data_q.put(iimg)
        simglist.clear()

    data_q.join()
    print("entire job took:", time.time()-start)
    # today = str(datetime.date.today())
    with open("img\\weapon\\log.txt", "w", encoding='utf-8') as logfile:
        istr = "weapon [n|r|sr|ssr][sword|blade|spear|axe|staff|gun|fist|bow|harp|katana]\n"
        logfile.write(istr)
        for ilog in grouptop:
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