import tkinter as tk
import random

class JuegoPiedraPapel:
    def __init__(self, master):
        self.master = master
        self.master.title("Piedra, Papel o Tijera")
        
        # Establecer un tamaño mayor para la ventana
        self.master.geometry("400x300")
        
        # Deshabilitar el botón de maximizar
        self.master.resizable(False, False)

        self.opciones = ['piedra', 'papel', 'tijera']
        self.victorias_usuario = 0
        self.victorias_PC = 0

        self.instrucciones = tk.Label(master, text="Elige: Piedra, Papel o Tijera")
        self.instrucciones.pack(pady=10)

        self.boton_piedra = tk.Button(master, text="Piedra", command=lambda: self.jugar('piedra'))
        self.boton_piedra.pack(pady=5)

        self.boton_papel = tk.Button(master, text="Papel", command=lambda: self.jugar('papel'))
        self.boton_papel.pack(pady=5)

        self.boton_tijera = tk.Button(master, text="Tijera", command=lambda: self.jugar('tijera'))
        self.boton_tijera.pack(pady=5)

        self.resultado = tk.Label(master, text="")
        self.resultado.pack(pady=10)

        self.marcador = tk.Label(master, text="Marcador: Tú 0 - 0 PC")
        self.marcador.pack(pady=10)

        self.boton_reiniciar = tk.Button(master, text="Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.pack(pady=10)

    def jugar(self, usuario):
        PC = random.choice(self.opciones)
        resultado_texto = f"La PC eligió: {PC}\n"

        if usuario == PC:
            resultado_texto += "Empate"
        else:
            if usuario == 'piedra':
                if PC == 'tijera':
                    resultado_texto += "Ganaste: PIEDRA aplasta TIJERA."
                    self.victorias_usuario += 1
                else:
                    resultado_texto += "Perdiste: PAPEL envuelve PIEDRA."
                    self.victorias_PC += 1
            elif usuario == 'papel':
                if PC == 'piedra':
                    resultado_texto += "Ganaste: PAPEL envuelve PIEDRA."
                    self.victorias_usuario += 1
                else:
                    resultado_texto += "Perdiste: TIJERA corta PAPEL."
                    self.victorias_PC += 1
            elif usuario == 'tijera':
                if PC == 'papel':
                    resultado_texto += "Ganaste: TIJERA corta PAPEL."
                    self.victorias_usuario += 1
                else:
                    resultado_texto += "Perdiste: PIEDRA aplasta TIJERA."
                    self.victorias_PC += 1

        self.resultado.config(text=resultado_texto)
        self.marcador.config(text=f"Marcador: Tú {self.victorias_usuario} - {self.victorias_PC} PC")

        if self.victorias_usuario == 6:
            self.resultado.config(text="¡Felicidades! Has ganado el juego.")
            self.deshabilitar_botones()
        elif self.victorias_PC == 6:
            self.resultado.config(text="La PC ha ganado el juego. ¡Mejor suerte la próxima vez!")
            self.deshabilitar_botones()

    def deshabilitar_botones(self):
        self.boton_piedra.config(state='disabled')
        self.boton_papel.config(state='disabled')
        self.boton_tijera.config(state='disabled')

    def reiniciar(self):
        self.victorias_usuario = 0
        self.victorias_PC = 0
        self.resultado.config(text="")
        self.marcador.config(text="Marcador: Tú 0 - 0 PC")
        self.boton_piedra.config(state='normal')
        self.boton_papel.config(state='normal')
        self.boton_tijera.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoPiedraPapel(root)
    root.mainloop()
