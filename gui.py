from tkinter import *

root = Tk()
root.title("Weather App")
root.geometry("500x400") 
root.resizable(0, 0)
root.iconbitmap(r"C:\vscode dir\python\my projects\weather fetcher\my.ico")
root.configure(background='#ffffff')

# functions -----------------------------

import requests as rq

API_KEY = 'b0fd9db11bcead7a19c763ec32b1be95'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
def get_name():
    global City
    City = cityname.get()

    req_url = f"{BASE_URL}?appid={API_KEY}&q={City}"
    response = rq.get(req_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]['description']
        textbox.insert(END,f"Weather : {weather} \n")
        temperature = round(data['main']['temp'] - 273.15, 2)
        textbox.insert(END,f"temperature : {temperature} \n ")
    
    else:
        textbox.insert(0,"an error occurred")


def clear_name():
    textbox.delete(0, END)
    cityname.delete(0, END)

# main code------------------------------

Label(root, text="Weather App",font='roboto 14',fg="orange",bg='white').place(x=30,y=20)

Cityname = Label(root, text="Enter a city name",font='roboto 12',bg='white')
Cityname.place(x=30,y=80)

city = StringVar()
cityname = Entry(root,textvariable=city,font='roboto 13',bg='#f9f9f9')
cityname.place(x=180,y=80)

submitbtn = Button(root, command=get_name , text="Show me",font='roboto 13',fg='#0a0a0a',bg='orange')
submitbtn.place(x=390,y=74)

clearbtn = Button(root, command=clear_name , text=" Clear ",font='roboto 13',fg='#0a0a0a',bg='orange')
clearbtn.place(x=400,y=330)

textbox = Entry(root,width=48,font='roboto 13',bg='#fafafa' )
textbox.place(x=30,y=140,height=160)


root.mainloop()