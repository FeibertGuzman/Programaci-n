import tkinter as tk
import random

class Culebrita:
    def __init__(self, master):
        self.master = master
        master.title("Juego de la Culebrita")

        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack()

        self.iniciar_juego()

        master.bind("<KeyPress>", self.cambiar_direccion)
        self.direccion = "Derecha"
        self.juego()

    def iniciar_juego(self):
        self.culebra = [(20, 20), (20, 30), (20, 40)]
        self.comida = self.generar_comida()
        self.puntuacion = 0

    def generar_comida(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.culebra:
                return (x, y)

    def cambiar_direccion(self, event):
        if event.keysym == 'Up' and self.direccion != "Abajo":
            self.direccion = "Arriba"
        elif event.keysym == 'Down' and self.direccion != "Arriba":
            self.direccion = "Abajo"
        elif event.keysym == 'Left' and self.direccion != "Derecha":
            self.direccion = "Izquierda"
        elif event.keysym == 'Right' and self.direccion != "Izquierda":
            self.direccion = "Derecha"

    def mover(self):
        cabeza_x, cabeza_y = self.culebra[0]
        
        if self.direccion == "Arriba":
            cabeza_y -= 10
        elif self.direccion == "Abajo":
            cabeza_y += 10
        elif self.direccion == "Izquierda":
            cabeza_x -= 10
        elif self.direccion == "Derecha":
            cabeza_x += 10

        nueva_cabeza = (cabeza_x, cabeza_y)

        # Verificar colisiones
        if (0 <= cabeza_x < 400 and 0 <= cabeza_y < 400) and (nueva_cabeza not in self.culebra):
            self.culebra.insert(0, nueva_cabeza)
            if nueva_cabeza == self.comida:
                self.puntuacion += 1
                self.comida = self.generar_comida()
            else:
                self.culebra.pop()
        else:
            self.perder()

    def perder(self):
        self.canvas.create_text(200, 200, text="¡Perdiste!", fill="red", font=("Arial", 24))
        self.master.after_cancel(self.juego_id)

    def dibujar(self):
        self.canvas.delete("all")
        for segmento in self.culebra:
            x, y = segmento
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")

        comida_x, comida_y = self.comida
        self.canvas.create_oval(comida_x, comida_y, comida_x + 10, comida_y + 10, fill="red")

        self.canvas.create_text(350, 10, text=f"Puntos: {self.puntuacion}", fill="white", font=("Arial", 10))

    def juego(self):
        self.mover()
        self.dibujar()
        self.juego_id = self.master.after(100, self.juego)

if __name__ == "__main__":
    root = tk.Tk()
    juego = Culebrita(root)
    root.mainloop()
