from tkinter import *
import tkinter as tk

from future.backports.datetime import timedelta
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import ImageTk, Image

weather = Tk()
weather.title("Weather App")

bg = ImageTk.PhotoImage(Image.open("images/bg.jpg"),)
label = Label(weather, image=bg)
label.pack()

weather.geometry("1000x600")
#weather.configure(bg="#0071c5")
weather.resizable(False, False)

def getweather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="weatherAPI")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text = f"{round(location.latitude,10)}°N, {round(location.longitude),8}°E")


    time=pytz.timezone(result)
    current_time = datetime.now(time).strftime('%a %b %d, %Y %I:%M:%S %p')
    clock.config(text=current_time)

    #weather
    #url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=a249f3b30a2bdb61fe5ac47c6e8ce7c1"
    url = "https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=a249f3b30a2bdb61fe5ac47c6e8ce7c1"
    json_data =requests.get(url).json()
    print(json_data)

    #current
    wind = json_data['wind']['speed']
    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    desc = json_data['weather'][0]['description']

    w.config(text=(wind, "m/s"))
    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hpa"))
    d.config(text=desc)

    #first cell
    #firstdayimage = json_data['daily'][0]['weather'][0]['icon']

    #second cell
    #seconddayimage = json_data['daily'][1]['weather'][0]['icon']

    #third cell
    #thirddayimage = json_data['daily'][2]['weather'][0]['icon']

    #fourth   cell
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']

    #fifth cell
    #fifthdayimage = json_data['daily'][4]['weather'][0]['icon']

    #sixth cell
    #sixthdayimage = json_data['daily'][5]['weather'][0]['icon']

    #seventh cell
   # seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    #days
    first = datetime.now()
    day1.config(text=day1.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=1)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=1)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=1)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=1)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=1)
    day7.config(text=seventh.strftime("%A"))



# search field
#oval_icon = ImageTk.PhotoImage(Image.open("images/11.jpeg"))
#myimage = Label(image=oval_icon,  bg="blue", width=320, height=60 , border=6, background="#0071c5")
#myimage.place(x=100, y=50)

textfield = tk.Entry(weather, justify="center", width=11, border=0, font=("poppins", 25), fg="white", bg="#72A0C1")
textfield.place(x=115, y=70)
textfield.focus()

Search_icon = ImageTk.PhotoImage(Image.open("images/search.png"))
image_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#72A0C1", command=getweather)
image_icon.place(x=350, y=70)


box = Frame(width=280, height=150, bg="#72A0C1")
box.place(x=30, y=210)

# Label1
Label1 = Label(weather, text="Wind speed", font=("Helvetica", 15, 'bold'), fg="white", bg="#72A0C1")
Label1.place(x=60, y=230)
Label2 = Label(weather, text="Temperature", font=("Helvetica", 15, 'bold'), fg="white", bg="#72A0C1")
Label2.place(x=60, y=250)
Label3 = Label(weather, text="Humidity", font=("Helvetica", 15, 'bold'), fg="white", bg="#72A0C1")
Label3.place(x=60, y=270)
Label4 = Label(weather, text="Pressure", font=("Helvetica", 15, 'bold'), fg="white", bg="#72A0C1")
Label4.place(x=60, y=290)
Label4 = Label(weather, text="Description", font=("Helvetica", 15, 'bold'), fg="white", bg="#72A0C1")
Label4.place(x=60, y=310)

#timezone
timezone = Label(weather, font=("Helvetica", 20), fg="white", bg="#142b44")
timezone.place(x=600, y=50)

long_lat = Label(weather, font=("Helvetica", 10), fg="white", bg="#142b44")
long_lat.place(x=600, y=90)

#clock
clock = Label(weather, font=("Helvetica", 17, 'bold'), fg="white", bg="#142b44")
clock.place(x=600, y=130)

#wthpd
w = Label(weather, font=("Helvetica", 11), fg="white", bg="#72A0C1")
w.place(x=200, y=230)
t = Label(weather, font=("Helvetica", 11), fg="white", bg="#72A0C1")
t.place(x=200, y=250)
h = Label(weather, font=("Helvetica", 11), fg="white", bg="#72A0C1")
h.place(x=200, y=270)
p = Label(weather, font=("Helvetica", 11), fg="white", bg="#72A0C1")
p.place(x=200, y=290)
d = Label(weather, font=("Helvetica", 11), fg="white", bg="#72A0C1")
d.place(x=200, y=310)

#first cell
firstbox = Frame(weather, width=180, height=130, highlightthickness=1, bg="#72a0c1")
firstbox.place(x=20, y=450)

day1 = Label(firstbox,text="day1", font=("arial", 20), bg="#72A0C1", fg="white")
day1.place(x=10, y=15)

firstImage = Label(firstbox, bg="#72A0C1")
firstImage.place(x=4, y=15)

#second cell
secondbox = Frame(weather, width=110, height=130, highlightthickness=1,  bg="#72A0C1")
secondbox.place(x=220, y=450)

day2 = Label(secondbox, font=("arial", 20), bg="#72A0C1", fg="white")
day2.place(x=10, y=15)

secondImage = Label(secondbox, bg="#72A0C1")
secondImage.place(x=4, y=15)

#third cell
thirdbox = Frame(weather, width=120, height=130, highlightthickness=1, bg="#72A0C1")
thirdbox.place(x=350, y=450)

thirdImage = Label(thirdbox, bg="#72A0C1")
thirdImage.place(x=4, y=15)

day3 = Label(thirdbox, font=("arial", 20), bg="#72A0C1", fg="white")
day3.place(x=10, y=15)


#fourth cell
fourthbox = Frame(weather, width=110, height=130, highlightthickness=1, bg="#72A0C1")
fourthbox.place(x=490, y=450)

day4 = Label(fourthbox, font=("arial", 20), bg="#72A0C1", fg="white")
day4.place(x=10, y=15)

fourthImage = Label(fourthbox, bg="#72A0C1")
fourthImage.place(x=4, y=15)

#fifth cell
fifthbox = Frame(weather, width=110, height=130, highlightthickness=1, bg="#72A0C1")
fifthbox.place(x=620, y=450)

day5 = Label(fifthbox, font=("arial", 20), bg="#72A0C1", fg="white")
day5.place(x=10, y=15)

fifthImage = Label(fifthbox, bg="#72A0C1")
fifthImage.place(x=4, y=15)

#sixth cell
sixthbox = Frame(weather, width=110, height=130, highlightthickness=1, bg="#72A0C1")
sixthbox.place(x=750, y=450)

day6 = Label(sixthbox, font=("arial", 20), bg="#72A0C1", fg="white")
day6.place(x=10, y=15)

sixthImage = Label(sixthbox, bg="#72A0C1")
sixthImage.place(x=4, y=15)

#seventh cell
seventhbox = Frame(weather, width=110, height=130, highlightthickness=1, highlightcolor="red", background="#0093AF", bg="#72A0C1")
seventhbox.place(x=880, y=450)

day7 = Label(seventhbox, font=("arial", 20), bg="#72A0C1", fg="white")
day7.place(x=10, y=15)

seventhImage = Label(seventhbox, bg="#72A0C1")
seventhImage.place(x=4, y=15)

weather.mainloop()
