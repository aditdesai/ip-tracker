import requests
from tkinter import *

root = Tk()
root.title("IP Tracker")
root.geometry("300x250")

def search(ip_address):
    url = 'http://ip-api.com/json/'
    url = url + ip_address.strip()

    response = requests.get(url)
    x = response.json()
    
    if response.status_code == 200 and x["status"] == "success":
        country.set('Country: ' + x["country"])
        region.set('Region: ' + x["region"])
        city.set('City: ' + x["city"])
        isp.set('ISP: ' + x["isp"])
    else:
        country.set('')
        region.set('Error')
        city.set('')
        isp.set('')
        

def enter(event):
    text = entry.get('1.0', END)
    search(text)
    entry.delete('1.0', END)
    entry.insert(INSERT, text)

label = Label(root, text = 'IP Address:')
label.place(x = 25, y = 30)

entry = Text(root, height = 1, width = 20, borderwidth = 3)
entry.place(x = 100, y = 30)

button = Button(root, text = 'Search', bd = 3, command = lambda : search(entry.get('1.0', END)))
button.place(x = 120, y = 65)
root.bind('<Return>', enter)

country = StringVar()
region = StringVar()
city = StringVar()
isp = StringVar()

country_label = Label(root, textvariable = country)
country_label.place(x = 25, y = 100)

region_label = Label(root, textvariable = region)
region_label.place(x = 25, y = 120)

city_label = Label(root, textvariable = city)
city_label.place(x = 25, y = 140)

isp_label = Label(root, textvariable = isp)
isp_label.place(x = 25, y = 160)


root.mainloop()