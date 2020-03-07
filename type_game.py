from tkinter import *
from math import *
import tkinter.messagebox
import os
#import pyttsx3
#import pyttsx3.drivers
import win32com.client
#import cv2
#程序开启语音欢迎语
speaker=win32com.client.Dispatch("SAPI.SpVoice")
#engine=pyttsx3.init()
#rate=engine.getProperty('rate')
#engine.getProperty('rate',rate-80)
#engine.setProperty('rate', rate - 50)
speaker.Speak("hello,baby,let's play games,please fill the word as the picture showed!")
#engine.runAndWait()
#读入图片库中的所有图片
images=[]
for file in os.listdir("D:\python\projects\program0003/pic"):
    images.append(file)
#拆分文件名和后缀,获取文件名
filenames=[]
for img in images:
    img_name=(img.split("."))[0]
    filenames.append(img_name)
#获取图片个数
Max_num=len(images)
#建立主窗口
window=Tk()
window.title("pepper's game")
window.geometry("680x490+500+300")

n=0
#定义回调函数,用configure来替换图片
def func():
    global n
    global picc
    if n==Max_num-1:
        imageLabel.configure(image=win_pic)
        notice.configure(text="congratulations!!!")
        e.set("congratulations!!!")
        speaker.Speak("congratulations,baby,you win the games，hooray.")
    else:
        if e.get()!=filenames[n]:#利用Variable()获取entry内部text
            tkinter.messagebox.showerror(title="Error",message="You are wrong!!!")#利用messagebox,在输入与图片内容不符时，弹出error对话框
            e.set("")#将输入文本清空
            speaker.Speak("Oh,no,you are wrong,try again.")
        else:
            notice.configure(text=("type "+filenames[n+1]+" below!"))
            e.set("")
            picc=PhotoImage(file=r"D:\python\projects\program0003/pic/"+images[n+1])
            imageLabel.configure(image=picc)
            speaker.Speak(filenames[n+1])
            n=n+1
        #n=n+1
        #if n==Max_num-1:
       #     n=0
        #else:
            #picc=PhotoImage(file="./pic/banana.png")
            #imageLabel.configure(image=picc)
            #notice.configure(text=("type "+filenames[n+1]+" below!"))
            #e.set("")

#显示图片
pic=PhotoImage(file=r"D:\python\projects\program0003/pic/"+images[0])
imageLabel=Label(window,image=pic)
imageLabel.place(x=200,y=0)

win_pic=PhotoImage(file=r"D:\python\projects\program0003/win/结衣.png")

notice=Label(window,text="type apple below!",font=("黑体",14))
notice.place(x=260,y=235)

e=Variable()
entry=Entry(window,show=None,textvariable=e,bg='yellow')
entry.place(x=260,y=258)

act_bnt=Button(window,text="OK",bg="pink",command=func,width=10,height=2)
act_bnt.place(x=180,y=400)


window.mainloop()