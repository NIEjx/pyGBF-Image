GBF-Image Q&A
========================
update: 2017/11/14

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

Q:下载不了图片  
A:
* 先检查自己的python版本是否是python3。
* 复制任意一行link里面的链接，看自身网络是否能够访问资源（如果访问不了，很可能是网络问题，或者是被自身网络提供商拦截了）
* 打开脚本文件，把开头的DEBUG = False 改成 DEBUG = True。（注意大小写）。删除文件夹内的err.txt再运行一次。
* 看错误信息err.txt，自己解决不了的，可以将err.txt,py文件，包含整个文件夹的屏幕截图，脚本运行的cmd截图一起发送到 njx901 at 126.com。截图时请注意匿名化，我也保证不会将相关文件用于debug以外其他用途。err.txt仅记录脚本运行的输出，并不包含系统信息和个人信息，请放心。
