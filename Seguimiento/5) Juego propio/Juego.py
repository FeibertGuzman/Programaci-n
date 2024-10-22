import tkinter as tk
import random

class JuegoDeMemoria:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de Memoria")
        self.master.geometry("850x850")  # Tamaño de la ventana

        self.cartas = []
        self.botones = []
        self.pares_encontrados = 0
        self.primera_seleccion = None
        self.segunda_seleccion = None

        self.crear_cartas()
        self.crear_botones()

    def crear_cartas(self):
        # Crear pares de cartas
        imagenes = ["🐶", "🐱", "🐰", "🐻", "🐷", "🦊", "🐸", "🐵"]
        self.cartas = imagenes * 2  # Dos de cada uno
        random.shuffle(self.cartas)  # Mezclar las cartas

    def crear_botones(self):
        # Crear botones para cada carta
        for i in range(4):
            fila = []
            for j in range(4):
                boton = tk.Button(self.master, text="🃏", width=8, height=4, font=("Helvetica", 24),
                                  command=lambda x=i, y=j: self.seleccionar_carta(x, y))
                boton.grid(row=i, column=j, padx=10, pady=10)
                fila.append(boton)
            self.botones.append(fila)

    def seleccionar_carta(self, fila, columna):
        # Mostrar la carta seleccionada
        if self.botones[fila][columna]["text"] == "🃏":
            self.botones[fila][columna]["text"] = self.cartas[fila * 4 + columna]

            # Si es la primera selección
            if self.primera_seleccion is None:
                self.primera_seleccion = (fila, columna)
            else:
                self.segunda_seleccion = (fila, columna)
                self.master.after(1000, self.comparar_cartas)

    def comparar_cartas(self):
        # Comparar las cartas seleccionadas
        primera_fila, primera_columna = self.primera_seleccion
        segunda_fila, segunda_columna = self.segunda_seleccion

        if self.cartas[primera_fila * 4 + primera_columna] != self.cartas[segunda_fila * 4 + segunda_columna]:
            # Si no son iguales, volver a ocultar las cartas
            self.botones[primera_fila][primera_columna]["text"] = "🃏"
            self.botones[segunda_fila][segunda_columna]["text"] = "🃏"
        
        else:
            self.pares_encontrados += 1
        
        # Verificar si se han encontrado todos los pares
        if self.pares_encontrados == len(self.cartas) // 2:
            self.mostrar_mensaje_ganador()

        # Reiniciar las selecciones
        self.primera_seleccion = None
        self.segunda_seleccion = None

    def mostrar_mensaje_ganador(self):
        tk.messagebox.showinfo("¡Felicidades!", "¡Has ganado! Has encontrado todas las cartas.")
        # Reiniciar el juego
        self.reiniciar_juego()

    def reiniciar_juego(self):
        self.pares_encontrados = 0
        self.primera_seleccion = None
        self.segunda_seleccion = None
        self.crear_cartas()
        for fila in self.botones:
            for boton in fila:
                boton.config(text="🃏")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoDeMemoria(root)
    root.mainloop()
