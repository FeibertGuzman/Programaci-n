# Laberinto Aventura en Python
![Static Badge](https://img.shields.io/badge/Python-12-red?logo=Python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)

## Índice

**1.** [Descripción](#descripción)

**2.** [¿Cómo puede ser clonado?](#cómo-puede-ser-clonado)

**3.** [Instalación](#instalación)

**4.** [Herramientas utilizas](#herramientas-utilizadas)

**5.** [Uso](#uso)

**6.** [Estructura del código](#estructura-del-codigo)

**7.** [Captura del proyecto](#captura-del-proyecto)

**8.** [Autor](#autor)

## Descripción
Este proyecto es un juego de laberinto interactivo creado en Python. El jugador comienza en el centro de un laberinto y tiene que buscar un tesoro mientras evita enemigos y puede ganar poderes especiales. El juego incluye un sistema de puntuación y muestra un ranking de jugadores al final.

### Características principales:

Movimiento del jugador dentro de un laberinto de 5x5.
Búsqueda de un tesoro oculto.
Encuentros con enemigos que deben ser evitados o derrotados.
Obtención de poderes especiales aleatorios.
Sistema de puntos basado en el hallazgo del tesoro.

## ¿Cómo puede ser clonado?

Clona este repositorio en tu máquina local. Para clonar este proyecto, asegúrate de tener Git instalado. Luego, clona el repositorio ejecutando el siguiente comando en tu terminal:
bash

## Instalación 
Para ejecutar el juego en tu máquina, sigue estos pasos:

Clona el repositorio utilizando el comando anterior.
Navega al directorio del proyecto:
bash
cd Laberinto-Aventura
Asegúrate de tener Python instalado en tu máquina. Este proyecto requiere Python 3.
Ejecuta el archivo Python:
bash
python laberinto.py

## Herramientas utilizadas 
Este proyecto fue desarrollado utilizando las siguientes herramientas:

Python 3.8+: Lenguaje de programación.
Random: Módulo para generar posiciones aleatorias.

## Uso
Para jugar el laberinto:

Mueve al jugador usando las teclas:
w: arriba
s: abajo
a: izquierda
d: derecha
Encuentra el tesoro (🪙) evitando a los enemigos (representados como *).
Si encuentras el tesoro, recibirás puntos. Si te encuentras con un enemigo, perderás.
El juego terminará mostrando tu puntuación y el ranking de jugadores.

## Estructura del código 
La estructura del código es la siguiente:

**laberinto:** Matriz que representa el laberinto.
**juga0dor_pos:** Lista que almacena la posición del jugador.
**tesoro_pos:** Posición aleatoria del tesoro.
**mostrar_lab():** Función que visualiza el laberinto con la posición del jugador, el tesoro y los enemigos.
Lógica de movimiento y combate con enemigos.
Sistema de puntos que se actualiza al encontrar el tesoro.

## Captura del proyecto


## Autor
Yan Frank Ríos López
