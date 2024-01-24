import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

def insertar_bicicleta():
    modelo = entry_modelo.get()
    color = combo_color.get()

    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bikes'
        )

        cursor = conexion.cursor()

        if not modelo:
            etiqueta_estado_bicicleta.config(text="Error: El modelo no puede estar vacío", background="red")
            return

        query_insertar = "INSERT INTO bike (model, color) VALUES (%s, %s)"
        cursor.execute(query_insertar, (modelo, color))
        conexion.commit()

        etiqueta_estado_bicicleta.config(text="OK: Fila insertada correctamente",background="green")

    except Error as e:
        etiqueta_estado_bicicleta.config(text=f"Error: {e}",background="red")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def listar_filas_bicicleta():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bikes'
        )

        cursor = conexion.cursor()

        query_seleccionar = "SELECT * FROM bike"
        cursor.execute(query_seleccionar)
        filas = cursor.fetchall()

        ventana_filas_bicicleta = tk.Toplevel(root_bicicleta)
        ventana_filas_bicicleta.title("Tabla de Bicicletas - Filas")

        for i, fila in enumerate(filas):
            ttk.Label(ventana_filas_bicicleta, text=f"Fila {i + 1}: {fila}").pack()

    except Error as e:
        etiqueta_estado_bicicleta.config(text=f"Error: {e}", background="red")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

root_bicicleta = tk.Tk()
root_bicicleta.title("Insertar en la Tabla de Bicicletas")

etiqueta_modelo = ttk.Label(root_bicicleta, text="Modelo:")
entry_modelo = ttk.Entry(root_bicicleta)
etiqueta_color = ttk.Label(root_bicicleta, text="Color:")
combo_color = ttk.Combobox(root_bicicleta, values=["Blanco", "Rojo", "Azul", "Verde"])
boton_insertar_bicicleta = ttk.Button(root_bicicleta, text="Insertar", command=insertar_bicicleta)
etiqueta_estado_bicicleta = ttk.Label(root_bicicleta, text="")
boton_listar_filas_bicicleta = ttk.Button(root_bicicleta, text="Listar Filas", command=listar_filas_bicicleta)

etiqueta_modelo.grid(row=0, column=0, padx=5, pady=5)
entry_modelo.grid(row=0, column=1, padx=5, pady=5)
etiqueta_color.grid(row=1, column=0, padx=5, pady=5)
combo_color.grid(row=1, column=1, padx=5, pady=5)
boton_insertar_bicicleta.grid(row=2, column=1, padx=5, pady=10)
etiqueta_estado_bicicleta.grid(row=3, column=0, columnspan=2, pady=5)
boton_listar_filas_bicicleta.grid(row=4, column=0, columnspan=2, pady=10)

root_bicicleta.mainloop()
