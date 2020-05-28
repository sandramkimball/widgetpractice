import tkinter as tk
from tkinter import font
import os
# in BASH - 'py -m pip install requests --user' - api fetch service
import requests 


# functions
def formatResponse(weather):
    try: 
        city = weather['name']
        desc = ['weather'][0]['description']
        temp = weather['main']['temp']
        print(city, weather['name'])
        formatted_data = city

    except:
        formatted_data = 'There was a problem retrieving the data.'

    print(formatted_data)
    return formatted_data

def getWeather(city):
    KEY = '29a969b2a16a32f479de15ffa59a5bd1'
    URL_FORE = 'https://api.openweathermap.org/data/2.5/forecast'
    URL_CURR = 'https://api.openweathermap.org/data/2.5/weather'

    params = {'APPID': KEY, 'q': city, 'units': 'imperial'}
    res = requests.get(URL_CURR, params=params)
    data = res.json() #json converts to python dict
    
    label['text'] = formatResponse(data)




root = tk.Tk()

#create container with defined size for input and button 
canvas = tk.Canvas(root, height=500, width=600, bg='pink')
canvas.pack()

# set background image
# background_image = tk.PhotoImage(file='island.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root)
frame.place(anchor="n", relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1) 

entry = tk.Entry(frame, bg='white', font=('Modern', 12))
entry.place(relwidth=0.75, relheight=1, )

button = tk.Button(frame, text="Get Weather", bg='white', font=('Modern', 12), command=lambda:getWeather(entry.get()) )
button.place(relx=0.75, relheight=1, relwidth=0.25) 

lower_frame = tk.Frame(root, bg='white', bd=3)
lower_frame.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6)

label = tk.Label(lower_frame, font=('Modern', 25) )
label.place(relwidth=1, relheight=1)

#always last line
root.mainloop()