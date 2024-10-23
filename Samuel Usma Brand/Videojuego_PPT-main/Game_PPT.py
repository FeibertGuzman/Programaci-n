import tkinter as tk
import random
from tkinter import messagebox


def jugar(usuario):
    opciones = ['piedra', 'papel', 'tijera']
    npc = random.choice(opciones)
    
    resultado = ""
    if usuario == npc:
        resultado = "Empate"
    else:
        if usuario == 'piedra':
            if npc == 'tijera':
                resultado = "¡Gana el usuario"
            else:
                resultado = "Gana la maquina"
        elif usuario == 'papel':
            if npc == 'piedra':
                resultado = "Gana el usuario"
            else:
                resultado = "Gana la maquina"
        elif usuario == 'tijera':
            if npc == 'papel':
                resultado = "Gana el usuario"
            else:
                resultado = "Gana la maquina"
    
    
    messagebox.showinfo("Resultado", f"NPC eligió: {npc}\n{resultado}")


def elegir(opcion):
    jugar(opcion)


ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("300x200")


boton_piedra = tk.Button(ventana, text="Piedra", command=lambda: elegir('piedra'))
boton_papel = tk.Button(ventana, text="Papel", command=lambda: elegir('papel'))
boton_tigera = tk.Button(ventana, text="Tijera", command=lambda: elegir('tijera'))


boton_piedra.pack(pady=10)
boton_papel.pack(pady=10)
boton_tigera.pack(pady=10)

boton_piedra.place(x=130, y=90)
boton_papel.place(x=200, y=90)
boton_tigera.place(x=70, y=90)

lbl= tk.Label(ventana, text="escoja una opcion para jugar", justify="center")
lbl.pack()
ventana.mainloop()