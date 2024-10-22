import random 

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    victorias_usuario = 0
    victorias_pc = 0
    
    while True:
        usuario = input("Elige: piedra, papel, tijera (o 'salir' para terminar): ").lower()
        
        if usuario == 'salir':
            print("Gracias por jugar!")
            print(f"Resultados finales - Tú: {victorias_usuario}, PC: {victorias_pc}")
            break
        
        if usuario not in opciones:
            print("Opción inválida. Por favor elige piedra, papel o tijera.")
            continue
        
        pc = random.choice(opciones)
        print(f"PC eligió: {pc}")

        if usuario == pc:
            print("Empate")
        else:
            if usuario == "piedra":
                if pc == "tijera":
                    print("Ganaste!")
                    victorias_usuario += 1
                else:
                    print("Perdiste!")
                    victorias_pc += 1
            elif usuario == "papel":
                if pc == "piedra":
                    print("Ganaste!")
                    victorias_usuario += 1
                else:
                    print("Perdiste!")
                    victorias_pc += 1
            elif usuario == "tijera":
                if pc == "papel":
                    print("Ganaste!")
                    victorias_usuario += 1
                else:
                    print("Perdiste!")
                    victorias_pc += 1
        
        print(f"Marcador - Tú: {victorias_usuario}, PC: {victorias_pc}")

# Llama a la función para jugar
jugar()
