from tkinter import *
from tkinter import ttk,messagebox
import pytz
from PIL import Image,ImageTk
import json
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# import main

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
        y.append(i["temp"])
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


    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = win)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,win)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
# def on_click(city):
#     main.get_weather(city)
#     plot()
win = Tk()
win.geometry("1280x720")
win.title("Weather App")
win.resizable(False,False)

entry= Entry(win, width= 40)
entry.pack()

plot_button = Button(master = win, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Plot")
  
# place the button 
# in main window
plot_button.pack()

win.mainloop()
