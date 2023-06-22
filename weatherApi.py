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
    long_lat.config(text = f"{round(location.latitude,10)}°N, {round(location.longitude),8}°E")
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%1:%M %p")
    clock.config(text=current_time)

    #weather
    api="https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&exclude={part}&appid={API key}"
    json_data =requests.get(api).json()

    #current
    wind = json_data['current']['wind']
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    desc = json_data['current']['weather'][0]['desc']

    w.config(text=(wind, "m/s"))
    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hpa"))
    d.config(text=desc)

    #first cell
    #second cell
    #third cell
    #fourth   cell
    #fifth cell
    #sixth cell
    #seventh cell

    #days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))


# search field
oval_icon = PhotoImage(file="images/11.png")
myimage = Label(image=oval_icon,  bg="blue")
myimage.place(x=200, y=50)

textfield = tk.Entry(weather, justify="center", width=20, border=0, font=("poppins", 15), fg="white", bg="#404040")
textfield.place(x=215, y=70)
textfield.focus()

Search_icon = PhotoImage(file="images/search.png")
image_icon = Button(image=Search_icon, border=0, borderwidth=0, cursor="hand2", bg="#404040", command=getweather )
image_icon.place(x=450, y=70)

image_icon = ImageTk.PhotoImage(Image.open("images/img-1.jpg"), width=500)
myimg = Label(weather, image=image_icon, border=2, bg="#0071c5")
myimg.place(x=350, y=200)

box_icon = PhotoImage(file="images/img-12.png")
myimage = Label(weather, image=box_icon, bg="#0071c5" )
myimage.place(x=50, y=150)


# Label1
Label1 = Label(weather, text="Wind speed", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label1.place(x=60, y=170)
Label2 = Label(weather, text="Temperature", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label2.place(x=60, y=190)
Label3 = Label(weather, text="Humidity", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label3.place(x=60, y=210)
Label4 = Label(weather, text="Pressure", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label4.place(x=60, y=230)
Label4 = Label(weather, text="Description", font=("Helvetica", 15, 'bold'), fg="white", bg="black")
Label4.place(x=60, y=250)


# bottom box
frame = Frame(weather, width=1100, height=180, bg="#00538C")
frame.pack(side=BOTTOM)

# bottom boxes
#firstbox = PhotoImage(file="images/img-12.png")
#secondbox = PhotoImage(file="images/img-14.png")

#Label(frame, image=firstbox, bg="#212120",border=2, background="white" ).place(x=30, y=20)
#Label(frame, image=secondbox, bg="#212120", border=2, background="white" ).place(x=270, y=20)
#Label(frame, image=secondbox, bg="#212120", border=2, background="white" ).place(x=400, y=20)
#Label(frame, image=secondbox, bg="#212120" , border=2, background="white" ).place(x=530, y=20)
#Label(frame, image=secondbox, bg="#212120" , border=2, background="white" ).place(x=660, y=20)
#Label(frame, image=secondbox, bg="#212120" , border=2, background="white" ).place(x=790, y=20)
#Label(frame, image=secondbox, bg="#212120", border=2, background="white" ).place(x=920, y=20)

#clock
clock = Label(weather, text="11:30 pm", font=("Helvetica", 20, 'bold'), fg="white", bg= "#0071c5")
clock.place(x=700, y=80)

#timezone
timezone = Label(weather, font=("Helvetica", 20), fg="white", bg= "#0071c5")
timezone.place(x=700, y=20)

long_lat = Label(weather, font=("Helvetica", 10), fg="white", bg= "#0071c5")
long_lat.place(x=700, y=50)

#wthpd
w = Label(weather, text="wind", font=("Helvetica", 11), fg="white", bg="black")
w.place(x=200, y=170)
t = Label(weather, font=("Helvetica", 11), fg="white", bg="black")
t.place(x=200, y=190)
h = Label(weather, font=("Helvetica", 11), fg="white", bg="black")
h.place(x=200, y=210)
p = Label(weather, font=("Helvetica", 11), fg="white", bg="black")
p.place(x=200, y=230)
d = Label(weather, font=("Helvetica", 11), fg="white", bg="black")
d.place(x=200, y=250)

#first cell
firstbox = Frame(frame, width=180, height=130, highlightthickness=1, bg="#0071c5")
firstbox.place(x=20, y=20)

day1 = Label(firstbox,text="day", font=("arial",20), bg="#0071c5", fg="white")
day1.place(x=10, y=15)
#second cell
secondbox = Frame(frame, width=100, height=130,highlightthickness=1,  bg="#0071c5")
secondbox.place(x=220, y=20)

#third cell
thirdbox = Frame(frame, width=100, height=130,highlightthickness=1, bg="#0071c5")
thirdbox.place(x=330, y=20)

#fourth cell
fourthbox = Frame(frame, width=100, height=130,highlightthickness=1, bg="#0071c5")
fourthbox.place(x=440, y=20)

#fifth cell
fifthbox = Frame(frame, width=100, height=130,highlightthickness=1, bg="#0071c5")
fifthbox.place(x=550, y=20)

#sixth cell
sixthbox = Frame(frame, width=100, height=130, highlightthickness=1, bg="#0071c5")
sixthbox.place(x=660, y=20)

#seventh cell
seventhbox = Frame(frame, width=100, height=130, highlightthickness=1,highlightcolor="red", background="#0093AF", bg="#0071c5")
seventhbox.place(x=770, y=20)

weather.mainloop()
