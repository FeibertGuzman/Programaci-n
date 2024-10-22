# Proyecto de Calculadora en **html** y **css**

## índice

**1.** [Descripción](#descripción)

**2.** [¿Cómo puede ser clonado?](#cómo-puede-ser-clonado)

**3.** [Instalación](#instalación)

**4.** [Herramientas utilizas](#herramientas-utilizadas)

**5.** [Uso](#uso)

**6.** [Estructura del código](#estructura-del-codigo)

**7.** [Captura del código](#captura-del-codigo)

**8.** [Autor](#autor)

## Descripción 
Este proyecto es una calculadora web interactiva que permite a los usuarios realizar operaciones matemáticas, así como el cálculo del Mínimo Común Múltiplo (MCM), el Máximo Común Divisor (MCD), suma, resta, división, multiplicación y división. La interfaz es intuitiva y está diseñada para ser accesible desde diferentes dispositivos, gracias a su diseño responsivo. La calculadora incluye campos para ingresar hasta tres números y una lista desplegable para seleccionar la operación deseada. Además, tiene un link a través del cual instruye a sus usuario sobre cómo utilizar esta calculadora.

### Primera parte: Estructura HTML

El archivo "index.html" define la estructura básica de la página web. Se incluye la etiqueta "meta" que establece la vista responsiva, permitiendo que la calculadora se adapte a diferentes tamaños de pantalla. El título de la página se establece como "Calculadora" y se vincula un archivo de estilos CSS "(style.css)" para aplicar el diseño visual. Dentro del cuerpo "(body)", se crea un encabezado "header" que contiene un título principal "h1" que dice "calculadora". Debajo del título, se incluye un menú de navegación que permite al usuario acceder a la página de instrucciones a través de un enlace. La sección principal del cuerpo incluye un formulario donde el usuario puede ingresar los datos requeridos para realizar cálculos. Hay tres campos de entrada, donde el segundo y tercer campos son numéricos, y la operación deseada se selecciona a través de un menú desplegable.

### Segunda parte: Funcionalidad de JavaScript

En esta sección, se inserta un bloque de código JavaScript que implementa la lógica de la calculadora. Se define la función Calcular(), que se ejecuta al hacer clic en el botón "Calcular".
La función obtiene los valores ingresados por el usuario en los campos de entrada y la operación seleccionada. A través de una estructura switch, se evalúa qué operación debe realizarse, que puede ser suma, resta, multiplicación, división, MCM o MCD. Dependiendo de la operación seleccionada, se ejecutan diferentes cálculos y se manejan los casos de error, como la división por cero.
Además, se definen dos funciones auxiliares, calcularMCM() y calcularMCD(), que se utilizan para calcular el MCM y el MCD, respectivamente. Ambas funciones utilizan la recursividad para realizar los cálculos necesarios.

### Tercera parte: Diseño CSS

El archivo style.css se encarga de definir la apariencia visual de la calculadora. Se establece una fuente general para todo el cuerpo, utilizando la familia Arial. El fondo se configura con una imagen y se centra todo el contenido utilizando flexbox.
El encabezado se estiliza con un color de fondo (lightseagreen), sombra de texto y bordes redondeados para darle un aspecto más atractivo. Los enlaces del menú de navegación cambian de color al pasar el cursor sobre ellos, mejorando la interactividad.
Los campos del formulario se diseñan con un enfoque en la usabilidad, asegurando que se mantengan claros y accesibles. Se utiliza un efecto de enfoque para cambiar el color y la posición de las etiquetas al hacer clic en los campos, lo que mejora la experiencia del usuario.

### Cuarta parte: Instrucciones en HTML

La página instru.html proporciona instrucciones detalladas sobre cómo usar la calculadora. Comienza con un encabezado que indica que se trata de instrucciones para utilizar la calculadora. A través de una serie de secciones numeradas, se explica cómo acceder a la calculadora, entender la interfaz, ingresar los datos, seleccionar la operación y ver los resultados.
Cada sección incluye un encabezado y un texto explicativo que guía al usuario a través del proceso, asegurándose de que comprenda cada paso necesario para utilizar la calculadora de manera efectiva.

### Quinta parte: Interactividad y Usabilidad

La calculadora está diseñada para ser altamente interactiva. Los mensajes de error se manejan adecuadamente, proporcionando retroalimentación al usuario en caso de que se produzcan errores, como intentar dividir por cero. Además, los resultados se muestran de manera clara, permitiendo que los usuarios verifiquen rápidamente los resultados de sus cálculos.
Los estilos aplicados a los elementos de la interfaz, como botones y campos de entrada, garantizan que sean fáciles de usar y visualmente atractivos, lo que contribuye a una experiencia de usuario fluida y agradable.

## ¿Cómo puede ser clonado?

### 1. Clona este repositorio en tu máquina local

Para clonar este proyecto, puedes utilizar Git. Asegúrate de tener Git instalado en tu sistema. Luego, puedes clonar el repositorio ejecutando el siguiente comando en tu terminal:

Copiar código: **git clone <[URL del repositorio](https://github.com/lppz16/Calculadora-html-css.git)>**

## Instalación
Para ejecutar la calculadora en tu propio entorno, sigue estos pasos:

**1.** Clona el repositorio utilizando el comando mencionado anteriormente.

**2.** Navega al directorio del proyecto:
Copiar código: **cd Calculadora-html-css**

**3.** Abre el archivo index.html en tu navegador preferido. Puedes hacerlo haciendo doble clic en el archivo o arrastrándolo a la ventana del navegador.

## Herramientas utilizadas

Este proyecto fue desarrollado utilizando las siguientes herramientas y tecnologías:

**1. HTML:** Para la estructura básica de la página web.

**2. CSS:** Para el diseño y estilización de la interfaz.

**3. JavaScript:** Para implementar la lógica de la calculadora y manejar las interacciones del usuario.

**4. Google Fonts:** Para mejorar la tipografía de la interfaz.

## Uso

Para utilizar la calculadora, sigue estos pasos:

**1.** Abre la página de la calculadora en tu navegador.

**2.** Ingresa los números en los campos correspondientes.

**3.** Selecciona la operación deseada desde el menú desplegable.

**4.** Haz clic en el botón "Calcular" para obtener el resultado.

**5.** El resultado se mostrará en un campo de texto debajo de la calculadora. Si deseas realizar otro cálculo, simplemente ingresa nuevos valores y haz clic en "Calcular" nuevamente.

## Estructura del código:

La estructura del código está organizada de la siguiente manera:

**1. index.html:** Archivo principal que contiene la estructura HTML de la calculadora.

**2. instru.html:** Archivo que contiene las instrucciones de uso de la calculadora.

**3. style.css:** Archivo de estilos que define el diseño de la calculadora y la página de instrucciones.

**4. style2.css:** Archivo de estilos para la página de instrucciones.

**5. JavaScript:** Incrustado en el archivo HTML, se encarga de la lógica de la calculadora, incluyendo las funciones para realizar las operaciones matemáticas y calcular el MCM y el MCD.

## Captura del proyecto:

![Página principal](https://github.com/lppz16/Calculadora-html-css/blob/main/Img/Captura%20de%20pantalla%202024-10-05%20233251.png?raw=true)

![](https://github.com/lppz16/Calculadora-html-css/blob/main/Img/Captura%20de%20pantalla%202024-10-05%20233303.png?raw=true)

## Autor

Yan Frank Ríos López
