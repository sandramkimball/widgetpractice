import tkinter as tk
from tkinter import font
import requests #api reqs

HEIGHT = 700
WIDTH = 800
KEY = '29a969b2a16a32f479de15ffa59a5bd1'
URL_FORE = 'api.openweathermap.org/data/2.5/forecast'
URL_CURR = 'api.openweathermap.org/data/2.5/weather'

# functions
def formatResponse(weather):
    try: 
        city = weather['name']
        desc = ['weather'][0]['description']
        temp = weather['main']['temp']

        formatted_data = 'City: %s \nConditions: %s \nTemperature: %s F' % (city, desc, temp)

    except:
        formatted_data = 'There was a problem retrieving the data.'

def getWeather(city):
    params = {'APPID': KEY, 'q': city, 'units': 'imperial'}
    res = requests.get(URL_FORE, params=params)
    data = res.json() #json converts to python dict
    
    label[text] = formatResponse(data)

# set background image
bk_img = tk.PhotoImage(file='island.jpg')
bk_label = tk.Label(root, image=bk_img)
bk_label.place(relwidth=1, relheight=1)

#every app built with tk needs a root to attach to
root = tk.TK()

#create container with defined size for button
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#efefef', bd=3)
frame.place(anchor="n", relwidth=.75, relheight=0.1, relx=0.5, rely=0.5) 

entry = tk.Entry(frame, bg='yellow', font=('Modern', 12))
entry.pack(relwidth=0.65, relheight=0.75)

button = tk.Button(root, text="Weather", bg='#cce6ff', font=('Modern', 12), command=Lambda:getWeather(entry.get()) )
#Lambda = reruns it each time the button is hit. Async function
button.pack(relx=0.7, relwidth=0.3, relheight=0.75) 

lower_frame = tk.Frame(root, bg='#efefef' bd=3)
lower_frame.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6)

label = tk.Label(lower_frame, font=('Modern', 30), )
label.pack(relwidth=1, relheight=1)

#always last line
root.mainloop()