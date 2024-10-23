import tkinter as tk
import random

# Función para determinar el resultado
def determinar_ganador(eleccion_jugador):
    eleccion_maquina = random.choice(["Piedra", "Papel", "Tijera"])
    if eleccion_jugador == eleccion_maquina:
        resultado.set(f"Empate. Ambos eligieron {eleccion_jugador}.")
    elif (eleccion_jugador == "Piedra" and eleccion_maquina == "Tijera") or \
         (eleccion_jugador == "Papel" and eleccion_maquina == "Piedra") or \
         (eleccion_jugador == "Tijera" and eleccion_maquina == "Papel"):
        resultado.set(f"Ganaste. Tú elegiste {eleccion_jugador} y la máquina eligió {eleccion_maquina}.")
    else:
        resultado.set(f"Perdiste. Tú elegiste {eleccion_jugador} y la máquina eligió {eleccion_maquina}.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")

# Ajustar tamaño de la ventana
ventana.geometry("400x400")  # Aumentar tamaño de la ventana

# Centrar la ventana en la pantalla
ancho_ventana = 400
alto_ventana = 400
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Variable para mostrar el resultado
resultado = tk.StringVar()

# Crear widgets
instrucciones = tk.Label(ventana, text="Elige tu opción:", font=("Helvetica", 14))
instrucciones.pack(pady=10)

# Crear botones más grandes con una fuente y tamaño de botón personalizados
boton_piedra = tk.Button(ventana, text="Piedra", font=("Helvetica", 16), width=10, height=2, command=lambda: determinar_ganador("Piedra"))
boton_piedra.pack(pady=10)

boton_papel = tk.Button(ventana, text="Papel", font=("Helvetica", 16), width=10, height=2, command=lambda: determinar_ganador("Papel"))
boton_papel.pack(pady=10)

boton_tijera = tk.Button(ventana, text="Tijera", font=("Helvetica", 16), width=10, height=2, command=lambda: determinar_ganador("Tijera"))
boton_tijera.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12))
etiqueta_resultado.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
