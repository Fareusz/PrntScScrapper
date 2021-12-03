import random
import string
import webbrowser
from bs4 import BeautifulSoup
import cloudscraper
from tkinter import *
from tkinter import messagebox
import requests
import urllib.request
import os
from datetime import datetime


# The creator is not responsible for the screenshots found by this script!!!

new = 1

root = Tk()
root.title("PrntScScapper by Fareusz")
root.geometry("500x250")

def openweb(link):
    webbrowser.open(link, new=new)


def rename():
    now = str(datetime.now())
    now = now.replace(":", "-")
    os.rename('image.jpg', f"{now}.jpg")

scraper = cloudscraper.create_scraper()
resultList = list()

def FindLinkPrnt():
    print(brwser)
    found = 0
    while found == 0:
        id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        URL = "https://prnt.sc/" + str(id)
        page = scraper.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        results = soup.find(class_="no-click screenshot-image")
        try:
            source = results['src']
        except:
            print('Unknown link... Skipping... ' + str(id))
            continue
        if '//st.prntscr.com/2021/10/22/2139/img/0_173a7b_211be8ff.png' in source:
            print('Unknown link.. skipping...' + str(id))
            continue
        if 'https://i.imgur.com/N2t4s73.png' in source:
            print('Unknown link.. skipping...' + str(id))
            continue
        if 'https://i.imgur.com/removed.png' in source:
            print('Unknown link.. skipping...' + str(id))
            continue
        res = requests.get(results['src'])
        response = res.status_code
        if response == 200:
            response = '✓  Success!'
            found =+ 1
        if response == 520:
            response = '✓  Success!'
            found =+ 1
        if response == 404:
            response = 'X  Not Found'
            continue
        if response == 403:
            response = 'X Forbidden'
            continue
        b = brwser.get()
        if b == 1:
            openweb(source)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        filename = 'image.jpg'
        image_url = source
        urllib.request.urlretrieve(image_url, filename)
        root2 = Tk()
        def next():
            root2.destroy()
            FindLinkPrnt()
        img = PhotoImage(master=root2, file="image.jpg")
        button3 = Button(root2, width=2, height=2, text = 'Next!', font = 'ComicSans', bg='black', fg='green', padx = 10, command = next)
        button2 = Button(root2, width=2, height=2, text = 'Save!', font = 'ComicSans', bg='black', fg='green', padx = 10, command = rename)
        button2.pack()
        button3.pack()
        label = Label(root2, image=img)
        label.pack()
        root2.mainloop()



Button(root, width=50, height=10, text = 'Get Link', font = 'ComicSans', bg='black', fg='green', padx = 10, command = FindLinkPrnt).place(x=10,y=10)

brwser = IntVar()
c = Checkbutton(root, text="Open in Browser at hit", variable=brwser, onvalue=1, offvalue=0)
c.pack()
c.place(x=200,y=205)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        try:
            os.remove("image.jpg")
            root.destroy()
        except:
            root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()
