import tkinter as tk
from tkinter import messagebox
import random

class AdivinaElNumero:
    def __init__(self, master):
        self.master = master
        master.title("Adivina el Número 🎉")

        self.intentos = 0
        self.numero_secreto = random.randint(1, 100)
        self.max_intentos = 10  # Máximo de intentos permitidos

        self.label = tk.Label(master, text="Adivina un número entre 1 y 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.adivinar_button = tk.Button(master, text="Adivinar", command=self.adivinar)
        self.adivinar_button.pack()

        self.reset_button = tk.Button(master, text="Reiniciar Juego", command=self.resetear)
        self.reset_button.pack()

        self.resultado_label = tk.Label(master, text="")
        self.resultado_label.pack()

        self.intentos_label = tk.Label(master, text=f"Te quedan {self.max_intentos} intentos.")
        self.intentos_label.pack()

        # Mensajes burlones con emojis
        self.burlas = [
            "¿Estás seguro de que eres humano? 🤖",
            "Ese número está más lejos que la luna. 🌕",
            "Intenta de nuevo, ¡pero esta vez usa tu cerebro! 🧠",
            "¡Casi! Solo te falta un océano de distancia. 🌊",
            "No te preocupes, a todos nos pasa... a veces. 😅",
            "¡Sigue intentándolo! El premio consuelo es un 'bien hecho'. 🏆",
            "¿Tienes el mapa del tesoro? Porque eso está muy lejos. 🗺️",
            "Vaya, parece que la suerte no está de tu lado hoy. 🍀",
            "¡Lo intentaste, y eso es lo que importa! O eso dicen... 🤷‍♂️",
        ]

    def adivinar(self):
        """Comprueba la adivinanza del jugador."""
        try:
            adivinanza = int(self.entry.get())
            self.intentos += 1
            
            if adivinanza < 1 or adivinanza > 100:
                raise ValueError("Fuera de rango")
            
            # Actualiza los intentos restantes
            intentos_restantes = self.max_intentos - self.intentos
            
            if adivinanza < self.numero_secreto:
                self.resultado_label.config(text=random.choice(self.burlas) + " El número es más alto. ⬆️")
            elif adivinanza > self.numero_secreto:
                self.resultado_label.config(text=random.choice(self.burlas) + " El número es más bajo. ⬇️")
            else:
                messagebox.showinfo("¡Felicidades! 🎉", f"¡Adivinaste el número {self.numero_secreto} en {self.intentos} intentos! 🥳")
                self.resetear()
                return
            
            # Actualiza la etiqueta de intentos restantes
            if intentos_restantes > 0:
                self.intentos_label.config(text=f"Te quedan {intentos_restantes} intentos.")
            else:
                messagebox.showinfo("¡Fin del Juego! 😢", f"No lograste adivinar el número {self.numero_secreto}.")
                self.resetear()
                
        except ValueError:
            messagebox.showwarning("Entrada inválida ⚠️", "Por favor, ingresa un número entre 1 y 100.")

    def resetear(self):
        """Reinicia el juego."""
        self.intentos = 0
        self.numero_secreto = random.randint(1, 100)
        self.resultado_label.config(text="")
        self.intentos_label.config(text=f"Te quedan {self.max_intentos} intentos.")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    juego = AdivinaElNumero(root)
    root.mainloop()