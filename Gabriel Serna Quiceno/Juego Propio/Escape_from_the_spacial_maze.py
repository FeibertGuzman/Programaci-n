import random
import tkinter as tk
from tkinter import messagebox

class JuegoAdivinanza:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de Adivinanza de Palabras")

        self.palabras = ["salle", "programar", "desarrollador", "juego", "feibert"]
        self.palabra_secreta = random.choice(self.palabras)
        self.letras_adivinadas = set()
        self.intentos = 6

        self.label_palabra = tk.Label(master, text=self.mostrar_progreso(), font=("Helvetica", 24))
        self.label_palabra.pack(pady=20)

        self.entry_letra = tk.Entry(master, font=("Helvetica", 24))
        self.entry_letra.pack(pady=20)

        self.boton_adivinar = tk.Button(master, text="Adivinar letra", command=self.adivinar_letra, font=("Helvetica", 18))
        self.boton_adivinar.pack(pady=20)

        self.label_intentos = tk.Label(master, text=f"Te quedan {self.intentos} intentos", font=("Helvetica", 18))
        self.label_intentos.pack(pady=20)

    def mostrar_progreso(self):
        return ' '.join(letra if letra in self.letras_adivinadas else '_' for letra in self.palabra_secreta)

    def adivinar_letra(self):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if letra in self.letras_adivinadas:
            messagebox.showinfo("Info", "Ya has adivinado esa letra. Intenta otra vez.")
            return

        self.letras_adivinadas.add(letra)

        if letra in self.palabra_secreta:
            messagebox.showinfo("¡Bien hecho!", "La letra está en la palabra.")
        else:
            self.intentos -= 1
            messagebox.showinfo("Lo siento", "Esa letra no está en la palabra.")

        if all(letra in self.letras_adivinadas for letra in self.palabra_secreta):
            messagebox.showinfo("Felicidades tilín!!!", f"Has adivinado la palabra: {self.palabra_secreta}")
            self.master.quit()

        if self.intentos <= 0:
            messagebox.showinfo("Perdiste", f"La palabra era: {self.palabra_secreta}")
            self.master.quit()

        self.label_palabra.config(text=self.mostrar_progreso())
        self.label_intentos.config(text=f"Te quedan {self.intentos} intentos")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAdivinanza(root)
    root.mainloop()
