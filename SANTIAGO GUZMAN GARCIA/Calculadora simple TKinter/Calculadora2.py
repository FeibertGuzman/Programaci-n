#importar tkinder
from tkinter import Tk, Label, Button, Entry
import math

def crear_ventana():
    #configurar colores
    bg_color = "#F0F0F0"
    fg_color = "#333"
    font = ("Times_New_Roman", 12)
    fontNum = ("Times_New_Roman", 14)
    fontMain = ("Times_New_Roman", 16, "bold")
    ope = ""
    # Crear ventana principal

    vent = Tk() 
    vent.title("Calculadora simple")
    vent.geometry("800x800") #Dimensión de la ventana
    vent.configure(bg = bg_color)

    def fnSumar ():
        n1 =txt1.get()
        n2 =txt2.get()
        r = float(n1) + float(n2)
        txt3.delete(0, 'end') #Limpiar el resultado
        txt3.insert(0, r)
        ope = "+"
        lblope = Label(vent, text=ope, fg = fg_color, bg = bg_color, font = font)
        lblope.place(relx=0.3, rely=0.25, anchor='center', relwidth = 0.01, relheight=0.1)
    
    def fnResta():
        n1 = txt1.get()
        n2 = txt2.get()
        r = float(n1) - float(n2)
        txt3.delete(0, 'end') #Limpiar el resultado
        txt3.insert(0, r)
        ope = "-"
        lblope = Label(vent, text=ope, fg = fg_color, bg = bg_color, font = font)
        lblope.place(relx=0.3, rely=0.25, anchor='center', relwidth = 0.01, relheight=0.1)

    def fnMulti():
        n1 = txt1.get()
        n2 = txt2.get()
        r = float(n1) * float(n2)
        txt3.delete(0, 'end') #Limpiar el resultado
        txt3.insert(0, r)
        ope = "x"
        lblope = Label(vent, text=ope, fg = fg_color, bg = bg_color, font = font)
        lblope.place(relx=0.3, rely=0.25, anchor='center', relwidth = 0.01, relheight=0.1)

    def fnDivi():
        n1 = txt1.get()
        n2 = txt2.get()
        r = float(n1) / float(n2)
        txt3.delete(0, 'end') #Limpiar el resultado
        txt3.insert(0, r)
        ope = "/"
        lblope = Label(vent, text=ope, fg = fg_color, bg = bg_color, font = font)
        lblope.place(relx=0.3, rely=0.25, anchor='center', relwidth = 0.01, relheight=0.1)

    def fnValorA():
        r = txt3.get()
        r = float(r)  # Convertir el valor de txt3 a número

        if r < 0:
            r = abs(r)  # Obtener el valor absoluto

        txt3.delete(0, 'end')  # Limpiar el resultado
        txt3.insert(0, r)  # Insertar el nuevo resultado

        ope = "||"
        lblope = Label(vent, text=ope, fg=fg_color, bg=bg_color, font=font)
        lblope.place(relx=0.3, rely=0.25, anchor='center', relwidth=0.01, relheight=0.1)

    def fnMCM():
        n1 = txt1.get()
        n2 = txt2.get()
        
        a = int(n1)
        b = int(n2)

        mcm = abs(a * b) // math.gcd(a, b)

        txt3.delete(0, 'end')  # Limpiar el resultado
        txt3.insert(0, mcm)

        ope = "MCM"
        lblope = Label(vent, text=ope, fg=fg_color, bg=bg_color, font=font)
        lblope.place(relx=0.3, rely=0.25, anchor='center', relwidth=0.05, relheight=0.1)

    def fnMCD():
        n1 = txt1.get()
        n2 = txt2.get()
        
        a = int(n1)
        b = int(n2)

        mcd = math.gcd(a, b)

        txt3.delete(0, 'end')  # Limpiar el resultado
        txt3.insert(0, mcd)

        ope = "MCD"
        lblope = Label(vent, text=ope, fg=fg_color, bg=bg_color, font=font)
        lblope.place(relx=0.3, rely=0.25, anchor='center', relwidth=0.05, relheight=0.1)

    def fnSalir():
        vent.destroy()

    #Menú principal
    lbl0 = Label(vent, text="¡Bienvenido a la calculadora!", fg = "#FF0000", bg = bg_color, font = fontMain)
    lbl0.place(relx=0.5, rely=0.055, anchor='center', relwidth = 0.4, relheight=0.2)
    lblequal = Label(vent, text="=", fg = fg_color, bg = bg_color, font = font)
    lblequal.place(relx=0.5, rely=0.25, anchor='center', relwidth = 0.2, relheight=0.1)

    #Crear etiquetas PN
    lbl1 = Label(vent, text="Primer número", fg = fg_color, bg = bg_color, font = font)
    lbl1.place(relx=0.2, rely=0.15, anchor='center', relwidth = 0.2, relheight=0.1)
    txt1=Entry(vent, bg="#FFFFFF", justify='center', font = fontNum)
    txt1.place(relx=0.2, rely=0.25, anchor='center',relwidth=0.1, relheight=0.1)

    #Crear etiquetas SN
    lbl2 = Label(vent, text="Segundo número", fg = fg_color, bg = bg_color,font = font)
    lbl2.place(relx=0.4, rely=0.15, anchor='center', relwidth = 0.2, relheight=0.1)
    txt2=Entry(vent, bg="#FFFFFF", justify='center', font = fontNum)
    txt2.place(relx=0.4, rely=0.25, anchor='center',relwidth=0.1, relheight=0.1)

    #Crear etiquetas PN
    lbl3 = Label(vent, text="Resultado", fg = fg_color, bg = bg_color,font = font)
    lbl3.place(relx=0.7, rely=0.15, anchor='center', relwidth = 0.2, relheight=0.1)
    txt3=Entry(vent, bg="#FFFFFF", justify='center', font = fontNum)
    txt3.place(relx=0.7, rely=0.25, anchor='center',relwidth=0.3, relheight=0.1)

    #Boton suma
    btn1=Button(vent, text= 'Sumar', command=fnSumar, fg = fg_color, bg = "#9b9b9b",font = fontNum)
    btn1.place(relx=0.2, rely=0.5, anchor='center', relwidth= 0.2, relheight= 0.15)

    #Boton Resta
    btn2=Button(vent, text= 'Resta', command=fnResta, fg = fg_color, bg = "#9b9b9b",font = fontNum)
    btn2.place(relx=0.4, rely=0.5, anchor='center', relwidth= 0.2, relheight= 0.15)

    #Boton multi
    btn3=Button(vent, text= 'Multiplicar', command=fnMulti, fg = fg_color, bg = "#9b9b9b",font = fontNum)
    btn3.place(relx=0.6, rely=0.5, anchor='center', relwidth= 0.2, relheight= 0.15)

    #Boton divi
    btn4=Button(vent, text= 'Dividir', command=fnDivi, fg = fg_color, bg = "#9b9b9b",font = fontNum)
    btn4.place(relx=0.8, rely=0.5, anchor='center', relwidth= 0.2, relheight= 0.15)

    #Boton valor absoluto
    btn1=Button(vent, text= 'Valor absoluto', command=fnValorA, fg = fg_color, bg = "#9b9b9b",font = fontNum)
    btn1.place(relx=0.2, rely=0.7, anchor='center', relwidth= 0.2, relheight= 0.15)

    #Boton minimo comun multiplo
    btn2=Button(vent, text= 'MCM', command=fnMCM, fg = fg_color, bg = "#9b9b9b",font = fontNum)
    btn2.place(relx=0.4, rely=0.7, anchor='center', relwidth= 0.2, relheight= 0.15)

    #Boton maximo comun divisor
    btn3=Button(vent, text= 'MCD', command=fnMCD, fg = fg_color, bg = "#9b9b9b",font = fontNum)
    btn3.place(relx=0.6, rely=0.7, anchor='center', relwidth= 0.2, relheight= 0.15)

    #Bonton Salir
    btn5=Button(vent, text= "Salir", command=fnSalir, fg = fg_color, bg = "#9b9b9b", font = fontNum)
    btn5.place(relx=0.5, rely = 0.9, anchor='center', relwidth= 0.2, relheight = 0.15)

    return vent

#Crear ventana
vent = crear_ventana()

#Inicio bucle
vent.mainloop()