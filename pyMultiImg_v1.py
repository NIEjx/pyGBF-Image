from queue import Queue
import os
import time
import threading
import urllib.request
import urllib.error

dirname = os.getcwd()
print_lock = threading.Lock()
data_q = Queue()
#limitation
maxcharaR = 75
maxcharaSR = 250
maxcharaSSR = 150
maxcharaExtra = 800
maxsmmN = 50
maxsmmR = 50
maxsmmSR = 100
maxsmmSSR = 200

MaxThread = 40

#image set
#character
# http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/zoom/3040010000_01.png
#http://game-a.granbluefantasy.jp/assets/img_light/sp/assets/npc/b/3030007000_01.png
#class
#http://game-a1.granbluefantasy.jp/assets/img/sp/assets/leader/job_change/120001_wa_1_01.png
#http://game-a1.granbluefantasy.jp/assets/img/sp/cjs/job_release_180001_1_c.png
#quest character
#http://game-a1.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3040022000.png
#summon
#http://game-a.granbluefantasy.jp/assets/img/sp/assets/summon/b/2030011000.png
def charaimglist():
    list = []
    # 3040010000_01
    str1 = "http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/zoom/30"
   #rare 75
    for index in range(1,10):
        tmpstr= str1+"2000"+str(index)+"000_01.png"
        list.append(tmpstr)
        tmpstr = str1 + "2000" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "2000" + str(index) + "000_03.png"
        list.append(tmpstr)
    if(maxcharaR <= 100):
        for index in range(11,maxcharaR):
            tmpstr= str1+"200"+str(index)+"000_01.png"
            list.append(tmpstr)
            tmpstr = str1 + "200" + str(index) + "000_02.png"
            list.append(tmpstr)
            tmpstr = str1 + "200" + str(index) + "000_03.png"
            list.append(tmpstr)
    else:
        for index in range(11,100):
            tmpstr= str1+"200"+str(index)+"000_01.png"
            list.append(tmpstr)
            tmpstr = str1 + "200" + str(index) + "000_02.png"
            list.append(tmpstr)
            tmpstr = str1 + "200" + str(index) + "000_03.png"
            list.append(tmpstr)
        for index in range(100,maxcharaR):
            tmpstr= str1+"20"+str(index)+"000_01.png"
            list.append(tmpstr)
            tmpstr = str1 + "20" + str(index) + "000_02.png"
            list.append(tmpstr)
            tmpstr = str1 + "20" + str(index) + "000_03.png"
            list.append(tmpstr)
    #super rare 250
    for index in range(1,10):
        tmpstr= str1+"3000"+str(index)+"000_01.png"
        list.append(tmpstr)
        tmpstr = str1 + "3000" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "3000" + str(index) + "000_03.png"
        list.append(tmpstr)
    for index in range(11,100):
        tmpstr= str1+"300"+str(index)+"000_01.png"
        list.append(tmpstr)
        tmpstr = str1 + "300" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "300" + str(index) + "000_03.png"
        list.append(tmpstr)
    for index in range(100,maxcharaSR):
        tmpstr= str1+"30"+str(index)+"000_01.png"
        list.append(tmpstr)
        tmpstr = str1 + "30" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "30" + str(index) + "000_03.png"
        list.append(tmpstr)
    #SSR 150
    for index in range(1,10):
        tmpstr= str1+"4000"+str(index)+"000_01.png"
        list.append(tmpstr)
        tmpstr = str1 + "4000" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "4000" + str(index) + "000_03.png"
        list.append(tmpstr)
    for index in range(11,100):
        tmpstr= str1+"400"+str(index)+"000_01.png"
        list.append(tmpstr)
        tmpstr = str1 + "400" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "400" + str(index) + "000_03.png"
        list.append(tmpstr)
    for index in range(100,maxcharaSSR):
        tmpstr= str1+"40"+str(index)+"000_01.png"
        list.append(tmpstr)
        tmpstr = str1 + "40" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "40" + str(index) + "000_03.png"
        list.append(tmpstr)
    return list
#zoom
def charazimglist():
    list = []
    # 3040010000_01
    str1 = "http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/b/30"
    #rare 75
    for index in range(1,10):
        tmpstr = str1 + "2000" + str(index) + "000_03.png"
        list.append(tmpstr)
    if(maxcharaR <= 100):
        for index in range(11,maxcharaR):
            tmpstr = str1 + "200" + str(index) + "000_03.png"
            list.append(tmpstr)
    else:
        for index in range(11,100):
            tmpstr = str1 + "200" + str(index) + "000_03.png"
            list.append(tmpstr)
        for index in range(100,maxcharaR):
            tmpstr = str1 + "20" + str(index) + "000_03.png"
            list.append(tmpstr)
    #super rare 250
    for index in range(1,10):
        tmpstr = str1 + "3000" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "3000" + str(index) + "000_03.png"
        list.append(tmpstr)
    for index in range(11,100):
        tmpstr = str1 + "300" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "300" + str(index) + "000_03.png"
        list.append(tmpstr)
    for index in range(100,maxcharaSR):
        tmpstr = str1 + "30" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "30" + str(index) + "000_03.png"
        list.append(tmpstr)
    #SSR 150
    for index in range(1,10):
        tmpstr = str1 + "4000" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "4000" + str(index) + "000_03.png"
        list.append(tmpstr)
    for index in range(11,100):
        tmpstr = str1 + "400" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "400" + str(index) + "000_03.png"
        list.append(tmpstr)
    for index in range(100,maxcharaSSR):
        tmpstr = str1 + "40" + str(index) + "000_02.png"
        list.append(tmpstr)
        tmpstr = str1 + "40" + str(index) + "000_03.png"
        list.append(tmpstr)
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
        list.append(tmpStr)
        # woman
        tmpStr = str1 + iStr + "1_01.png"
        list.append(tmpStr)
        # change class man
        tmpStr = str2 + iStr[0:6] + "_0_a.png"
        list.append(tmpStr)
        tmpStr = str2 + iStr[0:6] + "_0_b.png"
        list.append(tmpStr)
        tmpStr = str2 + iStr[0:6] + "_0_c.png"
        list.append(tmpStr)
        tmpStr = str2 + iStr[0:6] + "_0_d.png"
        list.append(tmpStr)
        tmpStr = str2 + iStr[0:6] + "_0_e.png"
        list.append(tmpStr)
        # woman
        tmpStr = str2 + iStr[0:6] + "_1_a.png"
        list.append(tmpStr)
        tmpStr = str2 + iStr[0:6] + "_1_b.png"
        list.append(tmpStr)
        tmpStr = str2 + iStr[0:6] + "_1_c.png"
        list.append(tmpStr)
        tmpStr = str2 + iStr[0:6] + "_1_d.png"
        list.append(tmpStr)
        tmpStr = str2 + iStr[0:6] + "_1_e.png"
        list.append(tmpStr)
    return list
def questimglist():
    list = []
    # 3040010000_01
    str1 = "http://game-a1.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/30"
    #rare 75
    for index in range(1,10):
        tmpstr= str1+"2000"+str(index)+"000.png"
        list.append(tmpstr)
    if(maxcharaR<=100):
        for index in range(11,maxcharaR):
            tmpstr= str1+"200"+str(index)+"000.png"
            list.append(tmpstr)
    else:
        for index in range(11,100):
            tmpstr= str1+"200"+str(index)+"000.png"
            list.append(tmpstr)
        for index in range(100,maxcharaR):
            tmpstr= str1+"20"+str(index)+"000.png"
            list.append(tmpstr)
    #super rare 250
    for index in range(1,10):
        tmpstr= str1+"3000"+str(index)+"000.png"
        list.append(tmpstr)
    for index in range(11,100):
        tmpstr= str1+"300"+str(index)+"000.png"
        list.append(tmpstr)
    for index in range(100,maxcharaSR):
        tmpstr= str1+"30"+str(index)+"000.png"
        list.append(tmpstr)
    #SSR 150
    for index in range(1,10):
        tmpstr= str1+"4000"+str(index)+"000.png"
        list.append(tmpstr)

    for index in range(11,100):
        tmpstr= str1+"400"+str(index)+"000.png"
        list.append(tmpstr)

    for index in range(100,maxcharaSSR):
        tmpstr= str1+"40"+str(index)+"000.png"
        list.append(tmpstr)
    #extra
    str1 = "http://game-a1.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/399"
    for index in range(1,10):
        tmpstr= str1+"000"+str(index)+"000.png"
        list.append(tmpstr)

    for index in range(11,100):
        tmpstr= str1+"00"+str(index)+"000.png"
        list.append(tmpstr)

    for index in range(100,maxcharaExtra):
        tmpstr= str1+"0"+str(index)+"000.png"
        list.append(tmpstr)

    return list
def smmimglist():
    list = []
    # 3040010000_01
    str1 = "http://game-a.granbluefantasy.jp/assets/img/sp/assets/summon/b/20"
    #normal 9 / 50
    for index in range(1,10):
        tmpstr= str1+"1000"+str(index)+"000.png"
        list.append(tmpstr)
    if(maxsmmN <= 100):
        for index in range(11,maxsmmN):
            tmpstr= str1+"100"+str(index)+"000.png"
            list.append(tmpstr)
    else:
        for index in range(11,100):
            tmpstr= str1+"100"+str(index)+"000.png"
            list.append(tmpstr)
        for index in range(100,maxsmmN):
            tmpstr= str1+"10"+str(index)+"000.png"
            list.append(tmpstr)
    #rare 34 / 50
    for index in range(1,10):
        tmpstr= str1+"2000"+str(index)+"000.png"
        list.append(tmpstr)
    if(maxsmmR<=100):
        for index in range(11,maxsmmR):
            tmpstr= str1+"200"+str(index)+"000.png"
            list.append(tmpstr)
    else:
        for index in range(11, 100):
            tmpstr = str1 + "200" + str(index) + "000.png"
            list.append(tmpstr)
        for index in range(100, maxsmmR):
            tmpstr = str1 + "20" + str(index) + "000.png"
            list.append(tmpstr)
    #super rare 55 / 100
    for index in range(1,10):
        tmpstr= str1+"3000"+str(index)+"000.png"
        list.append(tmpstr)
    if(maxsmmSR <= 100):
        for index in range(11,maxsmmSR):
            tmpstr= str1+"300"+str(index)+"000.png"
            list.append(tmpstr)
    else:
        for index in range(11, 100):
            tmpstr = str1 + "300" + str(index) + "000.png"
            list.append(tmpstr)
        for index in range(100, maxsmmSR):
            tmpstr = str1 + "30" + str(index) + "000.png"
            list.append(tmpstr)
    #SSR 129/ 150
    for index in range(1,10):
        tmpstr= str1+"4000"+str(index)+"000.png"
        list.append(tmpstr)

    for index in range(11,100):
        tmpstr= str1+"400"+str(index)+"000.png"
        list.append(tmpstr)

    for index in range(100,maxsmmSSR):
        tmpstr= str1+"40"+str(index)+"000.png"
        list.append(tmpstr)

    return list
# def classimglist():
#     list = []
#     str1 = "http://game-a1.granbluefantasy.jp/assets/img/sp/assets/leader/job_change/"
#     str2 = "http://game-a1.granbluefantasy.jp/assets/img/sp/cjs/job_release_"
#     #change class
#     for iStr in tmplist:
#         # class man
#         tmpStr= str1+iStr+"0_01.png"
#         list.append(tmpStr)
#     return list
def mkdir(path):
    tmppath = os.getcwd()+"\\"+path
    try:
        os.makedirs(tmppath)

    except:
        pass
    #     if(OSError.errno ==17):
    #         pass
    #     else:
    #         print(OSError.errno)
    #         sys.exit()
    return tmppath
class imgName:
    url = ""
    dir = ""
    def __init__(self, url, dir):
        self.url = url
        self.dir = dir


def saveImg(imgData):
    time.sleep(0.1)
    with print_lock:
        imgName = imgData.url.split('/')[-1]
        try:
            raw = urllib.request.urlopen(imgData.url)
            img = raw.read()
            raw.close()
            with open(imgData.dir+"\\"+imgName,'wb') as file:
                file.write(img)
        except:
            print("error:",imgName," not exist")
            pass
def worker():
    while True:
        imgData = data_q.get()
        saveImg(imgData)
        data_q.task_done()
def main():
    #socket.setdefaulttimeout(10)

    for x in range(MaxThread):
        t = threading.Thread(target = worker)
        t.daemon = True
        t.start()
    start = time.time()

    simglist = charaimglist()
    dirname = mkdir("chara")
    for iimg in simglist:
        data_q.put(imgName(iimg, dirname))
    simglist.clear()

    simglist = charazimglist()
    dirname = mkdir("zoom")
    for iimg in simglist:
        data_q.put(imgName(iimg, dirname))
    simglist.clear()

    simglist = classimglist()
    dirname = mkdir("class")
    for iimg in simglist:
        data_q.put(imgName(iimg, dirname))
    simglist.clear()

    simglist = questimglist()
    dirname = mkdir("quest")
    for iimg in simglist:
        data_q.put(imgName(iimg, dirname))
    simglist.clear()

    simglist = smmimglist()
    dirname = mkdir("summon")
    for iimg in simglist:
        data_q.put(imgName(iimg, dirname))
    simglist.clear()

    data_q.join()
    print("entire job took:", time.time()-start)



if __name__ == '__main__':
  main()

