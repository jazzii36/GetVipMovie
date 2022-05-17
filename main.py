# -*- coding: utf-8 -*-

import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from tkwebview2.tkwebview2 import WebView2

windows=Tk()
windows.title("vip视频播放器")
windows.geometry("1200x800+200+200")

#创建菜单实例
menubar=Menu(windows,tearoff=False)
#创建菜单1实例
menu1=Menu(menubar,tearoff=False)
menu1.add_command(label="登陆")
menu1.add_separator ()
menu1.add_command(label="exit",command=windows.quit)
menubar.add_cascade(label="菜单",menu=menu1)
#创建菜单2实例
menu2=Menu(menubar,tearoff=False)

menu2.add_command(label="使用说明")

menu2.add_command(label="检查更新")
menubar.add_cascade(label="帮助",menu=menu2)

#创建主体frame
mainframe=tkinter.Frame(windows,background="#FFFFFF")
mainframe.pack(fill="both",expand=True)

# webview布局
frame_titte=tkinter.Frame(mainframe,height=75,background="#EAEAEF")
frame_titte.pack(fill="both",side='top',expand=1)
wb = WebView2(frame_titte, 1200, 750)
wb.pack(side='left', fill="both", expand=1)

#创建底部frame窗口
frame_down=tkinter.Frame(mainframe,height=75,background="#EAEAEF")
frame_down.pack(fill="x",side=BOTTOM,expand=0)
#底部frame布局
l1=Label(frame_down,text='请输入要解析的URl').pack(side=LEFT,ipady=30,ipadx=10)
E1=Entry(frame_down,bd=0,width=40,xscrollcommand=True)
E1.pack(side=LEFT,padx=1)

datalist={"1【直解】VIP万能解析原画":"https://jx.aidouer.net/?url=","2【直接搜索视频名称】vip解析影院":"https://z1.m1907.cn/?jx=","3【全网VIP解析】":"https://parse.mw0.cc/?url=","4【推荐】vip解析":"https://api.leduotv.com/wp-api/ifr.php?vid=","5【OK万能视频解析】":"https://okjx.cc/?url=","6【云端视频解析】":"https://sb.5gseo.net/?url=","7【BL视频解析】":"https://svip.bljiex.cc/?url=","8【云VIP解析】":"https://jx.iztyy.com/svip/?url=","9【虾米视频解析】":"https://jx.xmflv.com/?url=","10【七彩vip解析】":"https://jx.xymav.com/?url=","11【无名解析小站】":"https://www.administratorw.com/video.php?url=","12【全民解析接口】":"https://jx.618g.com/?url=","13【盘古解析】":"https://www.pangujiexi.com/pangu/?url=","14【视频解析接口】":"https://660e.com/?url="}
yuanlist=ttk.Combobox(frame_down,state='readonly',width=30,values=list(datalist.keys()))
yuanlist.current(0)
yuanlist.pack(side=LEFT,padx=6)


#播放视频
def webview():
    url1key =yuanlist.get()
    url1=datalist[url1key]
    url2 = E1.get()
    finalurl = str(url1) + str(url2)
    wb.load_url(url=finalurl)
    print("播放成功")

button=Button(frame_down,text='播放',bd=1,bg="#336699",fg='#FFFFFF',width=5,command=webview)
button.pack(side=LEFT,padx=6)

windows.config(menu=menubar)
windows.mainloop()