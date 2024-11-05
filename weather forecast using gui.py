import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk 
import ttkbootstrap as ttk

def get_weather(city):
    api_key='0a205f67f1c1c9467d7ebc3b61c0ece3'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    res=requests.get(url)

    if res.status_code==404:
        messagebox.showerror("Error","City not found")
        return None
    
    weather=res.json()
    icon_id=weather['weather'][0]['icon']
    temperature=weather['main']['temp'] - 273.15
    description=weather['weather'][0]['description']
    city=weather['name']
    country=weather['sys']['country']


    icon_url=f'https://openweathermap.org/img/wn/{icon_id}@2x.png'
    return(icon_url,temperature,description,city,country)

def search():
    city=city_entry.get()
    result=get_weather(city)
    if result is None:
        return 
    
    icon_url,temperature,description, city,country = result

    location_label.configure(text=f"{city},{country}")
    image=Image.open(requests.get(icon_url,stream=True).raw)
    icon=ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image=icon

    temp_label.configure(text=f'Temperature: {temperature:.2f}C')
    description_label.configure(text=f'Description: {description}')




root = ttk.Window(themename='morph')
root.title('WEATHER APP')
root.geometry('500x500')

city_entry=ttk.Entry(root,font="Helvetica, 18")
city_entry.pack(pady=10)

search=ttk.Button(root, text="Search", command=search,bootstyle='warning')
search.pack(pady=10)

location_label=tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

icon_label=tk.Label(root)
icon_label.pack()

temp_label=tk.Label(root,font="Helvetica, 20")
temp_label.pack()

description_label=tk.Label(root,font="Helvetica, 20")
description_label.pack()

root.mainloop()