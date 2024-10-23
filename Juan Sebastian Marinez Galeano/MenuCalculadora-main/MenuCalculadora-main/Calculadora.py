from tkinter import *
from tkinter import ttk
import math
import subprocess

def ejecutar_otro_programa():
    programa = "Calculadora_simple.py"  
    try:
        subprocess.run(["python", programa], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el programa: {e}")

def temaOscuro():
    estilos.configure('mainframe.TFrame', background="#010924")
    estilos_label1.configure('label1.TLabel', background="#010924", foreground="white")
    estilos_label2.configure('label2.TLabel', background="#010924", foreground="white")
    
    estilos_numero.configure('Botones_numero.TButton', background="#00044A", foreground="white")
    estilos_numero.map('Botones_numero.TButton', background=[('active', '#020A90')] )
    
    estilos_otros.configure('Botones_OTROS.TButton', background="#010924", foreground="white")
    estilos_otros.map('Botones_OTROS.TButton', background=[('active', '#000AB1')] )

    estilos_borrar.configure('Botones_BORRAR.TButton', background="#010924", foreground="white")
    estilos_borrar.map('Botones_BORRAR.TButton', background=[('active', '#000AB1')] )

def temaClaro():
    estilos.configure('mainframe.TFrame', background="#DBDBDB")
    estilos_label1.configure('label1.TLabel', background="#DBDBDB", foreground="black")
    estilos_label2.configure('label2.TLabel', background="#DBDBDB", foreground="black")
    
    estilos_numero.configure('Botones_numero.TButton', background="#FFFFFF", foreground="black")
    estilos_numero.map('Botones_numero.TButton', background=[("active", "#B9B9B9")])
    
    estilos_otros.configure('Botones_OTROS.TButton', background="#CECECE", foreground="black")
    estilos_otros.map('Botones_OTROS.TButton', background=[("active", "#B9B9B9")])
    
    estilos_borrar.configure('Botones_BORRAR.TButton', background="#CECECE", foreground="black")
    estilos_borrar.map('Botones_BORRAR.TButton', foreground=[("active", "#FF0000")], background=[("active", "#858585")])

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
    menu_calculadora2.add_command(label="Calculadora Simple", command=ejecutar_otro_programa)

def ingresar_valores(tecla):
    if tecla  >= '0' and tecla <= '9' or tecla =='(' or tecla == ')' or tecla == '.':
        entry2.set(entry2.get()+tecla)
    
  
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entry1.set(entry2.get() )
        elif tecla == '/':
            entry1.set(entry2.get() + '/')
        elif tecla == '+':
            entry1.set(entry2.get() + '+')
        elif tecla == '-':
            entry1.set(entry2.get() + '-')
            
        entry2.set('')

    
    if tecla == '=':
      entry1.set(entry1.get() + entry2.get())
      resultado = eval(entry1.get())  
      entry2.set(resultado)      
  
def ingresar_valores_teclado(event):
    tecla = event.char
    
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entry2.set(entry2.get() + tecla)
    
    elif tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entry1.set(entry2.get() + '*')
        elif tecla == '/':
            entry1.set(entry2.get() + '/')
        elif tecla == '+':
            entry1.set(entry2.get() + '+')
        elif tecla == '-':
            entry1.set(entry2.get() + '-')
        entry2.set('')
    
    elif tecla == '=':
        entry1.set(entry1.get() + entry2.get())
        resultado = eval(entry1.get())
        entry2.set(resultado)
     
def raizCuadrada():
  entry1.set('')
  resultado =  math.sqrt(float(entry2.get()))
  entry2.set(resultado)
  
def borrar(*args):
  inicio = 0
  final = len(entry2.get())
  
  entry2.set(entry2.get()[inicio:final-1])

def borrar_todo(*args):
  entry1.set('')
  entry2.set('')

    
        
ventana = Tk()
ventana.title("Calculadora")
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
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

# Estilos label
estilos_label1 = ttk.Style()
estilos_label1.configure('label1.TLabel', font="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('label2.TLabel', font="arial 40", anchor="e")

# Entrada
entry1 = StringVar()
label_entry1 = ttk.Label(mainframe, textvariable=entry1, style="label1.TLabel")
label_entry1.grid(row=0, column=0, columnspan=4, sticky=(W, N, E, S))

entry2 = StringVar()
label_entry2 = ttk.Label(mainframe, textvariable=entry2, style="label2.TLabel")
label_entry2.grid(row=1, column=0, columnspan=4, sticky=(W, N, E, S))

# Estilos botones
estilos_numero = ttk.Style()
estilos_numero.configure('Botones_numero.TButton', font="arial22", width=5, background="#FFFFFF", relief="flat")


estilos_borrar = ttk.Style()
estilos_borrar.configure('Botones_BORRAR.TButton', font="arial22", width=5, background="#CECECE", relief="flat")

estilos_otros = ttk.Style()
estilos_otros.configure('Botones_OTROS.TButton', font="arial22", width=5, background="#CECECE", relief="flat")

# Crear botones

button0 = ttk.Button(mainframe, text="0", style="Botones_numero.TButton", command=lambda: ingresar_valores('0'))
button1 = ttk.Button(mainframe, text="1", style="Botones_numero.TButton", command=lambda: ingresar_valores('1'))
button2 = ttk.Button(mainframe, text="2", style="Botones_numero.TButton", command=lambda: ingresar_valores('2'))
button3 = ttk.Button(mainframe, text="3", style="Botones_numero.TButton", command=lambda: ingresar_valores('3'))
button4 = ttk.Button(mainframe, text="4", style="Botones_numero.TButton", command=lambda: ingresar_valores('4'))
button5 = ttk.Button(mainframe, text="5", style="Botones_numero.TButton", command=lambda: ingresar_valores('5'))
button6 = ttk.Button(mainframe, text="6", style="Botones_numero.TButton", command=lambda: ingresar_valores('6'))
button7 = ttk.Button(mainframe, text="7", style="Botones_numero.TButton", command=lambda: ingresar_valores('7'))
button8 = ttk.Button(mainframe, text="8", style="Botones_numero.TButton", command=lambda: ingresar_valores('8'))
button9 = ttk.Button(mainframe, text="9", style="Botones_numero.TButton", command=lambda: ingresar_valores('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_BORRAR.TButton", command=lambda: borrar())  # Botón para borrar un carácter
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_BORRAR.TButton", command=lambda: borrar_todo())  # Botón para borrar todo

button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_OTROS.TButton", command=lambda: ingresar_valores('('))  # Paréntesis de apertura
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_OTROS.TButton", command=lambda: ingresar_valores(')'))  # Paréntesis de cierre
button_punto = ttk.Button(mainframe, text=".", style="Botones_OTROS.TButton", command=lambda: ingresar_valores('.'))  # Punto decimal

button_division = ttk.Button(mainframe, text=chr(247), style="Botones_OTROS.TButton", command=lambda: ingresar_valores('/'))  # Botón para división
button_multiplicacion = ttk.Button(mainframe, text="x", style="Botones_OTROS.TButton", command=lambda: ingresar_valores('*'))  # Botón para multiplicación
button_suma = ttk.Button(mainframe, text="+", style="Botones_OTROS.TButton", command=lambda: ingresar_valores('+'))  # Botón para suma
button_resta = ttk.Button(mainframe, text="-", style="Botones_OTROS.TButton", command=lambda: ingresar_valores('-'))  # Botón para resta

button_radicacion = ttk.Button(mainframe, text="√", style="Botones_OTROS.TButton", command=lambda: raizCuadrada())  # Botón para radicación
button_igual = ttk.Button(mainframe, text="=", style="Botones_OTROS.TButton", command=lambda: ingresar_valores('='))  # Botón para igual

# Colocar botones en pantalla
button_parentesis1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parentesis2.grid(column=1, row=2, sticky=(W, N, E, S))
button_borrar_todo.grid(column=2, row=2, sticky=(W, N, E, S))
button_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_division.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_suma.grid(column=3, row=5, sticky=(W, N, E, S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
button_resta.grid(column=3, row=6, sticky=(W, N, E, S))  # Posición del botón de resta

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))  # Posición del botón igual
button_radicacion.grid(column=3, row=7, sticky=(W, N, E, S))  # Posición del botón de radicación

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

# Crear el menú en cascada
crear_menu(ventana)
ventana.bind('<Key>', ingresar_valores_teclado)
ventana.bind('<KeyPress-b>', borrar)
ventana.bind('<KeyPress-q>', borrar_todo)
ventana.mainloop()
ejecutar_otro_programa()
