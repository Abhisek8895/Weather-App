from tkinter import *
import requests
from timezonefinder import TimezoneFinder
import pytz
import datetime
import os
from dotenv import load_dotenv

# Converting the data to celcius
def get_temp_cel():
    try:
        load_dotenv()
        url = os.getenv("URL")
        api = os.getenv("API_KEY")
        city = city_name.get()
        data = requests.get(url+city+api).json()
        temp_cel = str(int(data["main"]["temp"] - 273.15))
        temp_c_lab.config(text=(temp_cel, "°"))
        temp_c_lab.place(x=300, y=150)
        temp_f_lab.place_forget()
    except:
        pass

# Converting the data to fahrenheit
def get_temp_frn():
    try:
        load_dotenv()
        url = os.getenv("URL")
        api = os.getenv("API_KEY")
        city = city_name.get()
        data = requests.get(url+city+api).json()
        temp_f_lab.config(text=(data["main"]["temp"], "°"))
        temp_f_lab.place(x=200, y=150)
        temp_c_lab.place_forget()
    except:
        pass

# Getting the data
def get_data():
    try:
        load_dotenv()
        url = os.getenv("URL")
        api = os.getenv("API_KEY")
        city = city_name.get()
        data = requests.get(url+city+api).json()

        weather_lab.config(text=data["weather"][0]["main"])

        humidity_lab.config(text=(data["main"]["humidity"], "%"))

        wind_lab.config(text=(data["wind"]["speed"], "km/h"))

        temp_cel = str(int(data["main"]["temp"]-273.15))
        temp_c_lab.config(text=(temp_cel, "°"))

        pressure_lab.config(text=data["main"]["pressure"])

        feel_temp_cel = str(int(data["main"]["feels_like"]-273.15))
        feels_like.config(text=(feel_temp_cel, "°C"))

        max_temp_cel = str(int(data["main"]["temp_max"]-273.15))
        max_temp.config(text=(max_temp_cel, "°C"))
        min_temp_cel = str(int(data["main"]["temp_min"]-273.15))
        min_temp.config(text=(min_temp_cel, "°C"))

        city_lab.config(text=data["name"])


        # get time
        lon = data["coord"]["lon"]
        lat = data["coord"]["lat"]

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=lon, lat=lat)
        home = pytz.timezone(result)
        local_time= datetime.datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        time_lab.config(text=current_time)
    except:
        pass


def geometry():
    w = 900  # width for the Tk root
    h = 500  # height for the Tk root
    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def cel_colour_fade():
    frn_lab.config(fg="black")
    cel_lab.config(fg="gray")

def frn_colour_fade():
    frn_lab.config(fg="gray")
    cel_lab.config(fg="black")


root = Tk()
geometry()
root.title("Weather Report")
root.resizable(False, False)
root.configure(bg="cornflower blue")

# icon
icon = PhotoImage(file="images/weather-app.png")
root.iconphoto(False, icon)
# Labels

logo_img = PhotoImage(file="images/weather-app.png")
Label(root, image=logo_img, bg="cornflower blue").place(x=20, y=20)

Label(root, text="Enter City Name", font=("helvetica", 20, "italic"), bg="cornflower blue").place(x=250, y=20)

searchbar_img = PhotoImage(file="images/Copy of search 1.png")
Label(root, image=searchbar_img, bg="cornflower blue").place(x=175, y=55)

city_name = Entry(root, width=14, justify="center", font=("helvetica", 25, "italic"), border=0)
city_name.place(x=235, y=70)

search_img = PhotoImage(file="images/search.png")
Button(root, image=search_img, bd=0, cursor="hand2", command=get_data).place(x=488, y=70)

city_lab = Label(root, text="", font=("helvetica", 20, "italic"), bg="cornflower blue")
city_lab.place(x=650, y=30)

time_lab = Label(root, text="", font=("helvetica", 20, "italic"), bg="cornflower blue")
time_lab.place(x=650, y=70)

# Temperature

temp_c_lab = Label(root, text="", font=("helvetica", 43), bg="cornflower blue")
temp_c_lab.place(x=300, y=150)

temp_f_lab = Label(root, text="", font=("helvetica", 43), bg="cornflower blue")
temp_f_lab.place(x=200, y=150)

cel_lab = Button(root, text="C", font=("helvetica", 20, "italic"), bg="cornflower blue", bd=0, command=lambda: [frn_colour_fade(), get_temp_cel()])
cel_lab.place(x=420, y=150)

or_lab = Label(root, text="/", font=("helvetica", 30, "italic"), bg="cornflower blue")
or_lab.place(x=460, y=150)

frn_lab = Button(root, text="F", font=("helvetica", 20, "italic"), bg="cornflower blue", bd=0, fg="gray", command=lambda: [cel_colour_fade(), get_temp_frn()])
frn_lab.place(x=480, y=150)

Label(root, text="Feels Like: ", font=("helvetica", 15, "italic"), bg="cornflower blue").place(x=215, y=230)
feels_like = Label(root, text="", font=("helvetica", 15, "italic"), bg="cornflower blue")
feels_like.place(x=410, y=230)

Label(root, text="Max Temperature: ", font=("helvetica", 15, "italic"), bg="cornflower blue").place(x=215, y=270)
max_temp = Label(root, text="", font=("helvetica", 15, "italic"), bg="cornflower blue")
max_temp.place(x=410, y=270)

Label(root, text="Min Temperature: ", font=("helvetica", 15, "italic"), bg="cornflower blue").place(x=215, y=310)
min_temp = Label(root, text="", font=("helvetica", 15, "italic"), bg="cornflower blue")
min_temp.place(x=410, y=310)


# Other details

weather = Label(root, text="Weather", font=("helvetica", 20, "italic"), bg="cornflower blue")
weather.place(x=25, y=370)

weather_lab = Label(root, text="", font=("helvetica", 15, "italic"), bg="cornflower blue")
weather_lab.place(x=45, y=410)

humidity = Label(root, text="Humidity", font=("helvetica", 20, "italic"), bg="cornflower blue")
humidity.place(x=220, y=370)

humidity_lab = Label(root, text="", font=("helvetica", 15, "italic"), bg="cornflower blue")
humidity_lab.place(x=240, y=410)

wind = Label(root, text="Wind Speed", font=("helvetica", 20, "italic"), bg="cornflower blue")
wind.place(x=430, y=370)

wind_lab = Label(root, text="", font=("helvetica", 15, "italic"), bg="cornflower blue")
wind_lab.place(x=450, y=410)

pressure = Label(root, text="Pressure", font=("helvetica", 20, "italic"), bg="cornflower blue")
pressure.place(x=700, y=370)

pressure_lab = Label(root, text="", font=("helvetica", 15, "italic"), bg="cornflower blue")
pressure_lab.place(x=720, y=410)

root.mainloop()