import tkinter as tk

# Función para agregar números u operadores a la entrada
def agregar(valor):
    entrada.insert(tk.END, valor)

# Función para evaluar la expresión
def evaluar():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Entrada de texto para mostrar los números y resultados
entrada = tk.Entry(ventana, font=("Arial", 20), justify="right", bd=10)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de la calculadora
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Añadir los botones a la ventana en una cuadrícula
fila, columna = 1, 0
for boton in botones:
    if boton == "=":
        btn = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15), command=evaluar)
    else:
        btn = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                        command=lambda b=boton: agregar(b))
    btn.grid(row=fila, column=columna, padx=5, pady=5)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botón de limpiar toda la entrada
btn_limpiar = tk.Button(ventana, text="C", width=23, height=2, font=("Arial", 15), command=limpiar)
btn_limpiar.grid(row=fila, column=0, columnspan=4, padx=5, pady=5)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
