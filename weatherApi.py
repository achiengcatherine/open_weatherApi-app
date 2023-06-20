from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

weather = Tk()
weather.title("Weather App")
weather.geometry("900x500")
weather.resizable(False, False)

def getweather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="weatherAPI")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    print(result)

# search field
textfield = tk.Entry(weather, justify="center", width=15, border=0, font=("poppins", 25, "bold"), fg="white", bg="#404040")
textfield.place(x=60, y=50)
textfield.focus()

Search_icon = PhotoImage(file="search.png", width=55, height=40)
image_icon = Button(image=Search_icon, border=0, borderwidth=0, cursor="hand2", bg="#404040")
image_icon.place(x=350, y=50)

# Label1
Label1 = Label(weather, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="red")
Label1.place(x=120, y=500)
Label1 = Label(weather, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="red")
Label1.place(x=120, y=500)
Label1 = Label(weather, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="red")
Label1.place(x=120, y=500)
Label1 = Label(weather, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="red")
Label1.place(x=120, y=500)
weather.mainloop()
