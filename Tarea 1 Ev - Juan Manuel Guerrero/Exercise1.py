import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import re

def insertar_cliente():
    email = entry_email.get()
    password = entry_password.get()

    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bikes'
        )

        cursor = conexion.cursor()

        if not email or not validar_email(email):
            etiqueta_estado.config(text="Error: Email inválido",background="red")
            return

        if not password or len(password) <= 8:
            etiqueta_estado.config(text="Error: La contraseña debe tener más de 8 caracteres",background="red")
            return

        query_insertar = "INSERT INTO client (email, password) VALUES (%s, %s)"
        cursor.execute(query_insertar, (email, password))
        conexion.commit()

        etiqueta_estado.config(text="OK: Fila insertada correctamente", background="green")

    except Error as e:
        etiqueta_estado.config(text=f"Error: {e}", background="red")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def listar_filas():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bikes'
        )

        cursor = conexion.cursor()

        query_seleccionar = "SELECT * FROM client"
        cursor.execute(query_seleccionar)
        filas = cursor.fetchall()

        ventana_filas = tk.Toplevel(root)
        ventana_filas.title("Tabla de Clientes - Filas")

        for i, fila in enumerate(filas):
            ttk.Label(ventana_filas, text=f"Fila {i + 1}: {fila}").pack()

    except Error as e:
        etiqueta_estado.config(text=f"Error: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()



def validar_email(email):
    patron_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    
    if not patron_email.match(email):
        return False
    
    return True


root = tk.Tk()
root.title("Insertar en la Tabla de Clientes")

etiqueta_email = ttk.Label(root, text="Email:")
entry_email = ttk.Entry(root)
etiqueta_password = ttk.Label(root, text="Contraseña:")
entry_password = ttk.Entry(root, show="*")
boton_insertar = ttk.Button(root, text="Insertar", command=insertar_cliente)
etiqueta_estado = ttk.Label(root, text="")
boton_listar = ttk.Button(root, text="Listar Filas", command=listar_filas)

etiqueta_email.grid(row=0, column=0, padx=5, pady=5)
entry_email.grid(row=0, column=1, padx=5, pady=5)
etiqueta_password.grid(row=1, column=0, padx=5, pady=5)
entry_password.grid(row=1, column=1, padx=5, pady=5)
boton_insertar.grid(row=2, column=1, padx=5, pady=10)
etiqueta_estado.grid(row=3, column=0, columnspan=2, pady=5)
boton_listar.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()