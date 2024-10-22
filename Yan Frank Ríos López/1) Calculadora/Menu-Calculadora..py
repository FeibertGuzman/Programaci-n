from tkinter import Tk, Label, Button, Entry, Menu, Listbox, Scrollbar, END, ANCHOR, simpledialog
import math, random

def crear_ventana():
    bg_color = "#1DC4FF"
    fg_color = "#333"
    font = ("Arial", 12)

    vent = Tk()
    vent.title("Mega Calculadora")
    vent.geometry("800x600")
    vent.configure(bg=bg_color)
    
    def fnSuma():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            f = float(n1) + float(n2)
            txt3.delete(0, 'end')
            txt3.insert(0, f)
            append_to_history(f"{n1} + {n2} = {f}")
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")

    def fnResta():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = float(n1) - float(n2)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
            append_to_history(f"{n1} - {n2} = {r}")
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")

    def fnMult():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            a = float(n1) * float(n2)
            txt3.delete(0, 'end')
            txt3.insert(0, a)
            append_to_history(f"{n1} * {n2} = {a}")
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")

    def fnDivi():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            n = float(n1) / float(n2)
            txt3.delete(0, 'end')
            txt3.insert(0, n)
            append_to_history(f"{n1} / {n2} = {n}")
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
        except ZeroDivisionError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")

    def fnValAbs():
        n1 = txt1.get()
        try:
            k = float(n1)
            valor_absoluto = abs(k)
            txt3.delete(0, 'end')
            txt3.insert(0, valor_absoluto)
            append_to_history(f"Abs({n1}) = {valor_absoluto}")
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")

    def fnMCM():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            n1 = int(n1)
            n2 = int(n2)
            mcm = abs(n1 * n2) // math.gcd(n1, n2)
            txt3.delete(0, 'end')
            txt3.insert(0, mcm)
            append_to_history(f"MCM({n1}, {n2}) = {mcm}")
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")

    def fnMCD():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            n1 = int(n1)
            n2 = int(n2)
            mcd = math.gcd(n1, n2)
            txt3.delete(0, 'end')
            txt3.insert(0, mcd)
            append_to_history(f"MCD({n1}, {n2}) = {mcd}")
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")

    def append_to_history(operation):
        history_listbox.insert(END, operation)

    def delete_history():
        selected_index = history_listbox.curselection()
        if selected_index:
           history_listbox.delete(selected_index)

    def edit_history():
        selected_index = history_listbox.curselection()
        if selected_index:
            old_value = history_listbox.get(selected_index)
            new_value = simpledialog.askstring("Editar", "Ingrese el nuevo valor:", initialvalue=old_value)
            if new_value:
                history_listbox.delete(selected_index)
                history_listbox.insert(selected_index, new_value)


    def changeBG():
        #vent.config(background = "#1DC4FF")
        colors = ["black", "green", "cyan", "white", "yellow", "red", "purple", "pink", "orange", "gray"]
        random_colors = random.choice(colors)
        vent.config(background= random_colors)
        lbl1.config(background= random_colors)
        lbl2.config(background= random_colors)
        lbl3.config(background= random_colors)

    def crear_menu(vent):
        barra_menu = Menu(vent)
        vent.config(menu=barra_menu)
        
        menu_inicio = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
        menu_inicio.add_command(label="Salir", command=vent.destroy)

        menu_operacion = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Operación", menu=menu_operacion)
        menu_operacion.add_command(label="Sumar", command=fnSuma)
        menu_operacion.add_command(label="Restar", command=fnResta)
        menu_operacion.add_command(label="Multiplicación", command=fnMult)
        menu_operacion.add_command(label="División", command=fnDivi)
        menu_operacion.add_command(label="Valor Absoluto", command=fnValAbs)
        menu_operacion.add_command(label="Mínimo Común Múltiplo", command=fnMCM)
        menu_operacion.add_command(label="Máximo Común Divisor", command=fnMCD)

    # Labels y Entries
    lbl1 = Label(vent, text="Número 1:", bg=bg_color, fg=fg_color, font=font)
    lbl1.place(x=50, y=30, width=150, height=30)
    txt1 = Entry(vent, bg="#fff")
    txt1.place(x=200, y=30, width=150, height=30)
    
    lbl2 = Label(vent, text="Número 2:", bg=bg_color, fg=fg_color, font=font)
    lbl2.place(x=50, y=80, width=150, height=30)
    txt2 = Entry(vent, bg="#fff")
    txt2.place(x=200, y=80, width=150, height=30)

    lbl3 = Label(vent, text="Resultado:", bg=bg_color, fg=fg_color, font=font)
    lbl3.place(x=50, y=130, width=150, height=30)
    txt3 = Entry(vent, bg="#FFF")
    txt3.place(x=200, y=130, width=150, height=30)

    # Historial
    history_listbox = Listbox(vent, width=50, height=10)
    history_listbox.place(x=400, y=30)

    # Botones para gestionar el historial
    delete_button = Button(vent, text="Eliminar", command=delete_history)
    delete_button.place(x=400, y=350, width=100, height=30)
    edit_button = Button(vent, text="Editar", command=edit_history)
    edit_button.place(x=520, y=350, width=100, height=30)

    main_btn =Button(vent, text="'Click' para cambiar el color", command=changeBG)
    main_btn.place(x=450, y=500)

    # Llamada a la función para crear el menú
    crear_menu(vent)

    return vent

vent = crear_ventana()
vent.mainloop()