# **Juego (Snake)**
![Static Badge](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![MIT](https://img.shields.io/badge/MIT-License-blue)
## **Índice**
1. [**Descripción**](#descripción)
2. [**Instalación**](#instalación)
3. [**Herramientas Utilizadas**](#herramientas-utilizadas)
4. [**Uso**](#uso)
5. [**Requisitos**](#requisitos)
6. [**Licencia**](#licencia)
7. [**Autor**](#autor)

# **Descripción**
Este codigo es una version mas simple del conocido juego "**snake**" realizado en python usando la libreria de tkinter con algunos de sus modulos para la interfaz grafica, pygame para crear el juego y la libreria random para generar las frutas de manera aleatoria, se definen variables globales para la posicion de la serpiente, su movimiento y la posicion de ls frutas dentro de los espacios del mapa.

Si hablamos de la interfaz grafica debemos mencionar que se usa una estructura basica con dos frames y un canvas donde se dibujan los elementos del juego, se generan dos botones para comenzar y salir, ademas se muestra un contador que contiene la cantidad de frutas que se han recogido.

Podemos controlar la serpienre en 4 direcciones diferentes(derecha, izquierda, arriba y abajo), esta cuenta con colision lo que hace que si llegara a chocarse consigo misma acaba el juego

# **Instalación**
1. Debes asegurarte de tener instalado **python 3.11** o alguna version mas reciente
2. Importante tener instalada la libreria tkinter
3. tener en cuenta que se debe tener instalada la libreria pygame para poder crear el juego
4. Clona el repositorio con el siguiente comando
   ```bash
   https://github.com/Brandsete/Juego.git


# **Herramientas utilizadas**
- **python**: Lenguaje de programacion
- **tkinter**: Libreria de python usada para interfaces graficas
- **pygame**: Libreria de python utilizada para crear juegos
- **Random**: Usado para crear funciones de aletoriedad
- **Message box**: Usada para crear ventanas de texto emergentes

# **Uso**
En el momento que comenzamos a correr el codigo veremos una especie de juego Snake, en este podremos controlar la serpiente con las flechas directoras del teclado para ir comiendo manzanas que aparecen aletoriamente en el mapa, cada vez que comemos una manzana se agrega un bloque de largo a nuestra serpiente, debes tener cuidado de no chocar contigo mismo si no quieres que se acabe el juego y debas empezar desde cero.

# **Requisitos**
- **Python**
- **tkinter**
- **pygame**

# **Licencia**
Este proyecto está licenciado bajo la **MIT License**.

# **Autor**
[Samuel Usma Brand]
