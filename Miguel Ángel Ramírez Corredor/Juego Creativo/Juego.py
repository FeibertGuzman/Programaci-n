import tkinter as tk
import random

# Crear una clase para el juego
class JuegoMemoria:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego de Memoria: Unir Pares")
        self.master.geometry("400x450")  # Establecer un tamaño fijo para la ventana
        
        # Lista de colores y su repetición para pares
        self.colores = ["red", "green", "blue", "yellow", "orange", "purple", "cyan", "magenta"]
        self.colores = self.colores * 2  # Crear pares
        random.shuffle(self.colores)  # Mezclar colores

        # Inicializar variables
        self.botones = []
        self.primera_seleccion = None
        self.segunda_seleccion = None
        self.parejas_encontradas = 0
        
        # Crear botones
        for i in range(4):
            fila = []
            for j in range(4):
                boton = tk.Button(master, text="", width=10, height=5,
                                  command=lambda i=i, j=j: self.seleccionar(i, j))
                boton.grid(row=i, column=j, padx=5, pady=5)  # Agregar separación entre botones
                fila.append(boton)
            self.botones.append(fila)

        # Etiqueta para mostrar mensajes
        self.mensaje_label = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.mensaje_label.grid(row=4, column=0, columnspan=4)  # Centrar mensaje debajo de los botones

    def seleccionar(self, i, j):
        # Mostrar color al seleccionar
        boton = self.botones[i][j]
        if boton['text'] == "" and self.primera_seleccion is None:
            boton.config(bg=self.colores[i * 4 + j], text=self.colores[i * 4 + j])
            self.primera_seleccion = (i, j)

        elif boton['text'] == "" and self.segunda_seleccion is None:
            boton.config(bg=self.colores[i * 4 + j], text=self.colores[i * 4 + j])
            self.segunda_seleccion = (i, j)
            self.master.after(500, self.verificar_pareja)  # Verificar después de 500ms

    def verificar_pareja(self):
        i1, j1 = self.primera_seleccion
        i2, j2 = self.segunda_seleccion
        if self.colores[i1 * 4 + j1] == self.colores[i2 * 4 + j2]:
            # Si son iguales, mantener los colores
            self.parejas_encontradas += 1
            if self.parejas_encontradas == len(self.colores) // 2:
                self.mostrar_mensaje("¡Has encontrado todos los pares!")
        else:
            # Si no son iguales, ocultar los colores
            self.botones[i1][j1].config(bg="SystemButtonFace", text="")
            self.botones[i2][j2].config(bg="SystemButtonFace", text="")
        
        # Reiniciar selecciones
        self.primera_seleccion = None
        self.segunda_seleccion = None

    def mostrar_mensaje(self, mensaje):
        for boton_fila in self.botones:
            for boton in boton_fila:
                boton.config(state=tk.DISABLED)  # Deshabilitar todos los botones
        self.mensaje_label.config(text=mensaje)  # Mostrar el mensaje en la etiqueta

# Crear la ventana principal
ventana = tk.Tk()
juego = JuegoMemoria(ventana)

# Ejecutar la ventana
ventana.mainloop()
