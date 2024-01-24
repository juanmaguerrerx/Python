import tkinter as tk
from tkinter import ttk
from tkinter import messagebox #Para agregar alertas de mensajes
from tkcalendar import DateEntry #Para agregar un input para fechas 
import mysql.connector
from mysql.connector import Error


def list_emails():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bikes'
        )

        cursor = connection.cursor()

        select_query = "SELECT email FROM client"
        cursor.execute(select_query)
        emails = cursor.fetchall()

        combo_email['values'] = [email[0] for email in emails]

    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def list_bikes():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bikes'
        )

        cursor = connection.cursor()

        select_query = "SELECT bike_id, model FROM bike"
        cursor.execute(select_query)
        bikes = cursor.fetchall()

        combo_bike['values'] = [f"{bike[0]} - {bike[1]}" for bike in bikes]

    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def obtener_datos(tabla, campos):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bikes'
        )

        cursor = connection.cursor()

        select_query = f"SELECT {', '.join(campos)} FROM {tabla}"
        cursor.execute(select_query)
        datos = cursor.fetchall()

        return datos

    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insertar_registro(tabla, campos, valores):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bikes'
        )

        cursor = connection.cursor()

        # Insertar datos en la tabla especificada
        insert_query = f"INSERT INTO {tabla} ({', '.join(campos)}) VALUES ({', '.join(['%s' for _ in valores])})"
        cursor.execute(insert_query, valores)
        connection.commit()

        messagebox.showinfo("Éxito", "Fila insertada exitosamente")

    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insertar_alquiler():
    email = combo_email.get()
    bike_id = combo_bike.get()
    ini_dt = entry_ini.get()
    end_dt = entry_end.get()
    if not email or not bike_id or ini_dt >= end_dt if end_dt else False:
        messagebox.showerror("Error", "Datos de alquiler inválidos")
        return

    insertar_registro("rental", ["email", "bike_id", "ini_dt", "end_dt"], [email, bike_id, ini_dt, end_dt])

def listar_filas(tabla, campos):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bikes'
        )

        cursor = connection.cursor()

        select_query = f"SELECT * FROM {tabla}"
        cursor.execute(select_query)
        filas = cursor.fetchall()

        ventana_filas = tk.Toplevel(root)
        ventana_filas.title(f"Tabla {tabla.capitalize()} - Filas")

        for i, fila in enumerate(filas):
            ttk.Label(ventana_filas, text=f"Fila {i + 1}: {fila}").pack()

    except Error as e:
        messagebox.showerror("Error", f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

root = tk.Tk()
root.title("Insertar en la Tabla de Alquiler")

label_email = ttk.Label(root, text="Email:")
combo_email = ttk.Combobox(root, state="readonly", values=[email[0] for email in obtener_datos("client", ["email"])])
label_bike = ttk.Label(root, text="Bike ID:")
combo_bike = ttk.Combobox(root, state="readonly", values=[f"{bike[0]} - {bike[1]}" for bike in obtener_datos("bike", ["bike_id", "model"])])
label_ini = ttk.Label(root, text="Fecha de Inicio:")
entry_ini = DateEntry(root, date_pattern="yyyy-mm-dd")
label_end = ttk.Label(root, text="Fecha de Fin:")
entry_end = DateEntry(root, date_pattern="yyyy-mm-dd")
button_insertar = ttk.Button(root, text="Insertar", command=insertar_alquiler)
button_listar = ttk.Button(root, text="Listar Filas", command=lambda: listar_filas("rental", ["email", "bike_id", "ini_dt", "end_dt"]))

label_email.grid(row=0, column=0, padx=5, pady=5)
combo_email.grid(row=0, column=1, padx=5, pady=5)
label_bike.grid(row=1, column=0, padx=5, pady=5)
combo_bike.grid(row=1, column=1, padx=5, pady=5)
label_ini.grid(row=2, column=0, padx=5, pady=5)
entry_ini.grid(row=2, column=1, padx=5, pady=5)
label_end.grid(row=3, column=0, padx=5, pady=5)
entry_end.grid(row=3, column=1, padx=5, pady=5)
button_insertar.grid(row=4, column=1, padx=5, pady=10)
button_listar.grid(row=5, column=0, columnspan=2, pady=10)

list_emails()
list_bikes()

root.mainloop()
