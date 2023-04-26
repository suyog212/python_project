from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from datetime import *
import requests
import json
import pytz
from PIL import Image,ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)



root = Tk("Weather app")
root.title("Weather app")
root.geometry("1280x720")
root.configure(bg="#57adff")

root.resizable(False,False)
api_key = "e2886abff213b644be43bfc12e3daca1"


#main canvas
# main
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# canvas
my_canvas = Canvas(main_frame,bg="#57adff",height=900)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# scrollbar
my_scrollbar = Scrollbar(main_frame, orient=VERTICAL)
my_scrollbar.pack(side=RIGHT, fill=Y)


#new frame 
# my_frame = Frame(second_canvas)

# add new frame in canvas
# my_canvas.create_window((0,0))


def plot():
    with open("hourly.json","r") as file:
        data = json.load(file)
    # the figure that will contain the plot
    fig = Figure(figsize = (15, 3),dpi = 100)
    x = []
    y = []
    x_names = []
    for i in data:
        x_names.append(str(datetime.fromtimestamp(i["dt"]).time().isoformat("minutes")))
        x.append(i["dt"])
        y.append(i["temp"] - 273.15)
    # list of squares
    # y = [i**2 for i in range(101)]
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(x[::3],y[::3])
    plot1.set_title("Weekly forcast")
    plot1.set_xlabel("Time")
    plot1.set_ylabel("Temperature")
    plot1.set_xticks(x[::4],labels=x_names[::4])

    plot1.savefig('daily_data.png')
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = mat_frame)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack(side=BOTTOM)
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def get_weather():
    city_name = textfield.get()
    geolocator = Nominatim(user_agent="Project")
    location=geolocator.geocode(city_name)
    #API url to fetch data
    base_url = "https://api.openweathermap.org/data/2.5/onecall?lat="
    url = base_url + str(location.latitude) + "&lon="+ str(location.longitude) + "&exclude=minutely&appid=" + api_key + "&units=metric"
    #request object to fetch data from api
    # res = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat_long[0]}&lon={lat_long[1]}&exclude=minutely&appid={api_key}").json()
    res = requests.get(url,timeout=100).json()
    print(url)
    # print(ConnectionRefusedError)
    #Creating and adding data to JSON file
    """json.dumps() function will convert a subset of Python objects into a json string.
    Not all objects are convertible and you may need to create a dictionary
    of data you wish to expose before serializing to JSON."""
    with open("data.json","w",encoding="UTF-8") as file:
        json.dump(res,file)
    file.close()
    with open("data.json",'r') as file_2:
        we_data = json.load(file_2)
    w_time = ["current","hourly","daily"]
    for i in w_time:
        with open(f"{i}.json","w") as sorted_data:
            json.dump(we_data[i],sorted_data)
    with open("current.json","r") as file:
        data = json.load(file)

    with open("hourly.json","r") as file:
        data_hour_1 = json.load(file)
        data_hour = data_hour_1[::2]
    first.config(text=format_time(data_hour[0]['dt']))
    t.config(text=f"{data['temp']} ℃")
    h.config(text=f"{data['humidity']} %")
    w.config(text=f"{data['wind_speed']} m/s")
    p.config(text=f"{data['pressure']} hPa")
    v.config(text=f"{data['visibility']/1000} Km")
    d.config(text=f"{data['weather'][0]['description']}")

    today.config(text=time_12_format)
    #data configs
    today_Bottom.config(text=f"{data['temp']} ℃",font=("Helvetica",22,"bold"))
    today_bottom.config(text=f"{data['weather'][0]['description']}",font=("Helvetica",16,"bold"))
    first_bottom.config(text=f"{data_hour[0]['temp']} ℃")
    second.config(text=format_time(data_hour[1]['dt']))
    second_bottom.config(text=f"{data_hour[1]['temp']} ℃")
    third.config(text=format_time(data_hour[2]['dt']))
    third_bottom.config(text=f"{data_hour[2]['temp']} ℃")
    fourth.config(text=format_time(data_hour[3]['dt']))
    fourth_bottom.config(text=f"{data_hour[3]['temp']} ℃")
    fifth.config(text=format_time(data_hour[4]['dt']))
    fifth_bottom.config(text=f"{data_hour[4]['temp']} ℃")
    sixth.config(text=format_time(data_hour[5]['dt']))
    sixth_bottom.config(text=f"{data_hour[5]['temp']} ℃")
    seventh.config(text=format_time(data_hour[6]['dt']))
    seventh_bottom.config(text=f"{data_hour[6]['temp']} ℃")
    eightth.config(text=format_time(data_hour[7]['dt']))
    eightth_bottom.config(text=f"{data_hour[7]['temp']} ℃")
    nineth.config(text=format_time(data_hour[8]['dt']))
    nineth_bottom.config(text=f"{data_hour[8]['temp']} ℃")



    #image icons
    today_Icon = ImageTk.PhotoImage(file=f"icons/{data['weather'][0]['icon']}.png")
    today_image.config(image=today_Icon)
    today_image.image=today_Icon

    first_Icon = ImageTk.PhotoImage(file=f"icons/{data_hour[0]['weather'][0]['icon']}.png")
    first_image.config(image=first_Icon,height=50,width=50)
    first_image.image=first_Icon

    second_Icon = ImageTk.PhotoImage(file=f"icons/{data_hour[1]['weather'][0]['icon']}.png")
    second_image.config(image=second_Icon,height=60,width=60)
    second_image.image=second_Icon

    third_Icon = ImageTk.PhotoImage(file=f"icons/{data_hour[2]['weather'][0]['icon']}.png")
    third_image.config(image=third_Icon,height=60,width=60)
    third_image.image=third_Icon

    fourth_Icon = ImageTk.PhotoImage(file=f"icons/{data_hour[3]['weather'][0]['icon']}.png")
    fourth_image.config(image=fourth_Icon,height=60,width=60)
    fourth_image.image=fourth_Icon

    fifth_Icon = ImageTk.PhotoImage(file=f"icons/{data_hour[4]['weather'][0]['icon']}.png")
    fifth_image.config(image=fifth_Icon,height=60,width=60)
    fifth_image.image=fifth_Icon

    sixth_Icon = ImageTk.PhotoImage(file=f"icons/{data_hour[5]['weather'][0]['icon']}.png")
    sixth_image.config(image=sixth_Icon,height=60,width=60)
    sixth_image.image=sixth_Icon

    seventh_Icon = ImageTk.PhotoImage(file=f"icons/{data_hour[6]['weather'][0]['icon']}.png")
    seventh_image.config(image=seventh_Icon,height=60,width=60)
    seventh_image.image=seventh_Icon

    eightth_Icon = ImageTk.PhotoImage(file=f"icons/{data_hour[7]['weather'][0]['icon']}.png")
    eightth_image.config(image=eightth_Icon,height=60,width=60)
    eightth_image.image=eightth_Icon

    nineth_Icon = ImageTk.PhotoImage(file=f"icons/{data_hour[8]['weather'][0]['icon']}.png")
    nineth_image.config(image=nineth_Icon,height=60,width=60)
    nineth_image.image=nineth_Icon
    
    plot()


def format_time(timestamp):
    time_now = datetime.fromtimestamp(timestamp).time().isoformat(timespec="minutes")
    now = datetime.strptime(str(time_now),"%H:%M",)
    return now.strftime("%I:%M %p")
#reading data from json file



time_now = datetime.now().time().isoformat(timespec="minutes")
now = datetime.strptime(str(time_now),"%H:%M")
time_12_format = now.strftime("%I:%M %p")

##icon
Image_icon = PhotoImage(file="icons/logo.png")
root.iconphoto(False,Image_icon)

# Round_box= PhotoImage(file="icons\Rounded Rectangle 2.png")
# Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)


#labels
label1 = Label(my_canvas,text=f"Temperature : ",font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
t= Label(my_canvas,font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
t.place(x=240,y=240)
label1.place(x=70,y=240)

label1 = Label(my_canvas,text=f"Humidity : ",font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
h= Label(my_canvas,font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
h.place(x=240,y=280)
label1.place(x=70,y=280)

label1 = Label(my_canvas,text=f"Wind_speed : ",font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
w= Label(my_canvas,font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
w.place(x=240,y=320)
label1.place(x=70,y=320)

label1 = Label(my_canvas,text=f"Pressure : ",font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
p= Label(my_canvas,font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
p.place(x=240,y=360)
label1.place(x=70,y=360)

label1 = Label(my_canvas,text=f"Visibility : ",font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
v= Label(my_canvas,font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
v.place(x=240,y=400)
label1.place(x=70,y=400)

label1 = Label(my_canvas,text=f"Description : ",font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
d= Label(my_canvas,font=('Helvetica',18,"bold"),fg="black",bg="#57adff")
d.place(x=240,y=440)
label1.place(x=70,y=440)


##Search box
Search_box = PhotoImage(file="icons\Rounded Rectangle 3.png")
my_image = Label(image=Search_box,bg="#57adff")
my_image.place(x=620,y=120)

weat_image = PhotoImage(file="icons/Layer 7.png")
weatherImage = Label(root,image=weat_image,bg="#203243")
weatherImage.place(x=640,y=130)

textfield = tk.Entry(root,justify="center",width=16,font=("poppins",25,"bold"),bg="#203243",border=0,fg="white")
textfield.place(x=715,y=136)
textfield.focus()

Search_icon = ImageTk.PhotoImage(file="icons/Layer 6.png")
myImage_icon = Button(root,image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",
                      command=get_weather
                      )
myImage_icon.place(x=995,y=125)


#Current weather icon
# curren_icon = PhotoImage(file="icons/01d.png")
# curr_Icon = Label(my_canvas,image=curren_icon,bg="#57adff")
# curr_Icon.place(x=640,y=240)

## Bottom Box
frame = Frame(my_canvas,width=1280,height=170,bg="#203243")
frame.place(x=0,y=530)

#bottom boxes
first_box = PhotoImage(file="icons\Rounded Rectangle 2.png")
second_box = PhotoImage(file="icons\Rounded Rectangle 2 copy.png")
#current weather cell


Label(frame,image=first_box,bg="#212120").place(x=30,y=20)
current_frame = Frame(frame,width=230,height=132,bg="#282829")
current_frame.place(x=35,y=25)

today = Label(current_frame,font=("arial 20",16),bg="#282829",fg="#fff")
today.place(x=110,y=5)

#Weather icons
today_image = Label(current_frame,bg="#282829")
today_image.place(x=7,y=20)

today_Bottom= Label(current_frame,font=("arial 20",12),bg="#282829",fg="#fff",anchor="center")
today_Bottom.place(x=110,y=90)

today_bottom= Label(current_frame,font=("arial 20",12),bg="#282829",fg="#fff",anchor="center")
today_bottom.place(x=110,y=45)
#cell no 1


Label(frame,image=second_box,bg="#212120").place(x=300,y=30)
first_frame = Frame(frame,width=70,height=115,bg="#282829")
first_frame.place(x=305,y=35)

first = Label(first_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
first.place(x=7,y=5)

first_image = Label(first_frame,bg="#282829")
first_image.place(x=7,y=20)
#bottom Label
first_bottom= Label(first_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
first_bottom.place(x=10,y=90)
#cell no 2


Label(frame,image=second_box,bg="#212120").place(x=400,y=30)
second_frame = Frame(frame,width=70,height=115,bg="#282829")
second_frame.place(x=405,y=35)

second = Label(second_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
second.place(x=7,y=5)

second_image = Label(second_frame,bg="#282829")
second_image.place(x=7,y=20)
#bottom Label
second_bottom= Label(second_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
second_bottom.place(x=10,y=90)
#cell no 3


Label(frame,image=second_box,bg="#212120").place(x=500,y=30)
third_frame = Frame(frame,width=70,height=115,bg="#282829")
third_frame.place(x=505,y=35)

third = Label(third_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
third.place(x=7,y=5)

third_image = Label(third_frame,bg="#282829")
third_image.place(x=7,y=20)
#bottom Label
third_bottom= Label(third_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
third_bottom.place(x=10,y=90)
#cell no 4


Label(frame,image=second_box,bg="#212120").place(x=600,y=30)
fourth_frame = Frame(frame,width=70,height=115,bg="#282829")
fourth_frame.place(x=605,y=35)

fourth = Label(fourth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
fourth.place(x=7,y=5)

fourth_image = Label(fourth_frame,bg="#282829")
fourth_image.place(x=7,y=20)
#bottom Label
fourth_bottom= Label(fourth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
fourth_bottom.place(x=10,y=90)
#cell no 5


Label(frame,image=second_box,bg="#212120").place(x=700,y=30)
fifth_frame = Frame(frame,width=70,height=115,bg="#282829")
fifth_frame.place(x=705,y=35)

fifth = Label(fifth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
fifth.place(x=7,y=5)

fifth_image = Label(fifth_frame,bg="#282829")
fifth_image.place(x=7,y=20)
#bottom Label
fifth_bottom= Label(fifth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
fifth_bottom.place(x=10,y=90)
#cell no 6


Label(frame,image=second_box,bg="#212120").place(x=800,y=30)
sixth_frame = Frame(frame,width=70,height=115,bg="#282829")
sixth_frame.place(x=805,y=35)

sixth = Label(sixth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
sixth.place(x=7,y=5)

sixth_image = Label(sixth_frame,bg="#282829")
sixth_image.place(x=7,y=20)
#bottom Label
sixth_bottom= Label(sixth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
sixth_bottom.place(x=10,y=90)
#cell no 7


Label(frame,image=second_box,bg="#212120").place(x=900,y=30)
seventh_frame = Frame(frame,width=70,height=115,bg="#282829")
seventh_frame.place(x=905,y=35)

seventh = Label(seventh_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
seventh.place(x=7,y=5)

seventh_image = Label(seventh_frame,bg="#282829")
seventh_image.place(x=7,y=20)
#bottom Label
seventh_bottom= Label(seventh_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
seventh_bottom.place(x=10,y=90)
#cell no 8


Label(frame,image=second_box,bg="#212120").place(x=1000,y=30)
eightth_frame = Frame(frame,width=70,height=115,bg="#282829")
eightth_frame.place(x=1005,y=35)

eightth = Label(eightth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
eightth.place(x=7,y=5)

eightth_image = Label(eightth_frame,bg="#282829")
eightth_image.place(x=7,y=20)
#bottom Label
eightth_bottom= Label(eightth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
eightth_bottom.place(x=10,y=90)
#cell no 9


Label(frame,image=second_box,bg="#212120").place(x=1100,y=30)
nineth_frame = Frame(frame,width=70,height=115,bg="#282829")
nineth_frame.place(x=1105,y=35)

nineth = Label(nineth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
nineth.place(x=7,y=5)

nineth_image = Label(nineth_frame,bg="#282829")
nineth_image.place(x=7,y=20)
#bottom Label
nineth_bottom= Label(nineth_frame,font=("arial 20",10),bg="#282829",fg="#fff",anchor="center")
nineth_bottom.place(x=10,y=90)
#cell no 10




#matplotlib graph 
mat_frame = Frame(my_canvas,bg="#282829",height=300,width=1280)
mat_frame.place(x=0,y=720)
# mat_canvas = Canvas(mat_frame,bg="#282829").place(x=5,y=725)

# with open("hourly.json","r") as file:
#         data = json.load(file)
#     # the figure that will contain the plot
# fig = Figure(figsize = (15, 3),dpi = 100)
# x = []
# y = []
# x_names = []
# for i in data:
#     x_names.append(str(datetime.fromtimestamp(i["dt"]).time().isoformat("minutes")))
#     x.append(i["dt"])
#     y.append(i["temp"])
# # list of squares
# # y = [i**2 for i in range(101)]
# # adding the subplot
# plot1 = fig.add_subplot(111)

# # plotting the graph
# plot1.plot(x[::3],y[::3])
# plot1.set_title("Weekly forcast")
# plot1.set_xlabel("Time")
# plot1.set_ylabel("Temperature")
# plot1.set_xticks(x[::4],labels=x_names[::4])
# # creating the Tkinter canvas
# # containing the Matplotlib figure
# canvas = FigureCanvasTkAgg(fig,
#                            master = mat_frame)  
# canvas.draw()

# # placing the canvas on the Tkinter window
# canvas.get_tk_widget().pack(side=BOTTOM)

# # configure the canvas
# main_frame.configure(yscrollcommand=my_scrollbar.set(first=0,last=1))
# main_frame.bind(
#     '<Configure>', lambda e: my_canvas.configure(scrollregion=main_frame.bbox("all"))
# )
my_scrollbar.config(command =my_canvas.yview)

#clock 
clock = Label(my_canvas,text=f"{time_12_format}",font=("Helvetica",40,"bold"),fg="white",bg="#57adff")
clock.place(x=100,y=80)


root.mainloop()
