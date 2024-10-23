import tkinter as tk
import random

# Inicializar el conteo de victorias, empates y derrotas
victorias = 0
empates = 0
derrotas = 0

def jugar(opcion_usuario):
    global victorias, empates, derrotas

    # Opciones disponibles
    opciones = ["Piedra", "Papel", "Tijera"]
    opcion_maquina = random.choice(opciones)

    # Determinar el resultado
    if opcion_usuario == opcion_maquina:
        resultado = "Empate"
        empates += 1
    elif (opcion_usuario == "Piedra" and opcion_maquina == "Tijera") or \
         (opcion_usuario == "Papel" and opcion_maquina == "Piedra") or \
         (opcion_usuario == "Tijera" and opcion_maquina == "Papel"):
        resultado = "¡Ganaste!"
        victorias += 1
    else:
        resultado = "Perdiste"
        derrotas += 1

    # Actualizar la etiqueta de resultado
    resultado_label.config(text=f"Resultado: {resultado}\nMaquina eligió: {opcion_maquina}")
    # Actualizar los contadores en la interfaz
    actualizar_contadores()

    # Comprobar si se alcanzaron 10 victorias
    if victorias == 10:
        resultado_label.config(text="¡Has alcanzado 10 victorias! Fin del juego.")
        desactivar_botones()

def actualizar_contadores():
    victorias_label.config(text=f"Victorias: {victorias}")
    empates_label.config(text=f"Empates: {empates}")
    derrotas_label.config(text=f"Derrotas: {derrotas}")

def desactivar_botones():
    piedra_button.config(state=tk.DISABLED)
    papel_button.config(state=tk.DISABLED)
    tijera_button.config(state=tk.DISABLED)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("300x300")  # Establecer el tamaño fijo de la ventana

# Etiquetas para mostrar el resultado y contadores
resultado_label = tk.Label(ventana, text="Haz tu elección:", font=("Helvetica", 14))
resultado_label.pack(pady=10)

victorias_label = tk.Label(ventana, text="Victorias: 0", font=("Helvetica", 12))
victorias_label.pack()

empates_label = tk.Label(ventana, text="Empates: 0", font=("Helvetica", 12))
empates_label.pack()

derrotas_label = tk.Label(ventana, text="Derrotas: 0", font=("Helvetica", 12))
derrotas_label.pack()

# Botones para las opciones del usuario
piedra_button = tk.Button(ventana, text="Piedra", command=lambda: jugar("Piedra"), width=15)
piedra_button.pack(pady=5)

papel_button = tk.Button(ventana, text="Papel", command=lambda: jugar("Papel"), width=15)
papel_button.pack(pady=5)

tijera_button = tk.Button(ventana, text="Tijera", command=lambda: jugar("Tijera"), width=15)
tijera_button.pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()
