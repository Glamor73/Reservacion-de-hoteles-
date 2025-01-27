import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3

# Función para validar las fechas
def validar_fechas(fecha_entrada, fecha_salida):
    try:
        # Convertir las fechas a formato datetime
        entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d')
        salida = datetime.strptime(fecha_salida, '%Y-%m-%d')
        
        # Verificar que la fecha de entrada no sea posterior a la de salida
        if entrada >= salida:
            raise ValueError("La fecha de entrada debe ser anterior a la fecha de salida.")
        
        return True
    except ValueError as e:
        messagebox.showerror("Error de fecha", str(e))
        return False

# Función para consultar la base de datos y obtener las habitaciones disponibles
def consultar_disponibilidad():
    fecha_entrada = entry_entrada.get()
    fecha_salida = entry_salida.get()
    
    # Validar las fechas ingresadas
    if not validar_fechas(fecha_entrada, fecha_salida):
        return
    
    # Conectar a la base de datos y consultar las habitaciones disponibles
    conn = sqlite3.connect('hotel.db')
    cursor = conn.cursor()

    # Consulta SQL para obtener habitaciones disponibles entre las fechas seleccionadas
    cursor.execute('''
        SELECT habitacion, precio
        FROM habitaciones
        WHERE fecha_disponible >= ? AND fecha_disponible <= ?
    ''', (fecha_entrada, fecha_salida))

    habitaciones = cursor.fetchall()
    conn.close()

    # Mostrar los resultados
    resultado_text.delete(1.0, tk.END)  # Limpiar resultados anteriores
    if habitaciones:
        for habitacion in habitaciones:
            resultado_text.insert(tk.END, f"Habitación: {habitacion[0]} - Precio: ${habitacion[1]}\n")
    else:
        resultado_text.insert(tk.END, "No hay habitaciones disponibles para esas fechas.\n")

# Crear la ventana principal
root = tk.Tk()
root.title("Buscador de Habitaciones de Hotel")

# Etiquetas y campos de entrada
label_entrada = tk.Label(root, text="Fecha de entrada (YYYY-MM-DD):")
label_entrada.grid(row=0, column=0, padx=10, pady=10)

entry_entrada = tk.Entry(root)
entry_entrada.grid(row=0, column=1, padx=10, pady=10)

label_salida = tk.Label(root, text="Fecha de salida (YYYY-MM-DD):")
label_salida.grid(row=1, column=0, padx=10, pady=10)

entry_salida = tk.Entry(root)
entry_salida.grid(row=1, column=1, padx=10, pady=10)

# Botón para consultar disponibilidad
button_consultar = tk.Button(root, text="Consultar Disponibilidad", command=consultar_disponibilidad)
button_consultar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Área de resultados
resultado_text = tk.Text(root, height=10, width=50)
resultado_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la aplicación
root.mainloop()
