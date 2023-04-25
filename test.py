from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk
from datetime import time
import main

root = Tk("Weather app")
root.title("Weather app")
root.geometry("1280x720")
root.configure(bg="#57adff")

root.resizable(False,False)


time_now = datetime.now().time().isoformat(timespec="minutes")
now = datetime.strptime(str(time_now),"%H:%M")
time_12_format = now.strftime("%I:%M %p")

##icon
Image_icon = PhotoImage(file="icons/logo.png")
root.iconphoto(False,Image_icon)

# Round_box= PhotoImage(file="icons\Rounded Rectangle 2.png")
# Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)


#label
label1 = Label(root,text=f"Temperature : ",font=('Helvetica',15,"bold"),fg="black",bg="#57adff")
label1.place(x=70,y=240)

label1 = Label(root,text="Humidity",font=('Helvetica',15,"bold"),fg="black",bg="#57adff")
label1.place(x=70,y=280)

label1 = Label(root,text="Wind_speed",font=('Helvetica',15,"bold"),fg="black",bg="#57adff")
label1.place(x=70,y=320)

label1 = Label(root,text="Pressure",font=('Helvetica',15,"bold"),fg="black",bg="#57adff")
label1.place(x=70,y=360)

label1 = Label(root,text="Visibility",font=('Helvetica',15,"bold"),fg="black",bg="#57adff")
label1.place(x=70,y=400)

label1 = Label(root,text="Description",font=('Helvetica',15,"bold"),fg="black",bg="#57adff")
label1.place(x=70,y=440)


##Search box
Search_box = PhotoImage(file="icons\Rounded Rectangle 3.png")
my_image = Label(image=Search_box,bg="#57adff")
my_image.place(x=620,y=120)

weat_image = PhotoImage(file="icons/Layer 7.png")
weatherImage = Label(root,image=weat_image,bg="#203243")
weatherImage.place(x=670,y=134)

textfield = tk.Entry(root,justify="center",width=18,font=("poppins",25,"bold"),bg="#203243",border=0,fg="white")
textfield.place(x=710,y=136)
textfield.focus()

Search_icon = PhotoImage(file="icons/Layer 6.png")
myImage_icon = Button(root,image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=main.get_weather(textfield.get()))
myImage_icon.place(x=1010,y=134)


## Bottom Box
frame = Frame(root,width=1280,height=180,bg="#203243")
frame.pack(side=BOTTOM)

#bottom boxes
first_box = PhotoImage(file="icons\Rounded Rectangle 2.png")
second_box = PhotoImage(file="icons\Rounded Rectangle 2 copy.png")

Label(frame,image=first_box,bg="#212120").place(x=30,y=20)
Label(frame,image=second_box,bg="#212120").place(x=300,y=30)
Label(frame,image=second_box,bg="#212120").place(x=400,y=30)
Label(frame,image=second_box,bg="#212120").place(x=500,y=30)
Label(frame,image=second_box,bg="#212120").place(x=600,y=30)
Label(frame,image=second_box,bg="#212120").place(x=700,y=30)
Label(frame,image=second_box,bg="#212120").place(x=800,y=30)
Label(frame,image=second_box,bg="#212120").place(x=900,y=30)


#clock 
clock = Label(root,text=f"{time_12_format}",font=("Helvetica",40,"bold"),fg="white",bg="#57adff")
clock.place(x=100,y=80)


root.mainloop()
