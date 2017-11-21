# 批量下载GBF游戏资源-职业图
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

MaxThread = 40

prelist = ['100001_sw_', '110001_sw_',
           '120001_wa_', '130001_wa_',
           '140001_kn_', '150001_sw_',
           '160001_me_', '170001_bw_',
           '180001_mc_', '190001_sp_',
           '100101_sw_', '110101_sw_',
           '120101_wa_', '150101_sw_',
           '180101_mc_', '140101_kn_',
           '160101_me_', '170101_bw_',
           '130101_wa_', '190101_sp_',
           '100201_sw_', '110201_sw_',
           '120201_wa_', '150201_sw_',
           '180201_mc_', '140201_kn_',
           '190201_sp_', '170201_bw_',
           '130201_wa_', '160201_me_',
           '100301_sw_', '110301_sw_',
           '120301_wa_', '180301_mc_',
           '140301_kn_', '150301_sw_',
           '170301_bw_', '130301_wa_',
           '190301_sp_', '160301_me_',
           '210201_kt_', '220201_kt_',
           '230201_sw_', '240201_gu_',
           '250201_wa_', '270201_mc_',
           '260201_kn_', '165001_me_',
           '185001_mc_', '125001_wa_',
           '310001_sw_', '360001_me_',
           '310101_sw_', '200201_kn_',
           '280201_kn_', '360101_gu_']
prefix1 = "http://game-a1.granbluefantasy.jp/assets/img/sp/"
groupdir = ["img\\class\\cover","img\\class\\change","img\\class\\spirit"]
grouplink = ["link\\class-cover.txt","link\\class.txt","link\\class-sp.txt"]
def mkdir(path):
    tmppath = os.getcwd()+"\\"+path
    try:
        os.makedirs(tmppath)

    except:
        pass
    return tmppath

def saveIndex(istr):
    time.sleep(0.1)
    with print_lock:
        for gentle in [0,1]:
            try:
                url = prefix1 + "assets/leader/job_change/" + istr + str(gentle) +"_01.png"
                if(download.saveImg(url,groupdir[1])):
                    if(SAVELINK):
                        with open(grouplink[1],"a") as linkfile:
                            linkfile.write(url+"\n")
            except:
                pass
            for word in ['a','b','c','d','e']:
                try:
                    url = prefix1 + "cjs/job_release_" + istr[0:6] + "_" + str(gentle) + "_"+word+".png"
                    if (download.saveImg(url, groupdir[2])):
                        if (SAVELINK):
                            with open(grouplink[2], "a") as linkfile:
                                linkfile.write(url + "\n")
                except:
                    pass
            try:
                url = prefix1 + "assets/leader/my/" + istr + str(gentle) + "_01.png"
                if(download.saveImg(url,groupdir[0])):
                    if(SAVELINK):
                        with open(grouplink[0],"a") as linkfile:
                            linkfile.write(url+"\n")
            except:
                pass

def worker():
    while True:
        imgData1 = data_q.get()
        saveIndex(imgData1)
        data_q.task_done()

def main():
    #socket.setdefaulttimeout(10)
    if(sys.version_info.major != 3):
        print("This script only works for python3")
        return
    lastpoint = 0
    try:
        logdata = ""
        with open("img\\class\\log.txt") as logfile:
            lines = logfile.readlines()
            if(len(lines) == len(prelist)):
                print("Already the latest!")
                return
            elif(len(prelist)>len(lines)):
                lastpoint = len(lines)
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

    for i in prelist[lastpoint:]:
        data_q.put(i)
    data_q.join()
    print("entire job took:", time.time()-start)
    # today = str(datetime.date.today())
    with open("img\\class\\log.txt", "w", encoding='utf-8') as logfile:
        for ilog in prelist:
            iline = ilog + "\n"
            logfile.write(iline)

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