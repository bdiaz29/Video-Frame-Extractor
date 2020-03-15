from tkinter import *
import PIL
from PIL import Image, ImageGrab, ImageTk
import numpy as np
from tkinter import filedialog
import os.path
from os import path
import xlwt
from tkinter import messagebox
import cv2
overall=1
import time
from random import randint
#value to determine how many frames to skip
skip=0

#assign where the file will be saved.
def assign_destination():
    global destination
    global name
    name = name_txt.get()
    dest_String = filedialog.askdirectory()
    destination = dest_String + "/extracted_" + name + "/"
#assign the source file
def assign_source():
    global source
    global file_list
    source = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4","*.mp4"),("avi","*.avi"),("all files","*.*")))

def extract():
    global destination
    global name
    global overall
    global limit_skip2
    global limit_txt
    global source
    #make new folder if it doesn't exist already
    if not os.path.isdir(destination):
        os.mkdir(destination)
    skip=int(limit_skip2.get())
    name=name_txt.get()
    counter=0
    # get the number of frames to skip from the text entry
    limit=int(limit_txt.get())
    vidcap = cv2.VideoCapture(source)
    success, image = vidcap.read()
    #count variable to label file names
    #count started at 1000000
    count = 1000000
    FPS=0
    while success:
        A = time.time()
        if counter > limit and (count-1000000)>=skip:
            cv2.imwrite(destination + "/" + name +"frame%d.jpg" % count,
                        image)  # save frame as JPEG file
            counter=0
            print('Read a new frame , FPS:', str(FPS))
            count += 1
        else:
            P=0
            count += 1
        counter=counter+1
        success, image = vidcap.read()
        B = time.time()
        C=A-B
        if B-A==0:
            FPS=0
        else:
            FPS=1/(B-A)
    print("done")
    overall=overall+1


window = Tk()
window.title("frame extracting application")
window.geometry('750x750')
source=""
destination=""
name=""

file_frame = Frame(master=window)
file_frame.grid(column=0, row=0)


destination_btn = Button(file_frame, text="destination", command=assign_destination)
destination_btn.grid(column=0, row=1)
destination_lbl = Label(file_frame, text="destination")
destination_lbl.grid(column=1, row=1)
name_lbl = Label(file_frame, text="Project Name")
name_lbl.grid(column=2, row=2)
name_txt = Entry(file_frame, width=25)
name_txt.grid(column=3, row=2)

start_btn = Button(file_frame, text="start", command=extract)
start_btn.grid(column=0, row=3)

lbl_limit=Label(file_frame,text="skip frame")
lbl_limit.grid(column=0, row=4)
limit_txt=Entry(file_frame, text="entry")
limit_txt.grid(column=1, row=4)
limit_txt.insert(END,0)


lbl_skip=Label(file_frame,text="skip to frame")
lbl_skip.grid(column=0, row=5)

limit_skip2=Entry(file_frame, text="entry2")
limit_skip2.grid(column=1, row=5)
limit_skip2.insert(END,"0")


source_btn = Button(file_frame, text="source", command=assign_source)
source_btn.grid(column=0, row=0)
source_lbl = Label(file_frame, text=source)
source_lbl.grid(column=1, row=0)

window.mainloop()