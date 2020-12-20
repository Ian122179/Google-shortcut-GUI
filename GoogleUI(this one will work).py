import os
import time
import tkinter as tk
import webbrowser
from tkinter import PhotoImage

height = 600
width = 360
root = tk.Tk()
#image: PhotoImage = tk.PhotoImage(file=r"C:\Users\UserName\Downloads\googleIcon (1).png")
#krunker: PhotoImage = tk.PhotoImage(file=r"C:\Users\UserName\OneDrive\Desktop\krunkerIcon.png")
#go: PhotoImage = tk.PhotoImage(file=r"C:\Users\inven\UserName\Desktop\arrowIcon.png")
#minec: PhotoImage = tk.PhotoImage(file=r"C:\Users\inven\Username\Pictures\minelcon.png")
userentry = tk.StringVar(root)
#the lines above are picture files you have to have pictures with the same path and unhashtag them to use them
answer = 3
root.title('Google Search-ui')


def clicked():
    webbrowser.open("https://www.google.com/search?rlz=1C1UEAD_enUS931US931&sxsrf=ALeKk01F9CUdScJJFMpv-5HoEyg4ECJX1w%3A1607912644518&ei=xMzWX-nUHoz0tAaoionIBA&q=")




def search():
    url = str(userentry.get())
    webbrowser.open("https://www.google.com/search?rlz=1C1UEAD_enUS931US931&sxsrf=ALeKk01F9CUdScJJFMpv-5HoEyg4ECJX1w%3A1607912644518&ei=xMzWX-nUHoz0tAaoionIBA&q=" + url)


def krumand():
    webbrowser.open("https://krunker.io")

#def mine():
    #os.startfile("C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe")
# launches minecraft java remove the hashtags above to use the code

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

entry = tk.Entry(frame, bg='#e3e3e3', textvariable=userentry, borderwidth=0)
entry.place(height=30, relwidth=0.6, rely=.4, relx=0.15)

chrome = tk.Button(frame, text="chrome", bg='white', fg='blue', command=clicked, borderwidth=0)#replace text="chrome" with image=image to use the chrome image
chrome.place(relx=0.15, rely=0.475)

krunkerB = tk.Button(frame, text="krunker", command=krumand, borderwidth=0, bg='white')#replace text="krunker" with image=krunker to use the krunker image
krunkerB.place(relx=.4, rely=.475)

minecraft = tk.Button(frame, text="minec", borderwidth=0, bg='white')#replace text="minec" with image=minec to use the minecraft image you also need to add command=mine
minecraft.place(relx=.65, rely=.475)
#you will aslo have to have minecraft java to be installed in the right location for this to do anything

def Update():

    current_time = time.strftime("%I:%M")#, t)
    label.config(text=current_time)
    label.after(500, Update)


label = tk.Label(frame, text="", font=("Helvetica", 40), bg='white')
label.place(rely=.27, relx=.35)

#label.after(500, Update)

search = tk.Button(frame, text="go", command=search, borderwidth=0)#replace text="go" with image=go to use the go image
search.place(relx=.75, rely=.4)

Update()

root.mainloop()
