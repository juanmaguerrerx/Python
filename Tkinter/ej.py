#Creating a UI
import tkinter as tk

window = tk.Tk()
i=0
label3 = tk.Label(text='')
def saludar():
    global i
    global label3
    st = 'Has pulsado '+ repr(i) + ' veces'
    
    label3.config(text=st)
    label3.pack()
    i=i+1
#Create a label
label1 = tk.Label(text='Hola Mundo')
label2 = tk.Label(text='Me llamo Juan Manueh')
label1.pack()
label2.pack()
but1 = tk.Button(text='Pulsa aquí', command=saludar)
but1.pack()

#Entrada de texto
ent1=tk.Entry()

#Obtener ese texto
ent1.get()

window.mainloop()


