# 🐍 El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas

Bienvenido al repositorio de mi proyecto final para la materia de Lógica de Programación. El sistema desarrollado consiste en una versión interactiva del clásico videojuego "Snake" implementado en consola.

Bienvenido al repositorio de mi proyecto final para la materia de Lógica de Programación. 

### 👤 Integrantes
* Johann Andrés Erazo Jiménez

### 📅 Fecha
* 28 de junio de 2026

### 🎯 Objetivo del sistema
Desarrollar una versión interactiva del clásico videojuego "Snake" utilizando Python puro para la consola. El objetivo principal de este proyecto es llevar la teoría a la práctica, demostrando el dominio de estructuras repetitivas (bucles `while` y `for`), condicionales en cascada (`if/elif`) y la manipulación dinámica de listas (usando `.insert()` y `.pop()`) para lograr que la serpiente crezca y se mueva correctamente dentro de un archivo de arquitectura monolítica.

### ⚙️ Descripción de funcionalidades
El sistema permite al jugador interactuar con el juego directamente desde la consola a través de las siguientes funciones:
* **Iniciar Juego:** El sistema solicita el nombre y la edad del jugador antes de generar el tablero de 10x10.
* **Cambiar Dirección:** El jugador controla el movimiento de la cabeza de la serpiente (`@`) utilizando las teclas **W** (arriba), **S** (abajo), **A** (izquierda) y **D** (derecha).
* **Visualizar Puntuación y Crecimiento:** Al comer una manzana (`*`), el jugador suma 10 puntos en el marcador en vivo y el cuerpo de la serpiente (`O`) crece una casilla automáticamente.
* **Detección de Colisiones (Game Over):** El programa calcula matemáticamente si la serpiente choca contra los límites del tablero (paredes) o si colisiona contra su propio cuerpo, terminando la partida y mostrando el puntaje final.
* **Salir del Juego:** El usuario puede interrumpir y salir de la partida en cualquier turno presionando la tecla **Q**.

---
*Nota: En este repositorio también se incluyen los diagramas de Casos de Uso, Diagrama de Flujo y Arquitectura del Sistema en formato imagen, junto con el código fuente completo en el archivo `.py`.*
