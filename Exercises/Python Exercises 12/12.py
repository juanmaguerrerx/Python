import tkinter as tk

window = tk.Tk()
items = []
labErr = tk.Label()

def addItem():
    item = ent.get()
    items.append(item)

def displayAll():
    label.config(text=items)

def clearItem():
    items.clear()

def removeItem():
    item = ent.get()
    if item in items:
        items.remove(item)

def popItem():
    num = ent.get()
    items.pop(int(num))  # Convert num to an integer before using it

def checkItemExists():
    item = ent.get()
    if item in items:
        labErr.config(text="Está")
    else:
        labErr.config(text="No está")

dis = tk.Button(text='Display All', command=displayAll)
clear = tk.Button(text='Clear', command=clearItem)
add = tk.Button(text='Add item', command=addItem)
remove = tk.Button(text='Remove Item', command=removeItem)
pop = tk.Button(text='Pop Item', command=popItem)
check = tk.Button(text='Check Item', command=checkItemExists)
ent = tk.Entry()
label = tk.Label(text=items)

dis.pack()
clear.pack()
add.pack()
remove.pack()
pop.pack()
check.pack()
ent.pack()
label.pack()
labErr.pack()

window.mainloop()
