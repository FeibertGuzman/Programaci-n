import tkinter as tk
import random

class JuegoPiedraPapelTijera:
    def __init__(self, master):
        self.master = master
        master.title("Piedra, Papel o Tijera")

        self.puntuacion_usuario = 0
        self.puntuacion_computadora = 0
        self.juegos_jugados = 0

        self.label = tk.Label(master, text="Selecciona tu opción:")
        self.label.pack(pady=10)

        self.boton_piedra = tk.Button(master, text="Piedra", command=lambda: self.jugar("piedra"))
        self.boton_piedra.pack(side=tk.LEFT, padx=10)

        self.boton_papel = tk.Button(master, text="Papel", command=lambda: self.jugar("papel"))
        self.boton_papel.pack(side=tk.LEFT, padx=10)

        self.boton_tijera = tk.Button(master, text="Tijera", command=lambda: self.jugar("tijera"))
        self.boton_tijera.pack(side=tk.LEFT, padx=10)

        self.resultado_label = tk.Label(master, text="")
        self.resultado_label.pack(pady=20)

        self.puntuacion_label = tk.Label(master, text="Tu puntuación: 0 | Puntuación de la computadora: 0")
        self.puntuacion_label.pack(pady=10)

        self.mensaje_final = tk.Label(master, text="")
        self.mensaje_final.pack(pady=20)

    def jugar(self, eleccion_usuario):
        opciones = ["piedra", "papel", "tijera"]
        eleccion_computadora = random.choice(opciones)

        if eleccion_usuario == eleccion_computadora:
            resultado = "¡Es un empate!"
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            resultado = "¡Ganaste!"
            self.puntuacion_usuario += 1
        else:
            resultado = "Perdiste..."
            self.puntuacion_computadora += 1

        self.juegos_jugados += 1

        self.resultado_label.config(text=f"Tú elegiste: {eleccion_usuario}\nComputadora eligió: {eleccion_computadora}\n{resultado}")
        self.puntuacion_label.config(text=f"Tu puntuación: {self.puntuacion_usuario} | Puntuación de la computadora: {self.puntuacion_computadora}")

        if self.juegos_jugados >= 7:
            self.mostrar_ganador()

    def mostrar_ganador(self):
        if self.puntuacion_usuario > self.puntuacion_computadora:
            mensaje = "¡Felicidades! Ganaste el juego."
        elif self.puntuacion_usuario < self.puntuacion_computadora:
            mensaje = "Lo siento, la computadora ganó el juego."
        else:
            mensaje = "¡Es un empate total!"

        self.mensaje_final.config(text=mensaje)
        self.boton_piedra.config(state=tk.DISABLED)
        self.boton_papel.config(state=tk.DISABLED)
        self.boton_tijera.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoPiedraPapelTijera(root)
    root.mainloop()
