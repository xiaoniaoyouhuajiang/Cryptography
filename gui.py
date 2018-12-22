# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:23:50 2018

@author: 小鸟游花酱
"""

from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
from des_2 import *

LARGE_FONT= ("Verdana", 20)

class Application(tk.Tk):
    def __init__(self):
        
        super().__init__()

        self.wm_title("加密器")
            
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #循环功能界面
        for F in (StartPage, PageOne, PageTwo,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(StartPage)

        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处

#主页面
class StartPage(tk.Frame):
    '''主页'''
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="DES加密器\r作者：201611921223", font=LARGE_FONT)
        label.pack(pady=100)
        ft2=tkFont.Font(size=16)
        Button(self, text="加密",font=ft2,command=lambda: root.show_frame(PageOne),width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        Button(self, text="解密",font=ft2,command=lambda: root.show_frame(PageTwo),width=30,height=2).pack()
        Button(self,text='退出系统',height=2,font=ft2,width=30,command=root.destroy,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        
    
#加密的界面
class PageOne(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="加密", font=LARGE_FONT)
        label.pack(pady=100)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        Label(self,text='请输入明文：',font=ft3).pack(side=TOP)
        global e1
        e1= StringVar()
        entry1=Entry(self,textvariable =e1,width=30,font=ft3,bg='Ivory')
        entry1.pack(side=TOP)
        Label(self,text='请输入单位为8的密钥：',font=ft3).pack(side=TOP)
        global e2
        e2=StringVar()
        entry2=Entry(self,textvariable=e2,width=30,font=ft3,bg='Ivory')
        entry2.pack(side=TOP)
        self.labelnum=StringVar()
        self.labelnum.set('---')
        Label(self,textvariable=self.labelnum,font=ft3,bg='Ivory').pack(side=TOP)
        Button(self, text="输出密文",width=8,font=ft4,command=self.get_miwen).pack(side=TOP)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=20)

    def get_miwen(self):
        text = str(e1.get())
        length = len(text)
        Result=""
        text=text+(length%4)*" "
        length=len(text)
        key = str(e2.get())
#        while(len(key)!=8):
#            self.labelnum.set('请输入8位密码！！')
        for i in range(int(length/4)):
            tempText=[text[j] for j in range(i*4,i*4+4)]
            Result="".join([Result,DES(tempText,key,int(0))])
        self.labelnum.set(str(Result))
        self.clipboard_clear()
        self.clipboard_append(str(Result))
        
        
            
#解密的界面
class PageTwo(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="加密", font=LARGE_FONT)
        label.pack(pady=100)
        ft3=tkFont.Font(size=14)
        ft4=tkFont.Font(size=12)
        Label(self,text='请输入密文：',font=ft3).pack(side=TOP)
        global e3
        e3= StringVar()
        global entry3
        entry3=Entry(self,textvariable =e3,width=30,font=ft3,bg='Ivory')
        entry3.pack(side=TOP)
        Label(self,text='请输入单位为8的密钥：',font=ft3).pack(side=TOP)
        global e4
        e4=StringVar()
        global entry4
        entry4=Entry(self,textvariable =e4,width=30,font=ft3,bg='Ivory')
        entry4.pack(side=TOP)
        self.labelnum=StringVar()
        self.labelnum.set('---')
        Label(self,textvariable=self.labelnum,font=ft3,bg='Ivory').pack(side=TOP)
        Button(self, text="输出明文",width=8,font=ft4,command=self.get_mingwen).pack(side=TOP)
        Button(self, text="返回首页",width=8,font=ft4,command=lambda: root.show_frame(StartPage)).pack(pady=20)
 
    def get_mingwen(self):
        text = str(e3.get())
        length = len(text)
        Result=""
        text=text+(length%4)*" "
        length=len(text)
        key = str(e4.get())
        while(len(key)!=8):
            self.labelnum.set('请输入8位密码！！')
        for i in range(int(length/8)):
            tempText=[text[j] for j in range(i*8,i*8+8)]
            Result="".join([Result,DES(tempText,key,int(1))])
        self.labelnum.set((str(Result)))
        self.clipboard_clear()
        self.clipboard_append(str(Result))
        

if __name__ == '__main__':
    app=Application()
    app.mainloop()