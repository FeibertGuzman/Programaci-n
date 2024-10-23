import tkinter as tk
import random

# Variables globales para victorias, derrotas, empates y partidas
victorias = 0
derrotas = 0
empates = 0
partidas = 10

# Función para actualizar la interfaz después de cada partida
def actualizar_resultado(resultado, pc_eleccion):
    global victorias, derrotas, empates, partidas

    label_pc.config(text=f"PC eligió: {pc_eleccion}")
    label_resultado.config(text=resultado)
    label_victorias.config(text=f"Victorias: {victorias}")
    label_derrotas.config(text=f"Derrotas: {derrotas}")
    label_empates.config(text=f"Empates: {empates}")
    label_partidas.config(text=f"Partidas restantes: {partidas}")

    if partidas == 0:
        if victorias > derrotas:
            label_resultado.config(text="¡Ganaste el juego!")
        elif derrotas > victorias:
            label_resultado.config(text="¡Perdiste el juego!")
        else:
            label_resultado.config(text="El juego terminó en empate.")
        boton_piedra.config(state="disabled")
        boton_papel.config(state="disabled")
        boton_tijera.config(state="disabled")

# Función para manejar la jugada del usuario
def jugar(usuario_eleccion):
    global victorias, derrotas, empates, partidas

    if partidas > 0:
        opciones = ['piedra', 'papel', 'tijera']
        pc_eleccion = random.choice(opciones)

        if usuario_eleccion == pc_eleccion:
            resultado = "Es un empate"
            empates += 1
        else:
            if usuario_eleccion == 'piedra':
                if pc_eleccion == 'tijera':
                    resultado = "Ganaste: piedra aplasta tijera."
                    victorias += 1
                else:
                    resultado = "Perdiste: papel envuelve piedra."
                    derrotas += 1
            elif usuario_eleccion == 'papel':
                if pc_eleccion == 'piedra':
                    resultado = "Ganaste: papel envuelve piedra."
                    victorias += 1
                else:
                    resultado = "Perdiste: tijera corta papel."
                    derrotas += 1
            elif usuario_eleccion == 'tijera':
                if pc_eleccion == 'papel':
                    resultado = "Ganaste: tijera corta papel."
                    victorias += 1
                else:
                    resultado = "Perdiste: piedra aplasta tijera."
                    derrotas += 1

        partidas -= 1
        actualizar_resultado(resultado, pc_eleccion)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Piedra, Papel o Tijera")

# Etiquetas para mostrar información
label_pc = tk.Label(root, text="PC eligió: ", font=("Arial", 12))
label_pc.pack()

label_resultado = tk.Label(root, text="Resultado", font=("Arial", 14))
label_resultado.pack()

label_victorias = tk.Label(root, text=f"Victorias: {victorias}", font=("Arial", 12))
label_victorias.pack()

label_derrotas = tk.Label(root, text=f"Derrotas: {derrotas}", font=("Arial", 12))
label_derrotas.pack()

label_empates = tk.Label(root, text=f"Empates: {empates}", font=("Arial", 12))
label_empates.pack()

label_partidas = tk.Label(root, text=f"Partidas restantes: {partidas}", font=("Arial", 12))
label_partidas.pack()

# Botones para seleccionar piedra, papel o tijera
boton_piedra = tk.Button(root, text="Piedra", command=lambda: jugar('piedra'), width=10, font=("Arial", 12))
boton_piedra.pack(pady=5)

boton_papel = tk.Button(root, text="Papel", command=lambda: jugar('papel'), width=10, font=("Arial", 12))
boton_papel.pack(pady=5)

boton_tijera = tk.Button(root, text="Tijera", command=lambda: jugar('tijera'), width=10, font=("Arial", 12))
boton_tijera.pack(pady=5)

# Iniciar el bucle principal de la interfaz
root.mainloop()