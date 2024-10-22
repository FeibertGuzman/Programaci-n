import tkinter as tk
import random

# Variables globales
ganadas = 0
perdidas = 0
empates = 0

# Función para jugar una ronda
def jugar(usuario):
    global ganadas, perdidas, empates
    opciones = ['piedra', 'papel', 'tigera']
    npc = random.choice(opciones)
    
    resultado_text = f"El NPC eligió {npc}. "
    
    if usuario == npc:
        resultado_text += "Empate crack"
        empates += 1
    else:
        if usuario == 'piedra':
            if npc == 'tigera':
                resultado_text += "Tu piedrota se la metió doblada a las tigeras de NPC. ¡Ganaste!"
                ganadas += 1
            else:
                resultado_text += "La piedra de NPC te aplastó noob. ¡Perdiste!"
                perdidas += 1
        elif usuario == 'papel':
            if npc == 'piedra':
                resultado_text += "Tu papel envolvió la piedra fea de NPC. ¡Ganaste!"
                ganadas += 1
            else:
                resultado_text += "Te envolvieron hasta la ch**ba. ¡Perdiste!"
                perdidas += 1
        elif usuario == 'tigera':
            if npc == 'papel':
                resultado_text += "Tus tigeras cortaron el papel de NPC. ¡Ganaste!"
                ganadas += 1
            else:
                resultado_text += "La piedra de NPC te aplastó. ¡Perdiste!"
                perdidas += 1
    
    # Actualizar la etiqueta de resultado
    resultado_label.config(text=resultado_text)
    
    # Actualizar las estadísticas
    actualizar_estadisticas()

# Función para actualizar las estadísticas
def actualizar_estadisticas():
    estadisticas_label.config(text=f"Ganadas: {ganadas}  |  Perdidas: {perdidas}  |  Empates: {empates}")

# Función para salir del juego
def salir():
    ventana.quit()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tigera")
ventana.geometry("400x350")

# Etiqueta de instrucciones
instrucciones_label = tk.Label(ventana, text="Elige: piedra, papel o tigera", font=("Arial", 14))
instrucciones_label.pack(pady=10)

# Botones de opciones
boton_piedra = tk.Button(ventana, text="Piedra", width=10, font=("Arial", 12), command=lambda: jugar('piedra'))
boton_piedra.pack(pady=5)

boton_papel = tk.Button(ventana, text="Papel", width=10, font=("Arial", 12), command=lambda: jugar('papel'))
boton_papel.pack(pady=5)

boton_tigera = tk.Button(ventana, text="Tigera", width=10, font=("Arial", 12), command=lambda: jugar('tigera'))
boton_tigera.pack(pady=5)

# Etiqueta para mostrar el resultado del juego
resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

# Etiqueta para mostrar las estadísticas
estadisticas_label = tk.Label(ventana, text="Ganadas: 0  |  Perdidas: 0  |  Empates: 0", font=("Arial", 12))
estadisticas_label.pack(pady=10)

# Botón para salir
boton_salir = tk.Button(ventana, text="Salir", width=10, font=("Arial", 12), command=salir)
boton_salir.pack(pady=20)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()