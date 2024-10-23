from tkinter import *
from tkinter import ttk
import math
import subprocess


def ejecutar_otro_programa():
    programa = "Calculadora.py"  
    try:
        subprocess.run(["python", programa], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el programa: {e}")
        
def temaOscuro():
    estilos.configure('mainframe.TFrame', background="#010924")
    estilos_label1.configure('label1.TLabel', background="#010924", foreground="white")
    estilos_boton.configure('Botones_BORRAR.TButton', background="#00044A", foreground="white")
    estilos_boton.map('Botones_BORRAR.TButton', background=[('active', '#020A90')] )
        
def temaClaro():
    estilos.configure('mainframe.TFrame', background="#DBDBDB")
    estilos_label1.configure('label1.TLabel', background="#DBDBDB", foreground="black")
    
    estilos_boton.configure('Botones_BORRAR.TButton', background="#CECECE", foreground="black")
    estilos_boton.map('Botones_BORRAR.TButton', foreground=[("active", "#FF0000")], background=[("active", "#858585")]) 
    
def crear_menu(vent):
    barra_menu = Menu(vent)
    vent.config(menu=barra_menu)
    
    # Menú de Inicio
    menu_inicio = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Salir", command=vent.destroy)

    # Menú de Tema
    menu_tema = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Tema", menu=menu_tema)
    menu_tema.add_command(label="Tema Claro", command=temaClaro)
    menu_tema.add_command(label="Tema Oscuro", command=temaOscuro)
    
    # Menú de Calculadora
    menu_calculadora2 = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Calculadora", menu=menu_calculadora2)
    menu_calculadora2.add_command(label="Calculadora", command=ejecutar_otro_programa)    
    
def formato_resultado(r):
    return int(r) if r % 1 == 0 else r

def factorial():
    n1 = txt1.get()
    try:
        r = math.factorial(int(n1))
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

def salir():
    ventana.destroy()
      
ventana = Tk()
ventana.title("Calculadora simple")
ventana.geometry("+500+80")
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Estilos
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(ventana, style="mainframe.TFrame")
mainframe.grid(row=0, column=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)


# Estilos label
estilos_label1 = ttk.Style()
estilos_label1.configure('label1.TLabel', font="arial 15", anchor="e")



# Entrada

label_entry1 = ttk.Label(mainframe, text="Numero 1", style="label1.TLabel")
label_entry1.grid(row=0, column=0)

txt1 = Entry(mainframe, bg="#fff")
txt1.grid(row=0, column=1, columnspan=4, sticky=(W,E))

label_entry2 = ttk.Label(mainframe, text="Numero 2", style="label1.TLabel")
label_entry2.grid(row=1, column=0)

txt2 = Entry(mainframe, bg="#fff")
txt2.grid(row=1, column=1, columnspan=4, sticky=(W,E))

label_entry3 = ttk.Label(mainframe, text="Resultado", style="label1.TLabel")
label_entry3.grid(row=2, column=0, sticky=(W,E))

txt3 = Entry(mainframe, bg="#fff")
txt3.grid(row=2, column=2, columnspan=4, sticky=(W,E))



estilos_boton = ttk.Style()
estilos_boton.configure('Botones_BORRAR.TButton', font="arial22", width=5, background="#CECECE", relief="flat")



buttonMCM = ttk.Button(mainframe, text="MCM", style="Botones_BORRAR.TButton", command=mcm)
buttonMCD = ttk.Button(mainframe, text="MCD", style="Botones_BORRAR.TButton", command=mcm)
buttonABS = ttk.Button(mainframe, text="ABS", style="Botones_BORRAR.TButton", command=valor_absoluto)
buttonFACT = ttk.Button(mainframe, text="!", style="Botones_BORRAR.TButton", command=factorial)

buttonMCM.grid(row=3, column=0, columnspan=2, sticky=(W, N, E, S))
buttonMCD.grid(row=3, column=2, columnspan=2, sticky=(W, N, E, S))
buttonABS.grid(row=4, column=0, columnspan=2, sticky=(W, N, E, S))
buttonFACT.grid(row=4, column=2, columnspan=2, sticky=(W, N, E, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)
    
crear_menu(ventana)

ventana.mainloop()