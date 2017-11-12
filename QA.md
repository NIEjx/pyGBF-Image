GBF-Image Q&A
========================
update: 2017/11/10

Q：怎么运行？  
A：安装python3以上版本，安装beautifulsoup库，之后就可以运行。

Q：下载不了全部图片  
A：把log.txt删掉，再重新运行就可以。

Q：log.txt怎么看  
A：第一行是对应文件夹和子文件夹，其中chara是角色全身图，quest是任务半身图，zoom是角色放大图，cover是首页角色图，summon是召唤石图 class是主角职业图，bg是游戏首页的背景图。R SR SSR是对应稀有度，extra则是任务中出现的角色（有主线支线活动的人物，也有星晶兽）。  
第二行是当前下载的最新图片的序号。  
例如，ssr任务半身图的序号就是第二行第七个数据。
>chara[R/SR/SSR/skin] quest[r/sr/ssr/extra] summon[n/r/sr/ssr] zoom[r/sr/ssr/skin] cover[r/sr/ssr/skin] class cover[class] bg chara[extra] zoom[extra]

Q:只想下载某部分图片  
A:可以参考把log里面对应数据以外的值改成最新的，对应数据改成0或者你想开始下载的编号。

Q:实在下载不了或者不想安装python
A:可以用下载工具批量下载link文件夹中对应文件的下载链接。查找单张图片则可以参考 [碧蓝幻想立绘](niejx.com/gbfimage)
