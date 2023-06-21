from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import ImageTk, Image

weather = Tk()
weather.title("Weather App")
weather.geometry("900x500")
weather.configure(bg="#0071c5")
weather.resizable(False, False)

def getweather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="weatherAPI")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)

# search field
oval_icon = PhotoImage(file="images/11.png")
myimage = Label(image=oval_icon,  bg="blue")
myimage.place(x=200, y=50)

textfield = tk.Entry(weather, justify="center", width=10, border=0, font=("poppins", 25, "bold"), fg="white", bg="#404040")
textfield.place(x=215, y=70)
textfield.focus()

Search_icon = PhotoImage(file="images/search.png", height=40)
image_icon = Button(image=Search_icon, border=0, borderwidth=0, cursor="hand2", bg="#404040", command=getweather )
image_icon.place(x=450, y=70)

image_icon = ImageTk.PhotoImage(Image.open("images/img-1.jpg"), width=500)
myimg = Label(weather, image=image_icon, border=2, bg="#0071c5")
myimg.place(x=350, y=200)

box_icon = PhotoImage(file="images/img-12.png")
myimage = Label(weather, image=box_icon, bg="#0071c5" )
myimage.place(x=50, y=180)


# Label1
Label1 = Label(weather, text="Wind speed", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label1.place(x=60, y=200)
Label2 = Label(weather, text="Temperature", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label2.place(x=60, y=220)
Label3 = Label(weather, text="Humidity", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label3.place(x=60, y=240)
Label4 = Label(weather, text="Pressure", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label4.place(x=60, y=260)
Label4 = Label(weather, text="Description", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label4.place(x=60, y=280)


# bottom box
frame = Frame(weather, width=1000, height=180, bg="#000001")
frame.pack(side=BOTTOM)

# bottom boxes
firstbox = PhotoImage(file="images/img-12.png")
secondbox = PhotoImage(file="images/img-14.png")

Label(frame, image=firstbox, bg="#212120",border=2, background="white" ).place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120", border=2, background="white" ).place(x=270, y=20)
Label(frame, image=secondbox, bg="#212120", border=2, background="white" ).place(x=400, y=20)
Label(frame, image=secondbox, bg="#212120" , border=2, background="white" ).place(x=530, y=20)
Label(frame, image=secondbox, bg="#212120" , border=2, background="white" ).place(x=660, y=20)
Label(frame, image=secondbox, bg="#212120" , border=2, background="white" ).place(x=790, y=20)
Label(frame, image=secondbox, bg="#212120", border=2, background="white" ).place(x=920, y=20)

#clock
clock = Label(weather,text="17:01 pm", font=("Helvetica",30,'bold'), fg="white", bg= "#0071c5")
clock.place(x=25,y=20)

#timezone
timezone = Label(weather, font=("Helvetica",20), fg="white", bg= "#0071c5")
timezone.place(x=500,y=20)

long_lat = Label(weather, font=("Helvetica",10), fg="white", bg= "#0071c5")
long_lat.place(x=500,y=40)
weather.mainloop()
