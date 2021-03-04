import tkinter as tk
from tkinter import ttk
from tkinter.constants import HORIZONTAL, TRUE
import wikipedia
from wikipedia.wikipedia import random
import time

root = tk.Tk()
progress = ttk.Progressbar(root, orient = HORIZONTAL, 
              length = 100, mode = 'determinate') 
canvas1 = tk.Canvas(root, width=400, height=300,  relief='raised')
canvas1.pack()
canvas1.configure(bg='yellow')

label1 = tk.Label(root, text='WikiPages')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter the Topic Name:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)
url = " "


def fetchurl():
    global url

    x1 = entry1.get()
    topic = str(x1)
    print(topic)
    progress.pack(pady=10)
    progress['value']=20
    root.update_idletasks()

    time.sleep(1)
    progress.pack(pady=10)
    progress['value']=50
    root.update_idletasks()
    progress.pack(pady=10)
    time.sleep(1)
    progress['value']=80
    root.update_idletasks()
    progress.pack(pady=10)
    time.sleep(1)
    progress['value']=100
    progress.pack(pady=10)
    try:
        url = wikipedia.page(topic).url

    except wikipedia.DisambiguationError as e:
        url = "Please be more specific"

    label4 = tk.Label(root, text=url, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)


def addtofile():
    print(url)
    file_object = open('urls.txt', 'a')

    file_object.write(url+"\n")

    file_object.close()

    label5 = tk.Label(root, text="URL added", font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 280, window=label5)


button1 = tk.Button(text='Fetch the page', command=fetchurl,
                    bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

button1 = tk.Button(text='Add to file', command=addtofile,
                    bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 260, window=button1)

root.mainloop()
