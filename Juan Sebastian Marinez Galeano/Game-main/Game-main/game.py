import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Tres en Raya")

signo = 0
tablero = [[" " for _ in range(3)] for _ in range(3)]

botones = []
for i in range(3):
    fila = []
    for j in range(3):
        boton = tk.Button(ventana, text=" ", command=lambda i=i, j=j: obtener_texto(i, j, ventana, etiqueta1, etiqueta2), height=3, width=6)
        boton.grid(row=i, column=j)
        fila.append(boton)
    botones.append(fila)

etiqueta1 = tk.Label(ventana, text="Jugador 1: X", font=('Helvetica', 12))
etiqueta1.grid(row=3, column=0, columnspan=3)

etiqueta2 = tk.Label(ventana, text="Jugador 2: O", font=('Helvetica', 12))
etiqueta2.grid(row=4, column=0, columnspan=3)

def ganador(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))

def obtener_texto(i, j, gb, l1, l2):
    global signo
    if tablero[i][j] == " ":
        if signo % 2 == 0:
            tablero[i][j] = "X"
            botones[i][j].config(text="X")
            l1.config(text="Jugador 1: X (Tu turno)", fg="blue")
            l2.config(text="Jugador 2: O")
        else:
            tablero[i][j] = "O"
            botones[i][j].config(text="O")
            l1.config(text="Jugador 1: X")
            l2.config(text="Jugador 2: O (Tu turno)", fg="blue")
        signo += 1
        
        if ganador(tablero, "X"):
            messagebox.showinfo("Ganador", "Jugador 1 (X) ha ganado")
            gb.destroy()
        elif ganador(tablero, "O"):
            messagebox.showinfo("Ganador", "Jugador 2 (O) ha ganado")
            gb.destroy()
        elif lleno():
            messagebox.showinfo("Empate", "¡Es un empate!")
            gb.destroy()

def lleno():
    for fila in tablero:
        if " " in fila:
            return False
    return True

ventana.mainloop()
