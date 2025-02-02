from tkinter import* 
from tkinter import ttk

import requests

city_name ="Dhaka"

data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=20a01944eda34a13f4a4dcecfff77197")






win = Tk()

win.title("Tanzirs Code")
win.config(bg= "Teal")
win.geometry("550x550")

name_label = Label(win,text="Tanzirs Weather App",
                    font=("Times New Roman", 35, "bold"))

name_label.place(x=50, y=50, height=60,width=450)

list_name =[
    "Dhaka", "Chittagong", "Khulna", "Rajshahi", "Barisal", "Sylhet", "Rangpur", "Mymensingh",
    "New York", "Los Angeles", "Chicago", "Houston", "Miami", "San Francisco", "Boston", "Seattle",
    "London", "Manchester", "Birmingham", "Glasgow", "Edinburgh", "Liverpool",
    "Berlin", "Munich", "Frankfurt", "Hamburg", "Cologne", "Stuttgart",
    "Paris", "Marseille", "Lyon", "Toulouse", "Nice",
    "Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya",
    "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu",
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide",
    "Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"
]

com = ttk.Combobox( win,text="Tanzirs Weather App", values=list_name,
                    font=("Times New Roman", 25, "bold"))

com.place(x=75, y=120, height=50,width=400)

done_button =Button(win,text="Done",
                    font=("Times New Roman", 15, "bold"))

done_button.place(y=195, height=50, width=100, x=225)



WA_label = Label(win,text="Climatic",
                    font=("Times New Roman", 15, "bold"))

WA_label.place(x=50, y=260, height=50,width=200)
WA_label1 = Label(win,text="",
                    font=("Times New Roman", 15, "bold"))

WA_label1.place(x=255, y=260, height=50,width=200)



WB_label = Label(win,text="Description",
                    font=("Times New Roman", 15, "bold"))

WB_label.place(x=50, y=320, height=50,width=200)
WB_label1 = Label(win,text="",
                    font=("Times New Roman", 15, "bold"))

WB_label1.place(x=255, y=320, height=50,width=200)



WC_label = Label(win,text="Warmth",
                    font=("Times New Roman", 15, "bold"))

WC_label.place(x=50, y=380, height=50,width=200)
WC_label1 = Label(win,text="",
                    font=("Times New Roman", 15, "bold"))

WC_label1.place(x=255, y=380, height=50,width=200)



WD_label = Label(win,text="Pressure",
                    font=("Times New Roman", 15, "bold"))

WD_label.place(x=50, y=440, height=50,width=200)
WD_label = Label(win,text="",
                    font=("Times New Roman", 15, "bold"))

WD_label.place(x=255, y=440, height=50,width=200)



win.mainloop()