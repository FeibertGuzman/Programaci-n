import tkinter as tk

def convertir(opcion):
    texto = entry_text.get()
    if opcion == 'mayusculas':
        resultado = texto.upper()
    elif opcion == 'minusculas':
        resultado = texto.lower()
    elif opcion == 'primera_mayuscula':
        resultado = texto.capitalize()
    elif opcion == 'primera_minuscula':
        resultado = texto[0].lower() + texto[1:] if texto else ""
    etiqueta_resultado.config(text=resultado)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Mayúsculas y Minúsculas")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Centrar la ventana
ventana.eval('tk::PlaceWindow . center')

# Entrada de texto
entry_text = tk.Entry(ventana, width=40, font=('Arial', 14))
entry_text.pack(pady=10)

# Botones
btn_mayusculas = tk.Button(ventana, text="Convertir a Mayúsculas", command=lambda: convertir('mayusculas'), font=('Arial', 12))
btn_mayusculas.pack(pady=3)

btn_minusculas = tk.Button(ventana, text="Convertir a Minúsculas", command=lambda: convertir('minusculas'), font=('Arial', 12))
btn_minusculas.pack(pady=3)

btn_primera_mayuscula = tk.Button(ventana, text="Primera Letra a Mayúscula", command=lambda: convertir('primera_mayuscula'), font=('Arial', 12))
btn_primera_mayuscula.pack(pady=3)

btn_primera_minuscula = tk.Button(ventana, text="Primera Letra a Minúscula", command=lambda: convertir('primera_minuscula'), font=('Arial', 12))
btn_primera_minuscula.pack(pady=3)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", wraplength=350, font=('Arial', 16), fg='blue')
etiqueta_resultado.pack(pady=(10, 5))  # Menos espacio en la parte inferior

# Iniciar el bucle principal
ventana.mainloop()
