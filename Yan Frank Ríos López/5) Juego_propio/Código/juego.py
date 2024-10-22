import random

# LABERINTO
laberinto = [[' ' for _ in range(5)] for _ in range(5)]
jugador_pos = [2, 2]  # Posición inicial del jugador en el centro
tesoro_pos = [random.randint(0, 4), random.randint(0, 4)]

# POSICIÓN != DEL TESORO
while tesoro_pos == jugador_pos:
    tesoro_pos = [random.randint(0, 4), random.randint(0, 4)] #Número random entre 0 y 4

print("Laberinto inicial:\n")
for fila in laberinto:
    print(' '.join(fila))
def mostrar_lab(laberinto, jugador_pos, tesoro_pos):
    laberinto_copy = [fila[:] for fila in laberinto]
    laberinto_copy[jugador_pos[0]][jugador_pos[1]] = '👾'
    laberinto_copy[tesoro_pos[0]][tesoro_pos[1]] = '🪙'
    for fila in laberinto_copy:
        print(' '.join(fila))

while True:
    mostrar_lab(laberinto, jugador_pos, tesoro_pos)
    movimiento = input("Movimiento (w: arriba, s: abajo, a: izquierda, d: derecha): ").lower()

    # Actualizar posición del jugador
    if movimiento == 'w' and jugador_pos[0] > 0:    #filas
        jugador_pos[0] -= 1
    elif movimiento == 's' and jugador_pos[0] < 4:
        jugador_pos[0] += 1
    elif movimiento == 'a' and jugador_pos[1] > 0:   #columnas
        jugador_pos[1] -= 1
    elif movimiento == 'd' and jugador_pos[1] < 4:
        jugador_pos[1] += 1

    # Verificar colisión con el tesoro
    if jugador_pos == tesoro_pos:
        print("¡Felicidades! Has encontrado el tesoro.")
        break

print("Segundo round:")

# Agregar poderes especiales
poderes = ['velocidad', 'invisibilidad']
jugador_poder = None

if random.choice([True, False]):
    jugador_poder = random.choice(poderes)
    print(f"¡Has conseguido este súperpoder: {jugador_poder}")
    
# Agregar enemigos en posiciones aleatorias
enemigos = [[random.randint(0, 4), random.randint(0, 4)] for _ in range(3)]

# Asegúrate de que los enemigos no estén en la posición del jugador o el tesoro
for enemigo in enemigos:
    while enemigo == jugador_pos or enemigo == tesoro_pos:
        enemigo = [random.randint(0, 4), random.randint(0, 4)]
        jugador_pos = [random.randint(0, 4), random.randint(0, 4)]
        tesoro_pos = [random.randint(0, 4), random.randint(0, 4)]

def mostrar_lab_combat(laberinto, jugador_pos, tesoro_pos, enemigos):
    laberinto_copy = [fila[:] for fila in laberinto]
    laberinto_copy[jugador_pos[0]][jugador_pos[1]] = '👾'
    laberinto_copy[tesoro_pos[0]][tesoro_pos[1]] = '🪙'
    for enemigo in enemigos:
        laberinto_copy[enemigo[0]][enemigo[1]] = '*'
    for fila in laberinto_copy:
        print(' '.join(fila))

# Lógica de combate
jugador_vida=6
enemigo_vida=4
def combatir(jugador_vida, enemigo_vida):
    while jugador_vida > 0 and enemigo_vida > 0:
        print("¡Luchando contra el enemigo!")
        enemigo_vida -= 1  # Simulación de ataque
        if enemigo_vida <= 0:
            return True  # Jugador gana
        jugador_vida -= 1  # Simulación de ataque del enemigo
    return False  # Jugador pierde

while True:
    mostrar_lab_combat(laberinto, jugador_pos, tesoro_pos, enemigos)
    movimiento = input("Movimiento (w: arriba, s: abajo, a: izquierda, d: derecha): ").lower()
    
    # Actualizar posición del jugador
    if movimiento == 'w' and jugador_pos[0] > 0:    #filas
        jugador_pos[0] -= 1
    elif movimiento == 's' and jugador_pos[0] < 4:
        jugador_pos[0] += 1
    elif movimiento == 'a' and jugador_pos[1] > 0:   #columnas
        jugador_pos[1] -= 1
    elif movimiento == 'd' and jugador_pos[1] < 4:
        jugador_pos[1] += 1

    if jugador_pos == enemigo:  # Vida del jugador, vida del enemigo
                print("Has sido derrotado.")
                exit()

    if jugador_pos == tesoro_pos:
        print("¡Felicidades! Has encontrado el tesoro.")
        break

# Sistema de puntos
puntos = 0

    # Movimiento y combate como antes...
if jugador_pos == tesoro_pos:
        puntos += 10
        print(f"¡Felicidades! Has encontrado el tesoro. Puntos: {puntos}")
else:
    print(f"Owwwww, ¡Has perdido!: {puntos}")
    
# Mostrar ranking de jugadores (puedes implementar un sistema para guardarlo)
print("Ranking de jugadores:")
print(f"Jugador: {puntos} puntos")
