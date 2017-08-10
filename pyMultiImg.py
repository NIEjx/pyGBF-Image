from queue import Queue
import os
import time
import threading
import urllib.request
import urllib.error

dirname = os.getcwd()
print_lock = threading.Lock()
data_q = Queue()

# chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover
groupstack = [0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,
              0,0]
groupstr = ["http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/b/302",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/b/303",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/b/304",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/b/371",
            "http://game-a1.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/302",
            "http://game-a1.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/303",
            "http://game-a1.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/304",
            "http://game-a1.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/399",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/summon/b/201",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/summon/b/202",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/summon/b/203",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/summon/b/204",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/zoom/302",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/zoom/303",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/zoom/304",
            "http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/zoom/371",
            "http://game-a1.granbluefantasy.jp/assets/img/sp/assets/npc/my/302",
            "http://game-a1.granbluefantasy.jp/assets/img/sp/assets/npc/my/303",
            "http://game-a1.granbluefantasy.jp/assets/img/sp/assets/npc/my/304",
            "http://game-a1.granbluefantasy.jp/assets/img/sp/assets/npc/my/371",
            "class",
            "classcover"]
# chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover
groupdir = ["chara\\R","chara\\SR","chara\\SSR","chara\\Skin",
            "quest\\R","quest\\SR","quest\\SSR","quest\\Extra",
            "summon\\N","summon\\R","summon\\SR","summon\\SSR",
            "zoom\\R","zoom\\SR","zoom\\SSR","zoom\\Skin",
            "cover\\R","cover\\SR","cover\\SSR","cover\\Skin",
            "class","cover\\class"]
#quest extra needs big step
groupstep = [20,20,20,20,
             20,20,20,50,
             20,20,20,20,
             20,20,20,20,
             20,20,20,20,
             0,0]

MaxThread = 40

def imglist(groupid):
    list = []
    # 3040001000_01
    for index in range(groupstack[groupid], groupstack[groupid]+groupstep[groupid]):
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_01.png"
        #url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr,index,groupid,1)  )
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_02.png"
        list.append(imgName(tmpstr, index, groupid, 1))
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_03.png"
        list.append(imgName(tmpstr, index, groupid, 1))
    return list
def imglist2(groupid):
    list = []
    # 3040001000
    for index in range(groupstack[groupid], groupstack[groupid]+groupstep[groupid]):
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000.png"
        # url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr, index, groupid, 2))
    return list
def imglist3(groupid):
    list = []
    # 3040001000
    for index in range(groupstack[groupid], groupstack[groupid]+groupstep[groupid]):
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000.png"
        # url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr, index, groupid, 3))
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_laugh.png"
        # url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr, index, groupid, 3))
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_laugh2.png"
        # url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr, index, groupid, 3))
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_sad.png"
        # url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr, index, groupid, 3))
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_angry.png"
        # url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr, index, groupid, 3))
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_serious.png"
        # url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr, index, groupid, 3))
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_surprise.png"
        # url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr, index, groupid, 3))
        tmpstr = groupstr[groupid] + str(index).zfill(4) + "000_suddenly.png"
        # url, dir, id, groupid, suffix = False
        list.append(imgName(tmpstr, index, groupid, 3))
    return list
def exlist():
    list = []
    tmpsrc = ["http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_muffler.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_muffler_laugh.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000muffler_laugh2.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_muffler_sad.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_muffler_suddenly.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_muffler_surprise.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_muffler2.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_angry.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_laugh.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_sad.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_suddenly.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_surprise.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_summer.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_summer_joy.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_summer_laugh.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_summer_sad.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_summer_surprise.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_summer2.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_swim.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_angry.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_laugh.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_sad.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_suddenly.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_surprise.png",
              "http://game-a.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3050000000_race_cutin.png"]
    n = 0
    for i in tmpsrc:
        list.append(imgName(i,-1,7,2))
    return list

def classimglist():
    list = []
    str1 = "http://game-a1.granbluefantasy.jp/assets/img/sp/assets/leader/job_change/"
    str2 = "http://game-a1.granbluefantasy.jp/assets/img/sp/cjs/job_release_"
    tmplist = ('100001_sw_','110001_sw_',
               '120001_wa_','130001_wa_',
               '140001_kn_','150001_sw_',
               '160001_me_','170001_bw_',
               '180001_mc_','190001_sp_',
               '100101_sw_','110101_sw_',
               '120101_wa_','150101_sw_',
               '180101_mc_','140101_kn_',
               '160101_me_','170101_bw_',
               '130101_wa_','190101_sp_',
               '100201_sw_','110201_sw_',
               '120201_wa_','150201_sw_',
               '180201_mc_','140201_kn_',
               '190201_sp_','170201_bw_',
               '130201_wa_','160201_me_',
               '100301_sw_','110301_sw_',
               '120301_wa_','180301_mc_',
               '140301_kn_','150301_sw_',
               '170301_bw_','130301_wa_',
               '190301_sp_','160301_me_',
               '210201_kt_','220201_kt_',
               '230201_sw_','240201_gu_',
               '250201_wa_','270201_mc_',
               '260201_kn_')

    #change class
    for iStr in tmplist:
        # class man
        tmpStr= str1+iStr+"0_01.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        # woman
        tmpStr = str1 + iStr + "1_01.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        # change class man
        tmpStr = str2 + iStr[0:6] + "_0_a.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        tmpStr = str2 + iStr[0:6] + "_0_b.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        tmpStr = str2 + iStr[0:6] + "_0_c.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        tmpStr = str2 + iStr[0:6] + "_0_d.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        tmpStr = str2 + iStr[0:6] + "_0_e.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        # woman
        tmpStr = str2 + iStr[0:6] + "_1_a.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        tmpStr = str2 + iStr[0:6] + "_1_b.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        tmpStr = str2 + iStr[0:6] + "_1_c.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        tmpStr = str2 + iStr[0:6] + "_1_d.png"
        list.append(imgName(tmpStr, -1, 20, 2))
        tmpStr = str2 + iStr[0:6] + "_1_e.png"
        list.append(imgName(tmpStr, -1, 20, 2))
    return list
def coverimglist():
    list = []
    str1 = "http://game-a1.granbluefantasy.jp/assets/img/sp/assets/leader/my/"
    tmplist = ('100001_sw_','110001_sw_',
               '120001_wa_','130001_wa_',
               '140001_kn_','150001_sw_',
               '160001_me_','170001_bw_',
               '180001_mc_','190001_sp_',
               '100101_sw_','110101_sw_',
               '120101_wa_','150101_sw_',
               '180101_mc_','140101_kn_',
               '160101_me_','170101_bw_',
               '130101_wa_','190101_sp_',
               '100201_sw_','110201_sw_',
               '120201_wa_','150201_sw_',
               '180201_mc_','140201_kn_',
               '190201_sp_','170201_bw_',
               '130201_wa_','160201_me_',
               '100301_sw_','110301_sw_',
               '120301_wa_','180301_mc_',
               '140301_kn_','150301_sw_',
               '170301_bw_','130301_wa_',
               '190301_sp_','160301_me_',
               '210201_kt_','220201_kt_',
               '230201_sw_','240201_gu_',
               '250201_wa_','270201_mc_',
               '260201_kn_','165001_me_',
               '185001_mc_','125001_wa_',
               '310001_sw_','360001_me_')

    #change class
    for iStr in tmplist:
        # class man
        tmpStr= str1+iStr+"0_01.png"
        list.append(imgName(tmpStr, -1, 21, 2))
        # woman
        tmpStr = str1 + iStr + "1_01.png"
        list.append(imgName(tmpStr, -1, 21, 2))
    return list
def mkdir(path):
    tmppath = os.getcwd()+"\\"+path
    try:
        os.makedirs(tmppath)

    except:
        pass
    return tmppath

class imgName:
    url = ""
    #dir = ""
    id = 0
    groupid = 0
    suffix = 1
    def __init__(self, url, id, groupid, suffix = 1):
        self.url = url
        self.id = id
        self.groupid = groupid
        #self.dir = dir
        self.suffix = suffix
    def __str__(self):
        thisstr = "["+self.url+","+str(self.id)+","+str(self.groupid)+"]"
        return thisstr


def saveImg(imgData):
    time.sleep(0.1)
    with print_lock:
        imgName = imgData.url.split('/')[-1]
        dir = dirname+"\\"+groupdir[imgData.groupid]
        print("downloading:"+imgName)
        try:
            raw = urllib.request.urlopen(imgData.url)
            img = raw.read()
            raw.close()
            #update logic
            if(imgData.id>groupstack[imgData.groupid]):
                groupstack[imgData.groupid] += groupstep[imgData.groupid]
                simglist = []
                if(imgData.suffix == 1):
                    simglist = imglist(imgData.groupid)
                elif(imgData.suffix == 2):
                    simglist = imglist2(imgData.groupid)
                elif(imgData.suffix == 3):
                    simglist = imglist3(imgData.groupid)
                else:
                    print("wrong suffix")

                for iimg in simglist:
                    data_q.put(iimg)
                simglist.clear()
            #save logic
            if(os.path.isfile(dir + "\\" + imgName) == False):
                with open(dir+"\\"+imgName,'wb') as file:
                    file.write(img)
            else:
                pass
        except:
            print("error:",imgName," in dir:",dir," not exist")
            pass


def worker():
    while True:
        imgData1 = data_q.get()
        #print(imgData1)
        saveImg(imgData1)
        data_q.task_done()

def main():
    #socket.setdefaulttimeout(10)

    for x in range(MaxThread):
        t = threading.Thread(target = worker)
        t.daemon = True
        t.start()

    for idir in groupdir:
        mkdir(idir)

    start = time.time()
    simglist = []
    # chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] mypage[r/sr/ssr/skin] class cover
    #character image
    for index in range(0,4):
        simglist = imglist(index)
        for iimg in simglist:
            data_q.put(iimg)
        simglist.clear()
    # quest image with expression
    for index in range(4,8):
        simglist = imglist3(index)
        for iimg in simglist:
            data_q.put(iimg)
        simglist.clear()
    # summon stone
    for index in range(8,12):
        simglist = imglist2(index)
        for iimg in simglist:
            data_q.put(iimg)
        simglist.clear()
    # character zoom image & mypage image
    for index in range(12,20):
        simglist = imglist(index)
        for iimg in simglist:
            data_q.put(iimg)
        simglist.clear()
    #class revolution
    simglist = classimglist()
    for iimg in simglist:
        data_q.put(iimg)
    simglist.clear()
    #mypage class
    simglist = coverimglist()
    for iimg in simglist:
        data_q.put(iimg)
    simglist.clear()
    #quest extra
    simglist = exlist()
    for iimg in simglist:
        data_q.put(iimg)
    simglist.clear()

    data_q.join()
    print("entire job took:", time.time()-start)


if __name__ == '__main__':
  main()

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