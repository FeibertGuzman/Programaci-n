import tkinter as tk

# Función para convertir a mayúsculas
def a_mayusculas():
    texto = entrada.get()
    resultado.set(texto.upper())

# Función para convertir a minúsculas
def a_minusculas():
    texto = entrada.get()
    resultado.set(texto.lower())

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)
    resultado.set("")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Texto")
ventana.geometry("400x200")

# Variables de entrada y salida
resultado = tk.StringVar()

# Widgets: Entrada de texto
tk.Label(ventana, text="Ingresa el texto:", font=("Arial", 14)).pack(pady=10)
entrada = tk.Entry(ventana, font=("Arial", 14), width=30)
entrada.pack(pady=5)

# Botones para realizar las conversiones
tk.Button(ventana, text="A Mayúsculas", font=("Arial", 12), command=a_mayusculas).pack(pady=5)
tk.Button(ventana, text="A Minúsculas", font=("Arial", 12), command=a_minusculas).pack(pady=5)

# Mostrar el resultado
tk.Label(ventana, text="Resultado:", font=("Arial", 14)).pack(pady=10)
tk.Label(ventana, textvariable=resultado, font=("Arial", 14)).pack()

# Botón de limpiar
tk.Button(ventana, text="Limpiar", font=("Arial", 12), command=limpiar).pack(pady=10)

# Bucle principal
ventana.mainloop()
