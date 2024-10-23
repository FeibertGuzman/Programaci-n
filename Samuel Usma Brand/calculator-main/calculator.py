from tkinter import *
import math

def crear_ventana():
    bg_color = "#d42bf0"
    fg_color = "#333"
    font = ("Arial", 12)
    vent = Tk()
    vent.title("Calculadora Simple")
    vent.geometry("750x400")
    vent.configure(bg=bg_color)
    def formato_resultado(r):
        return int(r) if r % 1 == 0 else r
    def suma():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = float(n1) + float(n2)
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def resta():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = float(n1) - float(n2)
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def multiplicacion():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = float(n1) * float(n2)
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def division():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = float(n1) / float(n2)
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
        except ZeroDivisionError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def valor_absoluto():
        n1 = txt1.get()
        try:
            r = abs(float(n1))
            r = formato_resultado(r)
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def mcm():
        def calcular_mcm(a, b):
            return abs(a * b) // math.gcd(a, b)

        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = calcular_mcm(int(n1), int(n2))
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def mcd():
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            r = math.gcd(int(n1), int(n2))
            txt3.delete(0, 'end')
            txt3.insert(0, r)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
    def salir():
        vent.destroy()
    lbl1 = Label(vent, text="Número 1:", bg=bg_color, fg=fg_color, font=font)
    lbl1.place(relx=0.2, rely=0.1, anchor='center', relwidth=0.3, relheight=0.1)
    txt1 = Entry(vent, bg="#fff")
    txt1.place(relx=0.6, rely=0.1, anchor="center", relwidth=0.3, relheight=0.1)
    
    lbl2 = Label(vent, text="Número 2:", bg=bg_color, fg=fg_color, font=font)
    lbl2.place(relx=0.2, rely=0.3, anchor='center', relwidth=0.3, relheight=0.1)
    txt2 = Entry(vent, bg="#fff")
    txt2.place(relx=0.6, rely=0.3, anchor="center", relwidth=0.3, relheight=0.1)

    lbl3 = Label(vent, text="Resultado:", bg=bg_color, fg=fg_color, font=font)
    lbl3.place(relx=0.2, rely=0.5, anchor='center', relwidth=0.3, relheight=0.1)
    txt3 = Entry(vent, bg="#FFF")
    txt3.place(relx=0.6, rely=0.5, anchor="center", relwidth=0.3, relheight=0.1)
    btn_suma = Button(vent, text="Sumar", command=suma, bg="#d3d3d3")
    btn_suma.place(x=50, y=300, width=150, height=30)
    
    btn_resta = Button(vent, text="Restar", command=resta, bg="#d3d3d3")
    btn_resta.place(x=220, y=300, width=150, height=30)
    
    btn_multiplicacion = Button(vent, text="Multiplicación", command=multiplicacion, bg="#d3d3d3")
    btn_multiplicacion.place(x=50, y=350, width=150, height=30)

    btn_division = Button(vent, text="División", command=division, bg="#d3d3d3")
    btn_division.place(x=220, y=350, width=150, height=30)

    btn_valor_absoluto = Button(vent, text="Valor Absoluto", command=valor_absoluto, bg="#d3d3d3")
    btn_valor_absoluto.place(x=560, y=300, width=150, height=30)
    
    btn_mcm = Button(vent, text="MCM", command=mcm, bg="#d3d3d3")
    btn_mcm.place(x=390, y=300, width=150, height=30)
    
    btn_mcd = Button(vent, text="MCD", command=mcd, bg="#d3d3d3")
    btn_mcd.place(x=560, y=350, width=150, height=30)

    btn_salir = Button(vent, text="Salir", command=salir, bg="#ff7f7f")
    btn_salir.place(x=390, y=350, width=150, height=30)

    return vent

vent = crear_ventana()
vent.mainloop()