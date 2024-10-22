import tkinter as tk
from tkinter import messagebox

def validacion(texto):
    return all(caracter.isalpha() or caracter.isspace() for caracter in texto)

def convertir_primeras_letras_mayusculas():
    texto=entrada.get()

    if validacion(texto):
        texto_capitalizado= ' '.join(word.capitalize() for word in texto.split())
        resultado.set(texto_capitalizado)
    else: 
        messagebox.showerror("Error", "Por favor, ingrese solo letras")

def mayus ():
    texto =entrada.get()

    if validacion(texto):
        resultado.set(texto.upper())
    else:
        messagebox.showerror("Error", "Por favor, ingrese solo letras")

def min():
    texto=entrada.get()

    if validacion(texto):
        resultado.set(texto.lower())
    else:
        messagebox.showerror("Error", "Por favor, ingrese solo letras")

def mayu_ini():
    texto=entrada.get()

    if validacion(texto):
        resultado.set(texto.capitalize())
    else:
        messagebox.showerror("Error", "Por favor, ingrese solo letras")

#Parte gráfica

#Ventana
ventana = tk.Tk()
ventana.title("Conversor de texto")

#Almacenar resultado
resultado=tk.StringVar()

#Crear cuadro
entrada = tk.Entry(ventana, width=50)
entrada.pack(padx=15, pady=15)

#Boton Mayuscula
boton_mayu=tk.Button(ventana, text="Convertir a Mayúsculas", command=mayus)
boton_mayu.pack(padx=10, pady=5)

#Boton Minuscula
boton_min=tk.Button(ventana, text="Convertur a Minúsculas", command=min)
boton_min.pack(padx=10, pady=5)

#Boton Capitalizar inicial
boton_cap_in=tk.Button(ventana, text="Capitalizar Primera Letra", command=mayu_ini)
boton_cap_in.pack(padx=10, pady=5)

#Boton Capitalizar todo
boton_todas_inician_Mayu= tk.Button(ventana, text="Capitalizar Primeras letras de cada palabra", command=convertir_primeras_letras_mayusculas)
boton_todas_inician_Mayu.pack(padx=10, pady=5)

#Etiqueta
etiqueta_resultado=tk.Label(ventana, textvariable=resultado, font=("Arial", 14, "bold"), fg="blue", background="gray")
etiqueta_resultado.pack(padx=10, pady=10)

#Ejecutar
ventana.mainloop()