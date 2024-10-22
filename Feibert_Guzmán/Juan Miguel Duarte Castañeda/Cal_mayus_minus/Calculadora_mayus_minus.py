import tkinter as tk
 
def convertir_mayusculas():
    texto = entrada.get()
    resultado.set(texto.upper())
 
def convertir_minusculas():
    texto = entrada.get()
    resultado.set(texto.lower())
 
def convertir_primera_letra_mayuscula():
    texto = entrada.get()
    resultado.set(texto.capitalize())
 
def capitalizar_primera_letra_cada_palabra():
    texto = entrada.get()
    resultado.set(texto.title())
 
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Convertidor de Texto")
 
# Variable para obtener el resultado
resultado = tk.StringVar()
 
# Entrada de texto
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=10)
 
# Botones para las diferentes conversiones
btn_mayusculas = tk.Button(ventana, text="Convertir a Mayúsculas", command=convertir_mayusculas)
btn_mayusculas.pack(pady=5)
 
btn_minusculas = tk.Button(ventana, text="Convertir a Minúsculas", command=convertir_minusculas)
btn_minusculas.pack(pady=5)
 
btn_primera_mayuscula = tk.Button(ventana, text="Convertir la Primera letra en Mayúscula", command=convertir_primera_letra_mayuscula)
btn_primera_mayuscula.pack(pady=5)
 
btn_capitalizar_palabras = tk.Button(ventana, text="Capitalizar Primeras Letras de Cada Palabra", command=capitalizar_primera_letra_cada_palabra)
btn_capitalizar_palabras.pack(pady=5)
 
# Mostrar el resultado
etiqueta_resultado = tk.Label(ventana, textvariable=resultado, width=50)
etiqueta_resultado.pack(pady=10)
 
# Iniciar el bucle de la aplicación
ventana.mainloop()
