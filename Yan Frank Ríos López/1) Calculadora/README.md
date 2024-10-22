# Mega Calculadora en Python con Tkinter

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![ttk](https://img.shields.io/badge/ttk-module-green)
![subprocess](https://img.shields.io/badge/subprocess-module-orange)
![math](https://img.shields.io/badge/math-module-yellow)
![MIT](https://img.shields.io/badge/MIT-License-blue)

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
Este proyecto es una calculadora interactiva creada con Python y la biblioteca Tkinter. Permite realizar diversas operaciones matemáticas, como suma, resta, multiplicación, división, cálculo del Valor Absoluto, Mínimo Común Múltiplo (MCM) y Máximo Común Divisor (MCD). Además, incluye un historial de operaciones que permite editar y eliminar entradas, así como una función para cambiar el color del fondo de la interfaz de manera aleatoria.

La interfaz gráfica es intuitiva y fácil de usar, diseñada para operar en un entorno de escritorio.

### Características principales:
Suma, resta, multiplicación y división.
Valor absoluto de un número.
Cálculo del MCM y MCD.
Historial interactivo de operaciones.
Función para cambiar el color del fondo aleatoriamente.

## ¿Cómo puede ser clonado?
### 1. Clona este repositorio en tu máquina local:
Para clonar este proyecto, asegúrate de tener Git instalado. Luego, clona el repositorio ejecutando el siguiente comando en tu terminal:

bash
git clone https://github.com/lppz16/MenuCalc.git

## Instalación
Para ejecutar la calculadora en tu máquina, sigue estos pasos:

Clona el repositorio utilizando el comando anterior.

**Navega al directorio del proyecto:**

bash
cd Mega-Calculadora

Instala las dependencias necesarias (si las hay). Este proyecto solo requiere Tkinter, que viene preinstalado en la mayoría de las versiones de Python.

**Ejecuta el archivo Python:**
bash
python calculadora.py

## Herramientas utilizadas
Este proyecto fue desarrollado utilizando las siguientes herramientas:

**Python 3.8+:** Lenguaje de programación.
**Tkinter:** Biblioteca para la creación de interfaces gráficas.
**Math:** Módulo para realizar operaciones matemáticas.
**Random:** Módulo para generar colores aleatorios.

## Uso
Para utilizar la calculadora:

**1.** Ingresa los números en los campos correspondientes ("Número 1" y "Número 2").
**2.** Selecciona la operación que deseas realizar desde el menú o presiona el botón correspondiente.
**3.** El resultado aparecerá en el campo "Resultado".
**4.** El historial de operaciones se mostrará en una lista donde puedes editar o eliminar entradas.
**5.** Haz clic en el botón "Click para cambiar el color" para cambiar el fondo de la calculadora aleatoriamente.

## Estructura del código
La estructura del código es la siguiente:

**crear_ventana():** Función que crea la ventana principal de la calculadora con sus elementos gráficos.
**Funciones matemáticas:** fnSuma(), fnResta(), fnMult(), fnDivi(): Realizan las operaciones básicas.
fnValAbs(): Calcula el valor absoluto.
fnMCM(), fnMCD(): Calculan el Mínimo Común Múltiplo y Máximo Común Divisor.
**Historial de operaciones:**
append_to_history(): Agrega las operaciones al historial.
delete_history(): Elimina entradas seleccionadas del historial.
edit_history(): Permite editar las entradas del historial.
changeBG(): Cambia el color de fondo de la ventana de manera aleatoria.
**Menú de opciones:** Permite seleccionar operaciones matemáticas desde la barra de menú.

## Captura del proyecto:
![](https://github.com/FeibertGuzman/Programaci-n/blob/d8b25e280e1d0130292171fa92a7c593baf1da8f/Yan%20Frank%20R%C3%ADos%20L%C3%B3pez/1)%20Calculadora/img/Captura%20de%20pantalla%202024-10-21%20222126.png)

![](https://github.com/FeibertGuzman/Programaci-n/blob/d8b25e280e1d0130292171fa92a7c593baf1da8f/Yan%20Frank%20R%C3%ADos%20L%C3%B3pez/1)%20Calculadora/img/Captura%20de%20pantalla%202024-10-21%20222134.png)

![](https://github.com/FeibertGuzman/Programaci-n/blob/d8b25e280e1d0130292171fa92a7c593baf1da8f/Yan%20Frank%20R%C3%ADos%20L%C3%B3pez/1)%20Calculadora/img/Captura%20de%20pantalla%202024-10-21%20222306.png))

## Autor
Yan Frank Ríos López
