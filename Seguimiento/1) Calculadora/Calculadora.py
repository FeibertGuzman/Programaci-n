import tkinter as tk
from tkinter import messagebox, Listbox, colorchooser
from math import gcd  # Importar la función gcd

# Funciones matemáticas
def suma():
    a, b = obtener_valores()
    if a is not None and b is not None:
        resultado = a + b
        mostrar_resultado(f"La suma de {a} + {b} = {resultado}")

def resta():
    a, b = obtener_valores()
    if a is not None and b is not None:
        resultado = a - b
        mostrar_resultado(f"La resta de {a} - {b} = {resultado}")

def multiplicacion():
    a, b = obtener_valores()
    if a is not None and b is not None:
        resultado = a * b
        mostrar_resultado(f"La multiplicación de {a} * {b} = {resultado}")

def division():
    a, b = obtener_valores()
    if a is not None and b is not None:
        if b == 0:
            mostrar_resultado("Error: No se puede dividir por 0")
        else:
            resultado = a / b
            mostrar_resultado(f"La división de {a} / {b} = {resultado}")

def valor_absoluto():
    a, b = obtener_valores()
    if a is not None and b is not None:
        resultado_a = abs(a)
        resultado_b = abs(b)
        mostrar_resultado(f"El valor absoluto de {a} = {resultado_a}\nEl valor absoluto de {b} = {resultado_b}")


def mcm():
    a, b = obtener_valores_enteros()  # Asegurar que sean enteros
    if a is not None and b is not None:
        resultado = abs(a * b) // gcd(a, b)
        mostrar_resultado(f"El MCM de {a} y {b} = {resultado}")

def mcd():
    a, b = obtener_valores_enteros()  # Asegurar que sean enteros
    if a is not None and b is not None:
        resultado = gcd(a, b)
        mostrar_resultado(f"El MCD de {a} y {b} = {resultado}")

# Funciones auxiliares
def obtener_valores():
    try:
        a = float(entry_numero1.get())
        b = float(entry_numero2.get())
        return a, b
    except ValueError:
        mostrar_resultado("Error: Introduce valores numéricos válidos.")
        return None, None

def obtener_valores_enteros():
    try:
        a = int(entry_numero1.get())  # Convertir a enteros
        b = int(entry_numero2.get())  # Convertir a enteros
        return a, b
    except ValueError:
        mostrar_resultado("Error: Introduce números enteros válidos para MCM y MCD.")
        return None, None

def obtener_valor_unico():
    try:
        a = float(entry_numero1.get())
        return a
    except ValueError:
        mostrar_resultado("Error: Introduce un valor numérico válido.")
        return None

def mostrar_resultado(mensaje):
    resultado_text.delete(1.0, tk.END)  # Limpiar cuadro de texto
    resultado_text.insert(tk.END, mensaje)  # Mostrar resultado
    agregar_historial(mensaje)

# Función para agregar al historial
def agregar_historial(mensaje):
    historial_listbox.insert(tk.END, mensaje)

# Función para calcular si el texto debe ser blanco o negro basado en el color
def color_texto_en_base_a_fondo(hex_color):
    # Convertir color HEX a RGB
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    # Calcular luminosidad
    luminosidad = (r*0.299 + g*0.587 + b*0.114)
    # Si la luminosidad es baja, usar texto blanco, de lo contrario, usar texto negro
    return "white" if luminosidad < 150 else "black"

# Función para cambiar el fondo de la calculadora
def cambiar_fondo():
    color = colorchooser.askcolor(title="Elige un color de fondo")[1]  # Escoger color
    if color:
        texto_color = color_texto_en_base_a_fondo(color)  # Determinar el color del texto
        ventana.config(bg=color)
        for widget in ventana.winfo_children():
            try:
                widget.config(bg=color, fg=texto_color)
            except:
                pass

# Crear ventana principal
def crear_menu():
    global entry_numero1, entry_numero2, resultado_text, historial_listbox, ventana
    
    ventana = tk.Tk()
    ventana.title("Calculadora con Tkinter")
    ventana.geometry("500x500")

    # Crear menú
    menubar = tk.Menu(ventana)
    
    # Menú de operaciones
    menu_inicio = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Salir", command=ventana.destroy)

    operaciones_menu = tk.Menu(menubar, tearoff=0)
    operaciones_menu.add_command(label="Suma", command=suma)
    operaciones_menu.add_command(label="Resta", command=resta)
    operaciones_menu.add_command(label="Multiplicación", command=multiplicacion)
    operaciones_menu.add_command(label="División", command=division)
    operaciones_menu.add_command(label="Valor Absoluto", command=valor_absoluto)
    operaciones_menu.add_command(label="MCM", command=mcm)
    operaciones_menu.add_command(label="MCD", command=mcd)
    menubar.add_cascade(label="Operaciones", menu=operaciones_menu)

    # Menú de opciones de fondo
    opciones_menu = tk.Menu(menubar, tearoff=0)
    opciones_menu.add_command(label="Cambiar color de fondo", command=cambiar_fondo)
    menubar.add_cascade(label="Opciones", menu=opciones_menu)
    
    # Campo de entrada para los números
    tk.Label(ventana, text="Número 1:").pack(pady=5)
    entry_numero1 = tk.Entry(ventana)
    entry_numero1.pack(pady=5)

    tk.Label(ventana, text="Número 2 (si aplica):").pack(pady=5)
    entry_numero2 = tk.Entry(ventana)
    entry_numero2.pack(pady=5)

    # Campo de texto para mostrar el resultado
    tk.Label(ventana, text="Resultado:").pack(pady=5)
    resultado_text = tk.Text(ventana, height=2, width=40)
    resultado_text.pack(pady=5)

    # Historial de operaciones
    tk.Label(ventana, text="Historial:").pack(pady=5)
    historial_listbox = Listbox(ventana, height=10, width=60)
    historial_listbox.pack(pady=5)

    ventana.config(menu=menubar)
    ventana.mainloop()

if __name__ == "__main__":
    crear_menu()