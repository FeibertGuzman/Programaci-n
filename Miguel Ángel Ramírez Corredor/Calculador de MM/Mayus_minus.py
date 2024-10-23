import tkinter as tk

def convertir_mayusculas():
    texto = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, texto.upper())

def convertir_minusculas():
    texto = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, texto.lower())

def convertir_primera_mayuscula():
    texto = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, texto.capitalize())

def capitalizar_primeras_letras():
    texto = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, texto.title())

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Convertidor de texto")

# Campo de entrada
entrada = tk.Entry(ventana, width=50)
entrada.pack(padx=10, pady=10)

# Botón para convertir a mayúsculas
btn_mayusculas = tk.Button(ventana, text="Convertir a Mayúsculas", command=convertir_mayusculas)
btn_mayusculas.pack(padx=10, pady=5)

# Botón para convertir a minúsculas
btn_minusculas = tk.Button(ventana, text="Convertir a Minúsculas", command=convertir_minusculas)
btn_minusculas.pack(padx=10, pady=5)

# Botón para convertir la primera letra en mayúscula
btn_primera_mayuscula = tk.Button(ventana, text="Convertir la Primera letra en Mayúscula", command=convertir_primera_mayuscula)
btn_primera_mayuscula.pack(padx=10, pady=5)

# Botón para capitalizar primeras letras de cada palabra
btn_capitalizar_palabras = tk.Button(ventana, text="Capitalizar Primeras Letras de Cada Palabra", command=capitalizar_primeras_letras)
btn_capitalizar_palabras.pack(padx=10, pady=5)

# Ejecutar la ventana
ventana.mainloop()
