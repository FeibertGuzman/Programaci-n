from tkinter import Tk, Label, Button, Entry, Menu, messagebox

def fnSuma():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        entry_resultado.config(state='normal')  # Cambiamos el estado a normal temporalmente
        entry_resultado.delete(0, 'end')
        entry_resultado.insert(0, str(resultado))
        entry_resultado.config(state='readonly')  # Volvemos a ponerlo en readonly
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def fnResta():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, 'end')
        entry_resultado.insert(0, str(resultado))
        entry_resultado.config(state='readonly')
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def fnMultiplicacion():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, 'end')
        entry_resultado.insert(0, str(resultado))
        entry_resultado.config(state='readonly')
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def fnDivision():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            raise ValueError("División por cero.")
        resultado = num1 / num2
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, 'end')
        entry_resultado.insert(0, str(resultado))
        entry_resultado.config(state='readonly')
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def crear_menu(vent):
    barra_menu = Menu(vent)
    vent.config(menu=barra_menu)
    
    menu_inicio = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Salir", command=vent.destroy)

def crear_ventana():
    vent = Tk()
    vent.title("Calculadora Completa")

    # Ajustar el tamaño de la ventana
    vent.geometry("400x300")  # Hacemos la ventana más grande

    # Crear el menú
    crear_menu(vent)
    
    # Crear widgets con espaciado
    Label(vent, text="Número 1:").grid(row=0, column=0, padx=10, pady=10)
    global entry_num1
    entry_num1 = Entry(vent, width=20)  # Ajustamos el ancho de las entradas
    entry_num1.grid(row=0, column=1, padx=10, pady=10)
    
    Label(vent, text="Número 2:").grid(row=1, column=0, padx=10, pady=10)
    global entry_num2
    entry_num2 = Entry(vent, width=20)
    entry_num2.grid(row=1, column=1, padx=10, pady=10)
    
    Label(vent, text="Resultado:").grid(row=2, column=0, padx=10, pady=10)
    global entry_resultado
    entry_resultado = Entry(vent, width=20, state='readonly')  # Lo ponemos como readonly desde el principio
    entry_resultado.grid(row=2, column=1, padx=10, pady=10)
    
    # Ajustar tamaño de botones y aplicar espaciado
    Button(vent, text="Sumar", command=fnSuma, width=20).grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
    Button(vent, text="Restar", command=fnResta, width=20).grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
    Button(vent, text="Multiplicar", command=fnMultiplicacion, width=20).grid(row=9, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
    Button(vent, text="Dividir", command=fnDivision, width=20).grid(row=10, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    return vent

vent = crear_ventana()
vent.mainloop()
