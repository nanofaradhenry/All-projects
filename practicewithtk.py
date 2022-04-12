print("Hello World")
print("Welcome to my program")
from cgitb import text
from inspect import FrameInfo
import time

from tkinter import*
from tkinter import colorchooser
from tkinter.ttk import *

root=Tk()

root.title("First_program")

label=Label(root, text="Hello Everyone !").pack()


time.sleep(2)

label=Label(root, text="Welcome to this new and innovative program").pack()
button= Button(root, text="Click Here!").pack()
label=Label(root, text="check out this menu").pack()
menubar=Menu(background='#d2b48c', foreground='black',activebackground='white', activeforeground='black')
file=Menu(menubar,tearoff=1,background='#ffcc99', foreground='black')
file.add_command("Hello")

root.mainloop()