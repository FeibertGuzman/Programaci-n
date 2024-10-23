import tkinter as tk
import random

# Variables globales para el número a adivinar y los intentos restantes
numero_a_adivinar = random.randint(1, 100)
intentos = 10

# Función para actualizar la interfaz después de cada intento
def actualizar_resultado(resultado):
    global intentos

    label_resultado.config(text=resultado)
    label_intentos.config(text=f"Intentos restantes: {intentos}")

    if intentos == 0:
        label_resultado.config(text="¡Perdiste! El número era " + str(numero_a_adivinar))
        entrada_numero.config(state="disabled")
        boton_adivinar.config(state="disabled")

# Función para manejar la adivinanza del usuario
def adivinar():
    global intentos
    if intentos > 0:
        try:
            adivinanza = int(entrada_numero.get())
            if adivinanza < 1 or adivinanza > 100:
                resultado = "Por favor, ingresa un número entre 1 y 100."
            else:
                if adivinanza < numero_a_adivinar:
                    resultado = "Demasiado bajo."
                elif adivinanza > numero_a_adivinar:
                    resultado = "Demasiado alto."
                else:
                    resultado = "¡Correcto! Has adivinado el número."
                    entrada_numero.config(state="disabled")
                    boton_adivinar.config(state="disabled")
            intentos -= 1
            actualizar_resultado(resultado)
        except ValueError:
            label_resultado.config(text="Por favor, ingresa un número válido.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Adivina el Número")

# Etiquetas para mostrar información
label_instrucciones = tk.Label(root, text="Adivina un número entre 1 y 100", font=("Arial", 12))
label_instrucciones.pack()

label_resultado = tk.Label(root, text="", font=("Arial", 14))
label_resultado.pack()

label_intentos = tk.Label(root, text=f"Intentos restantes: {intentos}", font=("Arial", 12))
label_intentos.pack()

# Entrada para el número
entrada_numero = tk.Entry(root, font=("Arial", 12))
entrada_numero.pack(pady=5)

# Botón para hacer la adivinanza
boton_adivinar = tk.Button(root, text="Adivinar", command=adivinar, width=10, font=("Arial", 12))
boton_adivinar.pack(pady=5)

# Iniciar el bucle principal de la interfaz
root.mainloop()
