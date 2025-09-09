import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime, timedelta
from calendario import generar_calendario, cargar_guia_de_marca
from export import exportar_excel, exportar_json
import json

# Función para limitar el rango de fechas a un trimestre
def limite(fecha_inicio, fecha_fin, label_mensaje):
    # Limitar la fecha de fin a un trimestre (3 meses)
    max_fecha_fin = fecha_inicio + timedelta(days=90)  # 90 días = 3 meses
    if fecha_fin > max_fecha_fin:
        mensaje = f"Advertencia: La fecha de fin es mayor que 3 meses desde la fecha de inicio.\nAjustando a {max_fecha_fin.strftime('%d-%m-%Y')}."
        label_mensaje.config(text=mensaje, fg="red")  # Mostrar mensaje en el label
        fecha_fin = max_fecha_fin  # Ajustar la fecha de fin a 3 meses desde la fecha de inicio
    else:
        label_mensaje.config(text="", fg="black")  # Limpiar el mensaje si no hay ajuste
    return fecha_fin

# Función que se ejecuta al presionar "Generar Calendario"
def generar():
    try:
        # Obtener las fechas seleccionadas desde el calendario (en formato mm/dd/yyyy)
        fecha_inicio = cal_inicio.get_date()
        fecha_fin = cal_fin.get_date()

        # Convertir las fechas a formato datetime
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%m/%d/%Y")
            fecha_fin = datetime.strptime(fecha_fin, "%m/%d/%Y")
        except ValueError as e:
            messagebox.showerror("Error de formato", "El formato de fecha es incorrecto. Asegúrese de que sea MM/DD/YYYY.")
            return

        # Obtener la frecuencia de publicaciones
        frecuencia = int(entry_frecuencia.get())

        # Cargar la guía de la marca
        guia_marca = cargar_guia_de_marca()

        # Definir las redes sociales y clases
        redes_sociales1 = ["Instagram"]
        redes_sociales2 = ["TikTok"]
        redes_sociales3 = ["LinkedIn"]
        redes_sociales4 = ["Facebook"]
        redes_sociales5 = ["YouTube"]
        
        clases = ["informal", "intermedio", "profesional"]

        # Generar el calendario
        fecha_fin = limite(fecha_inicio, fecha_fin, label_mensaje)
        calendario = generar_calendario(redes_sociales1, clases, fecha_inicio, fecha_fin, frecuencia, guia_marca)
        calendario = generar_calendario(redes_sociales2, clases, fecha_inicio, fecha_fin, frecuencia, guia_marca)
        calendario = generar_calendario(redes_sociales3, clases, fecha_inicio, fecha_fin, frecuencia, guia_marca)
        calendario = generar_calendario(redes_sociales4, clases, fecha_inicio, fecha_fin, frecuencia, guia_marca)
        calendario = generar_calendario(redes_sociales5, clases, fecha_inicio, fecha_fin, frecuencia, guia_marca)
        


        # Exportar los resultados a JSON
        exportar_json(calendario)
        exportar_excel(calendario)

        # Mostrar el calendario en la tabla
        mostrar_en_tabla(calendario)

        messagebox.showinfo("Éxito", "Calendario generado y exportado correctamente.")

    except ValueError as e:
        messagebox.showerror("Error", f"Hubo un problema: {e}")

# Función para mostrar los datos en la tabla
def mostrar_en_tabla(calendario):
    # Limpiar la tabla antes de llenarla
    for row in tabla.get_children():
        tabla.delete(row)

    # Insertar datos en la tabla para todas las redes sociales
    for red_social, clases in calendario.items():
        for clase, publicaciones in clases.items():
            for pub in publicaciones:
                tabla.insert("", "end", values=(
                    pub["fecha"],
                    pub["red_social"],
                    pub["clase"],
                    pub["tema"],
                    pub["copy"],
                    pub["hashtags"]
                ))
# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Generador de Calendario de Publicaciones")

# Etiquetas y Calendarios
label_inicio = tk.Label(root, text="Fecha de inicio:")
label_inicio.pack(pady=10)
cal_inicio = Calendar(root, date_pattern="mm/dd/yyyy")
cal_inicio.pack(pady=10)

label_fin = tk.Label(root, text="Fecha de fin:")
label_fin.pack(pady=10)
cal_fin = Calendar(root, date_pattern="mm/dd/yyyy")
cal_fin.pack(pady=10)

# Frecuencia de publicaciones
label_frecuencia = tk.Label(root, text="Frecuencia de publicaciones (días):")
label_frecuencia.pack(pady=10)
entry_frecuencia = tk.Entry(root)
entry_frecuencia.pack(pady=10)

# Crear un label para mostrar el mensaje de advertencia sobre el trimestre
label_mensaje = tk.Label(root, text="", font=("Arial", 12), fg="black")
label_mensaje.pack(pady=10)

# Botón para generar el calendario
button_generar = tk.Button(root, text="Generar Calendario", command=generar)
button_generar.pack(pady=20)

# Crear la tabla para mostrar el JSON
tabla = ttk.Treeview(root, columns=("Fecha", "Red Social", "Clase", "Tema", "Copy", "Hashtags"), show="headings")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Red Social", text="Red Social")
tabla.heading("Clase", text="Clase")
tabla.heading("Tema", text="Tema")
tabla.heading("Copy", text="Copy")
tabla.heading("Hashtags", text="Hashtags")
tabla.pack(pady=20)

# Ejecutar la interfaz
root.mainloop()
