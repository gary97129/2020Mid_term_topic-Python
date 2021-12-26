from pygame import mixer
from gtts import gTTS
from googletrans import Translator 
import speech_recognition     #SpeechRecognition
import tempfile
import tkinter as tk  
import tkinter.ttk as tt
from tkinter import *
import random
import time

def app1(LAN,t):
    try:
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            app2(t,"zh-TW")
            audio = r.listen(source)
            return r.recognize_google(audio,language = LAN)
    except speech_recognition.UnknownValueError:
        app2("無法辨識","zh-TW")
    except speech_recognition.RequestError as e:
        app2("無回應:"+ e,"zh-TW")
          
def app2(t,TRAN_LAN):
    mixer.init()
    with tempfile.NamedTemporaryFile(delete='True') as fp:
        tts = gTTS( text=t , lang = TRAN_LAN)
        tts.save("%s.mp3"% (fp.name))
        mixer.music.load("%s.mp3"%(fp.name))
        mixer.music.play()



def window1():
    trans = Translator()
    stdGrade = ['中文','英文','日文','韓文','越南文']
    stdGrade2 = ['zh-TW','en','ja','ko','vi']
    t=""
    
    def app1_0(LAN):
        return stdGrade2[stdGrade.index(LAN)]
        
    def app1_1(LAN):
        global t
        app1(LAN,"講話")
        labGrade.delete(1.0,"end")
        labGrade.insert(1.0, t) 
        
    def app1_2(LAN):
        t = labGrade.get(1.0,"end")
        t = trans.translate(t, dest=LAN).text
        labelExample.delete(1.0,"end")
        labelExample.insert(1.0, t)
        app2(t,LAN)
    
    def app1_3(LAN,TRAN_LAN):
            comGrade1.current(TRAN_LAN)
            comGrade2.current(LAN)
            
    
    #----------------------------------------------------------------------------------------
    window1 = tk.Tk()            #宣告window為視窗物件
    window1.title('翻譯程式')   #設定視窗標題
    
    #視窗大小
    window1.state("zoomed")
    #window1.geometry("400x300")             #寬x高
    #window1.minsize(width=400,height=320)   #最小範圍
    #window1.maxsize(width=1024,height=768)  #最大範圍
    window1.resizable(1,1) #1=True,0=False  是否調整大小 resizable(width,height)
    
    #顏色
    window1.config(bg="#F5DEB3")       #config(bg='背景顏色') 可以填入顏色或是色碼
    
    #透明度
    window1.attributes("-alpha",1)   #1~0 1是100%完全不透明 0是0%透明，可以輸入小數點
    
    #視窗至頂
    #window1.attributes("-topmost",1)#1=True,0=False
    #-------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------
    Grade = tk.Label(window1 , text = '輸入' , font='PMingLiU 30').place(relx=0.2,rely=0.13)
    labGrade = tk.Text(window1 , font='PMingLiU 20')
    labGrade.place(relx=0.1,rely=0.22,relwidth=0.3,relheight = 0.7)
    comGrade1 = tt.Combobox(window1,state="readonly" ,width=10,font='PMingLiU 20', values=stdGrade)
    comGrade1.current(0)
    comGrade1.place(relx=0.2,rely=0.05)
    #comGrade.place(x=80, y=0, width=50, height=20)
    #comGrade.pack()
    #labGrade.pack()
    #--------------------------------------------------------------------------------------
    Example = tk.Label(window1 , text = '輸出' , font='PMingLiU 30').place(relx=0.7,rely=0.13)
    labelExample = tk.Text(window1 , font='PMingLiU 20',width='40')
    labelExample.place(relx=0.6,rely=0.22,relwidth=0.3,relheight = 0.7)
    comGrade2 = tt.Combobox(window1, state="readonly",font = "PMingLiU 20", width=10, values=stdGrade)
    comGrade2.current(1)
    comGrade2.place(relx=0.7,rely=0.05)
    #labelExample.pack()
    #--------------------------------------------------------------------------------
    btn = tk.Button(window1,text='翻譯',activebackground='#FFFFF0',font='PMingLiU 20', command= lambda: app1_2(app1_0(comGrade2.get())))
    #btn.config(bg='#AFEEEE')      #按鈕的顏色
    btn.place(relx=0.47,rely=0.5)
    #btn.config(width=10,height=1) 
    #--------------------------------------------------------------------------------
    btn1 = tk.Button(window1,text='🎤',activebackground='#FFFFF0',font='PMingLiU 20', command= lambda: app1_1(app1_0(comGrade1.get())))
    #btn.config(bg='#AFEEEE')      #按鈕的顏色
    btn1.place(relx=0.476,rely=0.4)
    #btn.config(width=10,height=1) 
    #--------------------------------------------------------------------------------
    btn2 = tk.Button(window1,text='🔊',activebackground='#FFFFF0',font='PMingLiU 20', command= lambda: app2(labGrade.get(1.0,"end"),app1_0(comGrade1.get())))
    #btn.config(bg='#AFEEEE')      #按鈕的顏色
    btn2.place(relx=0.265,rely=0.13)
    #btn.config(width=10,height=1) 
    #--------------------------------------------------------------------------------
    btn3 = tk.Button(window1,text='🔊',activebackground='#FFFFF0',font='PMingLiU 20', command= lambda: app2(labelExample.get(1.0,"end"),app1_0(comGrade2.get())))
    #btn.config(bg='#AFEEEE')      #按鈕的顏色
    btn3.place(relx=0.765,rely=0.13)
    #btn.config(width=10,height=1) 
    #---------------------------------------------------------------------------------------
    btn4 = tk.Button(window1,text='⇋',font = "PMingLiU 20",activebackground='#FFFFF0' , command= lambda: app1_3(stdGrade.index(comGrade1.get()),stdGrade.index(comGrade2.get())))
    #btn1.config(bg='#AFEEEE')      #按鈕的顏色
    btn4.place(relx=0.47,rely=0.05) 
    btn4.config(width=5) #按鈕的大小
    #btn1.pack() #打包
    #---------------------------------------------------------------------------------------
    btn2 = tk.Button(window1,text='退出',activebackground='#930000',font='PMingLiU 20',bg = 'red' , fg = 'white' , command=window1.destroy)
    #btn1.config(bg='#AFEEEE')      #按鈕的顏色
    btn2.place(relx=0.93,rely=0.93) 
    #btn2.config(width=5,height=1) #按鈕的大小
    #btn1.pack() #打包
    
    
    window1.mainloop()             #循環常駐主視窗
    
def window2():
    az=""
    def app2_1():
        global az
        app2("遊戲開始","zh-TW")
        labGrade["state"] = "normal"
        labGrade.delete(1.0,"end")
        labGrade["state"] = "disabled"
        com["state"] = "disabled"
        btn["state"] = "disabled"
        btn1["state"] = "normal"
        az=str(random.randint(0,9))
        while str(len(az)) != com.get()[0]:
            s = str(random.randint(0,9))
            for i in range(0,len(az)):
                if s == az[i]:
                    break
            else:
                az += s
        print(az)
        
    def app2_2():
        global az
        inp = app1("zh-TW","請說出要猜的數字")
        if len(inp) == int(com.get()[0]):
            c=True
            for i in range(0,len(inp)-1):
                for j in range(i+1,len(inp)):
                    if inp[i] == inp[j] or inp[i]>"9" or inp[i]<"0"or inp[j]>"9" or inp[j]<"0":
                        c=False
                        break
                if c == False:
                    break
            if c == True:
                A = 0
                B = 0
                for i in range(0,len(inp)):
                    for j in range(0,len(az)):
                        if inp[i] == az[j] and i == j:
                            A+=1
                        elif inp[i] == az[j] and i != j:
                            B+=1
                app2(str(A) + "A" + str(B) + "B","zh-TW")
                labGrade["state"] = "normal"
                labGrade.insert(1.0, inp + " " + str(A) + "A" + str(B) + "B" + "  ") 
                labGrade["state"] = "disabled"
                if str(A) == com.get()[0]:
                    app2("你真的好棒棒","zh-TW")
                    com["state"] = "normal"
                    btn["state"] = "normal"
                    btn1["state"] = "disabled"
            else:
                 app2("輸入錯誤","zh-TW")   
        else:
            app2("輸入錯誤","zh-TW")
           
    window2 = tk.Tk()            #宣告window為視窗物件
    window2.title('1 A 2 B')   #設定視窗標題
    
    #視窗大小
    window2.state("zoomed")
    #window1.geometry("400x300")             #寬x高
    #window1.minsize(width=400,height=320)   #最小範圍
    #window1.maxsize(width=1024,height=768)  #最大範圍
    window2.resizable(1,1) #1=True,0=False  是否調整大小 resizable(width,height)
    
    #顏色
    window2.config(bg="#F5DEB3")       #config(bg='背景顏色') 可以填入顏色或是色碼
    
    #透明度
    window2.attributes("-alpha",1)   #1~0 1是100%完全不透明 0是0%透明，可以輸入小數點
    
    #視窗至頂
    #window2.attributes("-topmost",1)#1=True,0=False
    #-------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------
    labGrade = tk.Text(window2 , font='PMingLiU 30',state = "disabled")
    labGrade.place(relx=0.1,rely=0.23,relwidth=0.8,relheight = 0.72)
    com = tt.Combobox(window2,state="readonly" ,width=10,font='PMingLiU 20', values=["3位數","4位數","5位數"])
    com.current(0)
    com.place(relx=0.443,rely=0.05)
    #comGrade.place(x=80, y=0, width=50, height=20)
    #comGrade.pack()
    #labGrade.pack()
    #labelExample.pack()
    #--------------------------------------------------------------------------------
    btn = tk.Button(window2,text='開始遊戲',activebackground='#FFFFF0',font='PMingLiU 20', command= lambda: app2_1())
    #btn.config(bg='#AFEEEE')      #按鈕的顏色
    btn.place(relx=0.452,rely=0.13)
    #btn.config(width=10,height=1) 
    #--------------------------------------------------------------------------------
    btn1 = tk.Button(window2,text='我要猜',activebackground='#FFFFF0',font='PMingLiU 20',state = "disabled", command= lambda: app2_2())
    #btn.config(bg='#AFEEEE')      #按鈕的顏色
    btn1.place(relx=0.7,rely=0.09)
    #btn.config(width=10,height=1) 
    #---------------------------------------------------------------------------------------
    btn2 = tk.Button(window2,text='退出',activebackground='#930000',font='PMingLiU 20',bg = 'red' , fg = 'white' , command=window2.destroy)
    #btn1.config(bg='#AFEEEE')      #按鈕的顏色
    btn2.place(relx=0.93,rely=0.93) 
    #btn2.config(width=5,height=1) #按鈕的大小
    #btn1.pack() #打包
    
    
    window2.mainloop()             #循環常駐主視窗
  
    
    
def window3():
    az=""
    a=""
    b=""
    def app3_1():
        global az,a,b
        if len(ttext.get()) == 7:
            a = ttext.get()[:3]
            b = ttext.get()[-3:]
            for i in range(0,3):
                if a[i] > "9" or a[i]<"0" or b[i] > "9" or b[i]<"0":
                    return app2("輸入錯誤",'zh-TW')
            if a>b :
                a,b=int(b),int(a)
            else:
                a,b=int(a),int(b)
            ttext["state"] = "disabled"
            btn["state"] = "disabled"
            btn1["state"] = "normal"
            lab["text"] = "範圍是%s-%s之間"%(a,b)
            app2("遊戲開始",'zh-TW')
            az = random.randint(a, b)
            print(az)
        else:
            app2("輸入錯誤",'zh-TW')
            
    def app3_2():
        global az,a,b            #區域轉全域
        t = app1("zh-TW",lab.cget('text'))
        print(t)
        time.sleep(1)
        if len(t) == 3:
            for i in range(0,3):
                if t[i]>"9" or t[i]<"0":
                    return app2("輸入錯誤",'zh-TW')
            t= int(t)
            if a>=t or b<=t:
                app2("輸入錯誤",'zh-TW')
            elif t < az:
                a = t
            elif t > az:
                b = t
            elif t == az:
                ttext["state"] = "normal"
                btn["state"] = "normal"
                btn1["state"] = "disabled"
                lab["text"] = "請輸入100-999之間"
                return app2("你真的好棒棒","zh-TW")
            lab["text"] = "範圍是%s-%s之間"%(a,b)
        else:
            app2("輸入錯誤",'zh-TW')
    window3 = tk.Tk()            #宣告window為視窗物件
    window3.title('終極密碼')   #設定視窗標題
    
    #視窗大小
    window3.state("zoomed")
    #window1.geometry("400x300")             #寬x高
    #window1.minsize(width=400,height=320)   #最小範圍
    #window1.maxsize(width=1024,height=768)  #最大範圍
    window3.resizable(1,1) #1=True,0=False  是否調整大小 resizable(width,height)
    
    #顏色
    window3.config(bg="#F5DEB3")       #config(bg='背景顏色') 可以填入顏色或是色碼
    
    #透明度
    window3.attributes("-alpha",1)   #1~0 1是100%完全不透明 0是0%透明，可以輸入小數點
    
    #視窗至頂
    #window3.attributes("-topmost",1)#1=True,0=False
    #-------------------------------------------------------------------------------
    ttext = tk.Entry(window3 ,width = "7", font='PMingLiU 30')
    ttext.insert("1","100-999")
    ttext.place(relx=0.4,rely=0.3)
    #-------------------------------------------------------------------------------
    lab = tk.Label(window3 ,text='請輸入100-999之間', font='PMingLiU 50')
    lab.place(relx=0.3,rely=0.1)
    
    #--------------------------------------------------------------------------------
    btn = tk.Button(window3,text='確定',activebackground='#FFFFF0',font='PMingLiU 20', command= lambda: app3_1())
    #btn.config(bg='#AFEEEE')      #按鈕的顏色
    btn.place(relx=0.5,rely=0.3)
    #btn.config(width=10,height=1) 
    #--------------------------------------------------------------------------------
    btn1 = tk.Button(window3,text=' 我   要   猜 ',activebackground='#FFFFF0',font='PMingLiU 30',state = "disabled", command= lambda: app3_2())
    #btn.config(bg='#AFEEEE')      #按鈕的顏色
    btn1.place(relx=0.4,rely=0.45)
    #btn.config(width=10,height=1) 
    #---------------------------------------------------------------------------------------
    btn2 = tk.Button(window3,text='退出',activebackground='#930000',font='PMingLiU 20',bg = 'red' , fg = 'white' , command=window3.destroy)
    #btn1.config(bg='#AFEEEE')      #按鈕的顏色
    btn2.place(relx=0.93,rely=0.93) 
    #btn2.config(width=5,height=1) #按鈕的大小
    #btn1.pack() #打包
    
    
    window3.mainloop()             #循環常駐主視窗
        
        

window = tk.Tk()            #宣告window為視窗物件
window.title('選單')   #設定視窗標題
    
#視窗大小
#window.state("zoomed")
window.geometry("300x280")             #寬x高
#window.minsize(width=400,height=320)   #最小範圍
#window.maxsize(width=1024,height=768)  #最大範圍
window.resizable(0,0) #1=True,0=False  是否調整大小 resizable(width,height)
    
#顏色
window.config(bg="#F5DEB3")       #config(bg='背景顏色') 可以填入顏色或是色碼
    
#透明度
window.attributes("-alpha",1)   #1~0 1是100%完全不透明 0是0%透明，可以輸入小數點
    
#視窗至頂
#window.attributes("-topmost",1)#1=True,0=False 
    
ap1 = tk.Button(window,text='翻譯程式',activebackground='#FFFFF0',font='PMingLiU 20', command= lambda: window1())
#ap1.config(bg='#AFEEEE')      #按鈕的顏色
ap1.place(relx=0.27,rely=0.1)
#ap1.config(width=10,height=1) 

ap2 = tk.Button(window,text='  1 A 2 B ',activebackground='#FFFFF0',font='PMingLiU 20', command= lambda: window2())
#ap2.config(bg='#AFEEEE')      #按鈕的顏色
ap2.place(relx=0.27,rely=0.4)
#ap2.config(width=10,height=1) 

ap2 = tk.Button(window,text='終極密碼',activebackground='#FFFFF0',font='PMingLiU 20', command= lambda: window3())
#ap2.config(bg='#AFEEEE')      #按鈕的顏色
ap2.place(relx=0.27,rely=0.7)
#ap2.config(width=10,height=1) 

window.mainloop()