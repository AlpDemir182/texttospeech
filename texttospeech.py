from tkinter import *
#from tkinter.ttk import *
import tkinter.font as f
from gtts import gTTS
import os

root = Tk()
root.geometry("1000x1000")
root.title("TextToSpeech")
root.config(background="White")

def play():
    language = "en"
    myobject = gTTS(text = textentry.get(), lang= language, slow = False)
    myobject.save("converted.wav")
    os.system("converted.wav")



frame1 = Frame(root, bg = "green", height = "250")
frame1.pack(fill = X)

frame2 = Frame(root, bg = "cyan", height = "750")
frame2.pack(fill = X)

label1 = Label(frame1, text = "Text to Speech", font = ("Arial", 60), foreground= "white", background= "green")
label1.place(x=290, y= 80)

label2 = Label(frame2, text = "Enter text here:", font = ("Arial", 30), foreground = "black", background="cyan")
label2.place(x=150, y= 50)

textentry = Entry(frame2, width = 50, foreground = "black", background = "white")
textentry.place(x=250, y=100)



submitbutton = Button(frame2, text = "Submit", font = ("Arial", 30), command = play)
submitbutton.place(x=400, y=500)
root.mainloop()