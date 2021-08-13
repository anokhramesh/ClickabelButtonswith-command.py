#Create Clicable buttons with command in tkinter.
from tkinter import *
root =Tk()
root.title("PYSERIAL APP")
root.geometry("900x200")# frame size
Label(root, text="ANOKHAUTOMATION",bg="pink",fg="blue",font="Times 20 bold").pack()
def load1on():# function for Load 1 ON
    print("Load 1 is Turnd ON")
def load1off():# function for Load 1 OFF
    print("Load 1 is Turnd OFF")
def load2on():# function for Load 2 ON
    print("Load 2 is Turnd ON")
def load2off():# function for Load 2 OFF
    print("Load 1 is Turnd OFF")
frame = Frame(root,borderwidth =6,bg="gray",relief=SUNKEN)
frame.pack(side =LEFT,anchor ="nw")#nw is north west
# Button 1
b1 = Button(frame ,bg="yellow",fg="red",text="LOAD 1 ON",font="Times 20 bold",command =load1on)
b1.pack(side=LEFT,padx=20)
# Button 2
b2 = Button(frame ,bg="#34ebe5",fg="#eb34d2",text="LOAD 1 OFF",font="Times 20 bold",command =load1off)
b2.pack(side=LEFT,padx=20)
# Button 3
b3 = Button(frame ,bg="yellow",fg="red",text="LOAD 2 ON",font="Times 20 bold",command =load2on)
b3.pack(side=LEFT,padx=20)
# Button 4
b4 = Button(frame ,bg="#34ebe5",fg="#eb34d2",text="LOAD 2 OFF",font="Times 20 bold",command =load2off)
b4.pack(side=LEFT,padx=20)

root.mainloop()
