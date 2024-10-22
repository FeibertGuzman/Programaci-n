import random 

def jugar():
    opciones = ['piedra', 'papel', 'tijera']
    puntuacion_usuario = 0
    puntuacion_PC = 0
    rondas = 10

    for _ in range(rondas):
        usuario = input("Elige: Piedra, Papel o Tijera: ").lower()

        if usuario not in opciones:
            print("Opción inválida. Debes elegir entre Piedra, Papel o Tijera.")
            continue

        PC = random.choice(opciones)
        print(f"PC eligió: {PC.capitalize()}")

        if usuario == PC:
            print("Es un empate.")
        else:  
            if usuario == 'piedra':
                if PC == 'tijera':
                    print("¡Ganaste! Piedra aplasta tijera.")
                    puntuacion_usuario += 1
                else: 
                    print("Perdiste. Papel envuelve piedra.")
                    puntuacion_PC += 1
            elif usuario == 'papel':
                if PC == 'piedra':
                    print("¡Ganaste! Papel envuelve piedra.")
                    puntuacion_usuario += 1
                else: 
                    print("Perdiste. Tijera corta papel.")
                    puntuacion_PC += 1
            elif usuario == 'tijera': 
                if PC == 'papel':
                    print("¡Ganaste! Tijera corta papel.")
                    puntuacion_usuario += 1
                else:
                    print("Perdiste. Piedra aplasta tijera.")
                    puntuacion_PC += 1

    # Mostrar el resultado final
    print(f"\nPuntuación final: Tú {puntuacion_usuario} - PC {puntuacion_PC}")
    if puntuacion_usuario > puntuacion_PC:
        print("¡Eres el ganador!")
    elif puntuacion_usuario < puntuacion_PC:
        print("La PC es la ganadora. Mejor suerte la próxima vez.")
    else:
        print("Es un empate en la puntuación final.")

# Llamada a la función para jugar
jugar()




     

