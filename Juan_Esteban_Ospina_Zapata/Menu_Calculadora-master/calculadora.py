#importo las librerias que utilizaré
from tkinter import Tk, Label, Button, Entry, Menu, messagebox, Listbox, Scrollbar


#Funcion para actualizar el historial despues de cada accion
def actualizar_historial(operacion, resultado):
    historial.insert('end', f"{operacion} = {resultado}")

#Creamos las funciones
def fnSuma():
    try:
        resultado = float(entrada1.get()) + float(entrada2.get())
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        actualizar_historial(f"{entrada1.get()} + {entrada2.get()}", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def fnResta():
    try:
        resultado = float(entrada1.get()) - float(entrada2.get())
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        actualizar_historial(f"{entrada1.get()} + {entrada2.get()}", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def fnMultiplicacion():
    try:
        resultado = float(entrada1.get()) * float(entrada2.get())
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        actualizar_historial(f"{entrada1.get()} + {entrada2.get()}", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def fnDivision():
    try:
        divisor = float(entrada2.get())
        if divisor != 0:
            resultado = float(entrada1.get()) / divisor
            etiqueta_resultado.config(text=f"Resultado: {resultado}")
            actualizar_historial(f"{entrada1.get()} + {entrada2.get()}", resultado)
        else:
            messagebox.showerror("Error", "División por cero no permitida.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def fnValorAbsoluto():
    try:
        resultado = abs(float(entrada1.get()))
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        actualizar_historial(f"{entrada1.get()} + {entrada2.get()}", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

def fnMCM():
    try:
        from math import gcd
        a = int(entrada1.get())
        b = int(entrada2.get())
        resultado = abs(a * b) // gcd(a, b)
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        actualizar_historial(f"{entrada1.get()} + {entrada2.get()}", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")

def fnMCD():
    try:
        from math import gcd
        resultado = gcd(int(entrada1.get()), int(entrada2.get()))
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        actualizar_historial(f"{entrada1.get()} + {entrada2.get()}", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")

#Funcion para eliminar el historial de entrada
def eliminar_entrada():
    seleccion = historial.curselection()
    if seleccion:
        historial.delete(seleccion)

#Funcion para editar el historial de entrada
def editar_entrada():
    seleccion = historial.curselection()
    if seleccion:
        nueva_operacion = input("Nueva operación:")
        historial.delete(seleccion)
        historial.insert(seleccion, nueva_operacion)

#Funcion para cambiar el fondo de la ventana
def cambiar_color_fondo(color):
    vent.config(bg=color)

#Funcion para cambiar la fuente de la ventana
def cambiar_fuente(fuente):
    for widget in vent.winfo_children():
        if isinstance(widget, (Label, Button, Entry)):
            widget.config(font=(fuente, 12))

#Creación del menú, barra superior
def crear_menu(vent):

    #creación del objeto menú, para la barra superior
    barra_menu = Menu(vent)
    vent.config(menu=barra_menu)
    
    #Agregamos el menú al primer item de la barra superior
    menu_inicio = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Salir", command=vent.destroy)

    #Agregamos el menú al segundo item de la barra superior
    menu_operacion = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Operación", menu=menu_operacion)
    menu_operacion.add_command(label="Sumar", command=fnSuma)
    menu_operacion.add_command(label="Restar", command=fnResta)
    menu_operacion.add_command(label="Multiplicación", command=fnMultiplicacion)
    menu_operacion.add_command(label="División", command=fnDivision)
    menu_operacion.add_command(label="Valor Absoluto", command=fnValorAbsoluto)
    menu_operacion.add_command(label="Mínimo Común Múltiplo", command=fnMCM)
    menu_operacion.add_command(label="Máximo Común Divisor", command=fnMCD)

    #Creamos el menu donde se van a editar los datos del historial
    menu_editar = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Editar", menu=menu_editar)
    menu_editar.add_command(label="Eliminar", command=eliminar_entrada)
    menu_editar.add_command(label="Editar", command=editar_entrada)

    #Creamos el menu donde se van a personalizar el color de fondo de la ventana
    menu_color_fondo = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Color de fondo", menu=menu_color_fondo)
    menu_color_fondo.add_command(label="Color de fondo Blanco", command=lambda: cambiar_color_fondo("white"))
    menu_color_fondo.add_command(label="Color de fondo Gris", command=lambda: cambiar_color_fondo("white"))

    #Creamos el menu donde se van a personalizar la fuente de la ventana
    menu_fuente = Menu(barra_menu, tearoff=0)
    menu_fuente.add_cascade(label="Cambiar fuente", menu=menu_fuente)
    menu_color_fondo.add_command(label="Fuente Arial", command=lambda: cambiar_fuente("Arial"))
    menu_color_fondo.add_command(label="Fuente Verdana", command=lambda: cambiar_fuente("Verdana"))

#creamos y agregamos los estilos a la ventana CALCULADORA
def crear_ventana():
    vent = Tk()
    vent.title("Calculadora Dev-Juanes")
    vent.geometry("400x300")
    vent.config(bg="#f0f0f0")
    
    crear_menu(vent)
    
    #definimos que tipo de datos se ingresarán 
    global entrada1, entrada2, etiqueta_resultado, historial # (variable historial para almacenar el mismo de las acciones)
    
    Label(vent, text="Número 1:", bg="#f0f0f0").pack(pady=5)
    entrada1 = Entry(vent)
    entrada1.pack(pady=5)
    
    Label(vent, text="Número 2:", bg="#f0f0f0").pack(pady=5)
    entrada2 = Entry(vent)
    entrada2.pack(pady=5)
    
    etiqueta_resultado = Label(vent, text="Resultado:", bg="#f0f0f0", font=("Arial", 12, "bold"))
    etiqueta_resultado.pack(pady=20)
    
    Button(vent, text="Sumar", command=fnSuma, bg="#4CAF50", fg="white").pack(side="left", padx=10, pady=10)
    Button(vent, text="Restar", command=fnResta, bg="#f44336", fg="white").pack(side="left", padx=10, pady=10)

    #creamos un ListBox para almacenar y mostrar el historial de acciones
    historial = Listbox(vent, height=10, width=50)
    historial.pack(side='right', fill='y', padx=10, pady=10)

    #creamos un scrollbar para el Listbox
    scrollbar = Scrollbar(vent, orient='vertical')
    scrollbar.config(command=historial.yview)
    scrollbar.pack(side='right', fill='y')
    historial.config(yscrollcommand=scrollbar.set)

    return vent

vent = crear_ventana()
vent.mainloop()
