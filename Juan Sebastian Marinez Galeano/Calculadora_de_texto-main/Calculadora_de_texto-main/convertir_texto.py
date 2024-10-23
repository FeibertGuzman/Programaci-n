from tkinter import *  
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import constantes  

def es_texto_valido(texto):
    return all(caracter.isalpha() or caracter.isspace() for caracter in texto)

def convertir_primeras_letras_mayusculas():
    texto = entrada.get()

    if es_texto_valido(texto):
        texto_capitalizado = " ".join(word.capitalize() for word in texto.split())
        resultado.set(texto_capitalizado)  
    else:
        messagebox.showerror("Error", "Por favor ingrese SOLO letras.")

def convertir_mayusculas():
    texto = entrada.get()

    if es_texto_valido(texto):
        texto_capitalizado = " ".join(word.upper() for word in texto.split())
        resultado.set(texto_capitalizado)  
    else:
        messagebox.showerror("Error", "Por favor ingrese SOLO letras.")

def convertir_primeras_letras_minuscula():
    texto = entrada.get()

    if es_texto_valido(texto):
        if texto: 
            texto_MAYUS = texto[0].lower() + texto[1:].upper()
        resultado.set(texto_MAYUS)
    else:
        messagebox.showerror("Error", "Por favor ingrese SOLO letras.")



def convertir_minuscula():
    texto = entrada.get()

    if es_texto_valido(texto):
        texto_Primera_Minuscula = " ".join(word.lower() for word in texto.split())
        resultado.set(texto_Primera_Minuscula)  
    else:
        messagebox.showerror("Error", "Por favor ingrese SOLO letras.")
# Parte gráfica
# Ventana
ventana = tk.Tk()
ventana.title("Conversor de texto")
ventana.geometry("+500+80")  
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Estilos
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(ventana, style="mainframe.TFrame")
mainframe.grid(row=0, column=0, sticky=constantes.sticky)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)

resultado = tk.StringVar()

entrada = tk.Entry(mainframe, width=50)
entrada.grid(row=0, column=0, columnspan=2, sticky=constantes.sticky)  

# botones
boton_todas_inician_mayus = tk.Button(mainframe, text="Capitaliza", command=convertir_primeras_letras_mayusculas)
boton_todas_inician_mayus.grid(row=1, column=0, sticky=constantes.sticky )  

boton_todas_inician_minus = tk.Button(mainframe, text="Minusculas", command=convertir_primeras_letras_minuscula)
boton_todas_inician_minus.grid(row=1, column=1, sticky=constantes.sticky)  

boton_todas_mayus = tk.Button(mainframe, text="Bloq mayus", command=convertir_mayusculas)
boton_todas_mayus.grid(row=2, column=0,sticky=constantes.sticky)  

boton_todas_minus = tk.Button(mainframe, text="Todas Minusculas", command=convertir_minuscula)
boton_todas_minus.grid(row=2, column=1,sticky=constantes.sticky)  


# Etiqueta
etiqueta_resultado = tk.Label(mainframe, textvariable=resultado, font=constantes.letra, fg=constantes.fg)
etiqueta_resultado.grid(row=3, column=0, columnspan=2, sticky=constantes.sticky)  

ventana.mainloop()
