#import tkinter as tk

'''
root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 20, window=entry1)


def doSearch():
    words = entry1.get()

    label1 = tk.Label(root, text=words)
    canvas1.create_window(200, 80, window=label1)


button1 = tk.Button(text='Get the Square Root', command=doSearch)
canvas1.create_window(200, 50, window=button1)

root.mainloop()'''

from tkinter import *

root = Tk()
root.title("Mediamarkt Smartphone Comparison Tool")
lbl = Label(root, text="Search for your phone here:")
lbl.grid(row=0, column=0)
height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i+1, column=j+1)

mainloop()
