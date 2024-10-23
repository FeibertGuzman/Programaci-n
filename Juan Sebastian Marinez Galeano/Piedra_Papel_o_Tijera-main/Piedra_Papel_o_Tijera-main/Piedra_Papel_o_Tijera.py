import tkinter as tk
from tkinter import messagebox
import random

def jugar_10():
    opciones = ['piedra', 'papel', 'tijera']
    pc_point = 0
    usuario_point = 0
    ronda_actual = 0
    total_rondas = 10  # Jugar diez rondas

    def mostrar_resultado(usuario):
        nonlocal ronda_actual, pc_point, usuario_point

        if ronda_actual < total_rondas:
            ronda_actual += 1
            label_ronda.config(text=f"Ronda {ronda_actual} de {total_rondas}")

            pc = random.choice(opciones)
            label_pc.config(text=f"PC Eligió: {pc}")

            if usuario == pc:
                mensaje = "Es un Empate."
            else:
                if usuario == 'piedra':
                    if pc == 'tijera':
                        mensaje = "WINNER: piedra mata tijera."
                        usuario_point += 1
                    else:
                        mensaje = "GAMER OVER: papel envuelve piedra."
                        pc_point += 1
                elif usuario == 'papel':
                    if pc == 'piedra':
                        mensaje = "WINNER: papel envuelve piedra."
                        usuario_point += 1
                    else:
                        mensaje = "GAMER OVER: tijera mata papel."
                        pc_point += 1
                elif usuario == 'tijera':
                    if pc == 'papel':
                        mensaje = "WINNER: tijera mata papel."
                        usuario_point += 1
                    else:
                        mensaje = "GAMER OVER: piedra mata tijera."
                        pc_point += 1
                else:
                    mensaje = "Opción inválida. Intenta de nuevo."
                    ronda_actual -= 1  

            label_resultado.config(text=mensaje)
            label_puntos.config(text=f"Usuario: {usuario_point} | PC: {pc_point}")

            if ronda_actual == total_rondas:
                if usuario_point == pc_point:
                    final_mensaje = "¡Es un Empate!"
                elif usuario_point > pc_point:
                    final_mensaje = f"¡Usuario ganó con {usuario_point} puntos!"
                else:
                    final_mensaje = f"¡PC ganó con {pc_point} puntos!"

                messagebox.showinfo("Juego Terminado", final_mensaje)

                # Reiniciar el juego
                pc_point = 0
                usuario_point = 0
                ronda_actual = 0
                label_ronda.config(text=f"Ronda {ronda_actual} de {total_rondas}")
                label_puntos.config(text=f"Usuario: {usuario_point} | PC: {pc_point}")
                label_resultado.config(text="")
                label_pc.config(text="")

    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Piedra, Papel o Tijera")
    ventana.geometry("+500+80")

    label_ronda = tk.Label(ventana, text=f"Ronda {ronda_actual} de {total_rondas}", font=("Arial", 14))
    label_ronda.grid(row=0, column=0, columnspan=3)

    label_pc = tk.Label(ventana, text="", font=("Arial", 14))
    label_pc.grid(row=1, column=0, columnspan=3)

    label_resultado = tk.Label(ventana, text="", font=("Arial", 14))
    label_resultado.grid(row=2, column=0, columnspan=3)

    label_puntos = tk.Label(ventana, text=f"Usuario: {usuario_point} | PC: {pc_point}", font=("Arial", 14))
    label_puntos.grid(row=3, column=0, columnspan=3)

    # Crear botones para las opciones
    frame_botones = tk.Frame(ventana)
    frame_botones.grid(row=4, column=0, columnspan=3)

    for idx, opcion in enumerate(opciones):
        boton_opcion = tk.Button(frame_botones, text=opcion.capitalize(), command=lambda op=opcion: mostrar_resultado(op))
        boton_opcion.grid(row=0, column=idx, padx=10, pady=10)

    ventana.mainloop()

jugar_10()
