# proyecto_final_snake.py
# Proyecto Final de Lógica de Programación - Juego Snake Monolítico
# Desarrollado por: Johann Andrés Erazo Jiménez
# Demostración de estructuras repetitivas, condicionales en cascada y listas dinámicas.

import os
import random

# ==============================================================================
# 1. BLOQUE DE ESTADO (DATOS DEL JUGADOR Y VARIABLES INICIALES)
# ==============================================================================
# Limpiamos la consola para la pantalla de bienvenida
print("\n" * 50)
print("===================================")
print("   🐍 BIENVENIDO A SNAKE V2 🐍      ")
print("===================================")
nombre_jugador = input("Por favor, ingresa tu nombre: ")
edad_jugador = input("Por favor, ingresa tu edad: ")

ancho_tablero = 10
alto_tablero = 10

# ESTRUCTURA DE DATOS PRINCIPAL: Lista de tuplas para el cuerpo de la serpiente
# La cabeza es el elemento en el índice 0. Iniciamos con 3 segmentos para notar el cuerpo.
snake_body = [(5, 5), (5, 4), (5, 3)]

# Posición aleatoria de la primera comida (asegurando que no aparezca sobre la serpiente)
while True:
    comida_x = random.randint(0, ancho_tablero - 1)
    comida_y = random.randint(0, alto_tablero - 1)
    if (comida_y, comida_x) not in snake_body:
        break

puntos = 0
juego_activo = True

# ==============================================================================
# 2. BUCLE PRINCIPAL (ESTRUCTURA REPETITIVA PRINCIPAL)
# ==============================================================================
while juego_activo:
    
    # --------------------------------------------------------------------------
    # A. SUB-BLOQUE DE INTERFAZ (LIMPIEZA DE PANTALLA Y RENDERIZADO DE MATRIZ)
    # --------------------------------------------------------------------------
    # Limpiamos la consola en cada turno para dar efecto de animación en Spyder
    os.system("cls" if os.name == "nt" else "clear")
    
    # Cabecera con datos dinámicos
    print("=============================================================")
    print(f" 🐍 JUEGO SNAKE | JUGADOR: {nombre_jugador} ({edad_jugador} años) | PUNTOS: {puntos} ")
    print("=============================================================")
    
    # Dibujamos la pared superior del marco (#)
    print("#" * (ancho_tablero + 2))
    
    # Recorremos la matriz bidimensional para renderizar los caracteres
    for y in range(alto_tablero):
        fila = "#" # Pared izquierda del marco
        for x in range(ancho_tablero):
            
            # Condicionales para identificar qué dibujar en la coordenada actual
            if (y, x) == snake_body[0]:
                fila += "@" # Carácter para la Cabeza
            elif (y, x) in snake_body[1:]:
                fila += "O" # Carácter para el Cuerpo creciente
            elif x == comida_x and y == comida_y:
                fila += "*" # Carácter para la Comida
            else:
                fila += "." # Carácter para espacio vacío
                
        fila += "#" # Pared derecha del marco
        print(fila)
        
    # Dibujamos la pared inferior del marco (#)
    print("#" * (ancho_tablero + 2))

    # Lectura de la acción del usuario
    print("\nControles: W (Arriba), S (Abajo), A (Izquierda), D (Derecha)")
    print("Presiona Q para salir.")
    movimiento = input("Tu movimiento + Enter: ").lower()

    # --------------------------------------------------------------------------
    # B. SUB-BLOQUE DE CONTROL (LÓGICA MATEMÁTICA Y REGLAS DE DERROTA/CRECIMIENTO)
    # --------------------------------------------------------------------------
    
    # Extraemos la posición actual de la cabeza (Índice 0)
    head_y, head_x = snake_body[0]
    new_head_y, new_head_x = head_y, head_x

    # Escalera de decisiones para evaluar el input del teclado
    if movimiento == "q":
        juego_activo = False
        print(f"\nDecidiste salir del juego. ¡Gracias por jugar, {nombre_jugador}!")
        continue
    elif movimiento == "w":
        new_head_y -= 1
    elif movimiento == "s":
        new_head_y += 1
    elif movimiento == "a":
        new_head_x -= 1
    elif movimiento == "d":
        new_head_x += 1
    else:
        # Si presiona cualquier otra tecla, el bucle continúa sin aplicar movimiento
        continue

    # REGLA DE DERROTA 1: Validación de colisión contra las paredes (Límites 0-9)
    if new_head_x < 0 or new_head_x >= ancho_tablero or new_head_y < 0 or new_head_y >= alto_tablero:
        juego_activo = False
        print(f"\n¡GAME OVER, {nombre_jugador}! Chocaste contra las paredes del tablero.")
        continue

    # REGLA DE DERROTA 2: Validación de colisión contra sí misma (Autocolisión en la lista)
    new_head_coord = (new_head_y, new_head_x)
    if new_head_coord in snake_body[1:]:
        juego_activo = False
        print(f"\n¡GAME OVER, {nombre_jugador}! Te chocaste contra tu propio cuerpo.")
        continue

    # ACTUALIZACIÓN DEL CUERPO (Uso de métodos de listas)
    # Insertamos la nueva coordenada calculada al inicio de la lista (Nueva cabeza)
    snake_body.insert(0, new_head_coord)

    # REGLA DE CRECIMIENTO: Verificamos si la nueva cabeza llegó a la comida
    if new_head_x == comida_x and new_head_y == comida_y:
        puntos += 10 # Sumamos puntaje
        
        # Al NO ejecutar el método .pop(), la lista conserva el nuevo tamaño y la serpiente CRECE.
        # Generamos una nueva manzana asegurando que no aparezca encima del cuerpo
        while True:
            comida_x = random.randint(0, ancho_tablero - 1)
            comida_y = random.randint(0, alto_tablero - 1)
            if (comida_y, comida_x) not in snake_body:
                break
    else:
        # Si no comió, eliminamos el último elemento de la lista (.pop())
        # Esto hace que la serpiente se mueva fluidamente manteniendo su longitud actual
        snake_body.pop()

# Finalización formal del ciclo del programa
print("=============================================================")
print(f" FIN DEL JUEGO. Puntuación final de {nombre_jugador}: {puntos}")
print("=============================================================")