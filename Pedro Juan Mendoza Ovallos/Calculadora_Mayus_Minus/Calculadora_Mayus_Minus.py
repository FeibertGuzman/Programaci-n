import tkinter as tk
from tkinter import messagebox

def convertir_mayusculas():
    texto = entrada.get()
    if texto:
        entrada.delete(0, tk.END)
        entrada.insert(0, texto.upper())
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa texto.")

def convertir_minusculas():
    texto = entrada.get()
    if texto:
        entrada.delete(0, tk.END)
        entrada.insert(0, texto.lower())
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa texto.")

def convertir_primera_mayuscula():
    texto = entrada.get()
    if texto:
        entrada.delete(0, tk.END)
        entrada.insert(0, texto.capitalize())
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa texto.")

def capitalizar_palabras():
    texto = entrada.get()
    if texto:
        entrada.delete(0, tk.END)
        entrada.insert(0, texto.title())
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa texto.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Convertidor de Texto")
ventana.geometry("300x200")

# Entrada de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Botones para las diferentes funciones
boton_mayusculas = tk.Button(ventana, text="Convertir a Mayúsculas", command=convertir_mayusculas)
boton_mayusculas.pack(pady=5)

boton_minusculas = tk.Button(ventana, text="Convertir a Minúsculas", command=convertir_minusculas)
boton_minusculas.pack(pady=5)

boton_primera_mayuscula = tk.Button(ventana, text="Convertir la Primera letra en Mayúscula", command=convertir_primera_mayuscula)
boton_primera_mayuscula.pack(pady=5)

boton_capitalizar_palabras = tk.Button(ventana, text="Capitalizar Primeras Letras de Cada Palabra", command=capitalizar_palabras)
boton_capitalizar_palabras.pack(pady=5)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
