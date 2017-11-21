GBF-Image
========================
update: 2017/11/20

This is a downloader for GranBlue Fantasy(Cygames Inc.)
* Language python 3.7
* Require: BeautifulSoup4
##### How to use
* run "pyGBFRES.py" in command line
* 在命令行运行"pyGBFRES.py"
* smart start for the last download index(logged in log.txt in the same dir)
* 下载完成后会记录下载进度到log文件，下次下载会自动从该位置开始。
* Please delete /img if you want to obtain the whole image set.
* 如要下载完整图包，请删掉img 文件夹再运行脚本。
* pyGBFxxx are scripts for one single part of the whole set.
* pyGBFxxx脚本可以下载单独某个部分，bg代表背景，chara代表角色立绘，mainchara代表露莉亚和比，exchara是人物编外立绘，class代表主角职业，summon代表召唤石，weapon代表武器。
* Any questions please check QA.md
* 有任何疑问可以参考QA.md
##### Download what
* characters
* class
* summmon stones
* quest(with emotion subfix)
* skin
* mypage
* background
* weapon
##### History Version
* v4.0 2017/11/20 refresh the whole project
* v3.3 2017/11/19 add weapon download(please run pyGBFweapon.py)
* v3.2.1 2017/11/12 add download linkfile set
* v3.2 2017/11/08 add 1 [top background],2 [zoom]&[b] of extra characters
* v3.1 2017/10/24 update new job and skin address
* v3.1 2017/09/09 update log.txt file 
* v3 auto update to the latest resource
* v2 split index control easier to reach
* v1 downloader
##### Appendix
http://niejx.com/gbfimage
* a website powered by JEANNE which for game resource search

###### list
* weapon
    * http://game-a1.granbluefantasy.jp/assets/img/sp/assets/weapon/m/1040001600.jpg
    * http://game-a.granbluefantasy.jp/assets/img/sp/assets/weapon/b/1040001600.png
    * http://game-a.granbluefantasy.jp/assets/img/sp/assets/weapon/ls/1040500300.jpg
* image set
    * character origin zoom skin
    * http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/zoom/3040010000_01.png
    * http://game-a.granbluefantasy.jp/assets/img/sp/assets/npc/b/3030007000_01.png
* class
    * http://game-a1.granbluefantasy.jp/assets/img/sp/assets/leader/job_change/120001_wa_1_01.png
    * http://game-a1.granbluefantasy.jp/assets/img/sp/cjs/job_release_180001_1_c.png
* quest character 2 3 4 99
    * http://game-a1.granbluefantasy.jp/assets/img/sp/quest/scene/character/body/3040022000.png
* summon 1 2 3 4
    * http://game-a.granbluefantasy.jp/assets/img/sp/assets/summon/b/2030011000.png
* mypage class&sr
    * http://game-a1.granbluefantasy.jp/assets/img/sp/assets/npc/my/3040058000_02.png
    * http://game-a1.granbluefantasy.jp/assets/img/sp/assets/leader/my/140201_kn_1_01.png
* not used
    * http://game-a1.granbluefantasy.jp/assets/img/sp/assets/npc/npc_evolution/main/3040071000_02.png
