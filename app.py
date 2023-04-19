from tkinter import *
from tkinter import ttk
import main
win = Tk()
win.geometry("1280x720")
win.title("Weather App")
win.resizable(False,False)

entry= Entry(win, width= 40)
entry.pack()

win.mainloop()