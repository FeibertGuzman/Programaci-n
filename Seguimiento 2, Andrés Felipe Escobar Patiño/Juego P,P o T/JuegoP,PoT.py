import tkinter as tk
import random

# Opciones posibles
opciones = ["Piedra", "Papel", "Tijera"]

# Variables globales para los contadores
puntos_usuario = 0
puntos_pc = 0

# Función para jugar una ronda
def jugar(eleccion_usuario):
    global puntos_usuario, puntos_pc

    eleccion_pc = random.choice(opciones)

    if eleccion_usuario == eleccion_pc:
        resultado.set(f"Empate. Ambos eligieron {eleccion_usuario}.")
    elif (eleccion_usuario == "Piedra" and eleccion_pc == "Tijera") or \
         (eleccion_usuario == "Papel" and eleccion_pc == "Piedra") or \
         (eleccion_usuario == "Tijera" and eleccion_pc == "Papel"):
        puntos_usuario += 1
        resultado.set(f"¡Ganaste! {eleccion_usuario} vence a {eleccion_pc}.")
    else:
        puntos_pc += 1
        resultado.set(f"Perdiste. {eleccion_pc} vence a {eleccion_usuario}.")

    # Actualizar el marcador
    marcador.set(f"Tú: {puntos_usuario} | PC: {puntos_pc}")

    # Verificar si alguien ha ganado la partida al mejor de 11
    if puntos_usuario == 6:
        resultado.set("¡Felicidades! Ganaste la partida.")
        desactivar_botones()
    elif puntos_pc == 6:
        resultado.set("Perdiste la partida. ¡Intenta de nuevo!")
        desactivar_botones()

# Función para desactivar los botones al terminar la partida
def desactivar_botones():
    for boton in botones:
        boton.config(state=tk.DISABLED)

# Función para reiniciar el juego
def reiniciar():
    global puntos_usuario, puntos_pc
    puntos_usuario = 0
    puntos_pc = 0
    resultado.set("")
    marcador.set("Tú: 0 | PC: 0")
    for boton in botones:
        boton.config(state=tk.NORMAL)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera - Mejor de 11")
ventana.geometry("400x350")

# Variables para mostrar el resultado y el marcador
resultado = tk.StringVar()
marcador = tk.StringVar(value="Tú: 0 | PC: 0")

# Etiqueta de bienvenida
tk.Label(ventana, text="Elige tu opción:", font=("Arial", 16)).pack(pady=10)

# Crear y colocar los botones de opciones
botones = []
for opcion in opciones:
    boton = tk.Button(ventana, text=opcion, font=("Arial", 14), width=10,
                      command=lambda opt=opcion: jugar(opt))
    boton.pack(pady=5)
    botones.append(boton)

# Mostrar el marcador
tk.Label(ventana, textvariable=marcador, font=("Arial", 14)).pack(pady=10)

# Etiqueta para mostrar el resultado
tk.Label(ventana, textvariable=resultado, font=("Arial", 14), wraplength=300).pack(pady=20)

# Botón para reiniciar el juego
tk.Button(ventana, text="Reiniciar", font=("Arial", 12), command=reiniciar).pack(pady=10)

# Bucle principal de la aplicación
ventana.mainloop()