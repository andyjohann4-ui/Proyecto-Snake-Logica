import os
import random

# ==========================================
# 1. VARIABLES INICIALES DEL JUEGO
# ==========================================
ancho_tablero = 10
alto_tablero = 10

# Posición inicial de la serpiente (en el centro)
serpiente_x = 5
serpiente_y = 5

# Posición aleatoria de la primera comida
comida_x = random.randint(0, ancho_tablero - 1)
comida_y = random.randint(0, alto_tablero - 1)

puntos = 0
juego_activo = True

# ==========================================
# 2. BUCLE PRINCIPAL (Estructura Repetitiva)
# ==========================================
# Este while mantiene el juego corriendo hasta que perdamos o salgamos
while juego_activo:
    
    # Limpiamos la consola para que no se amontone el texto (cls en Windows, clear en Mac/Linux)
    os.system("cls" if os.name == "nt" else "clear")
    
    print("===================================")
    print(f"   🐍 JUEGO SNAKE | PUNTOS: {puntos} ")
    print("===================================")

    # 3. DIBUJAR EL TABLERO (Bucles for anidados)
    # Recorremos cada fila (Y) y cada columna (X) para dibujar el mapa
    for y in range(alto_tablero):
        fila = ""
        for x in range(ancho_tablero):
            
            # 4. CONDICIONALES PARA DIBUJAR LOS ELEMENTOS
            if x == serpiente_x and y == serpiente_y:
                fila += "[O]" # Dibujamos la cabeza de la serpiente
            elif x == comida_x and y == comida_y:
                fila += " * " # Dibujamos la comida
            else:
                fila += " . " # Dibujamos un espacio vacío del tablero
                
        print(fila) # Imprimimos la fila completa antes de pasar a la siguiente

    # 5. PEDIR ACCIÓN AL USUARIO
    print("\nControles: W (Arriba), S (Abajo), A (Izquierda), D (Derecha)")
    print("Presiona Q para salir.")
    movimiento = input("Tu movimiento + Enter: ").lower()

    # 6. CONDICIONALES DE MOVIMIENTO
    if movimiento == "q":
        juego_activo = False
        print("Decidiste salir del juego.")
    elif movimiento == "w":
        serpiente_y = serpiente_y - 1 # Subir es restar en el eje Y
    elif movimiento == "s":
        serpiente_y = serpiente_y + 1 # Bajar es sumar en el eje Y
    elif movimiento == "a":
        serpiente_x = serpiente_x - 1 # Izquierda es restar en el eje X
    elif movimiento == "d":
        serpiente_x = serpiente_x + 1 # Derecha es sumar en el eje X
    else:
        # Si presiona otra tecla, el bucle vuelve a empezar sin hacer nada
        continue

    # 7. CONDICIONALES DE DERROTA (Chocar contra la pared)
    # Verificamos si la serpiente se salió de los límites del 0 al 9
    if serpiente_x < 0 or serpiente_x >= ancho_tablero or serpiente_y < 0 or serpiente_y >= alto_tablero:
        juego_activo = False
        print("\n¡GAME OVER! Chocaste contra la pared limitante.")

    # 8. CONDICIONALES PARA COMER Y GANAR PUNTOS
    # Si las coordenadas de la serpiente y la comida son iguales
    if serpiente_x == comida_x and serpiente_y == comida_y:
        puntos = puntos + 10 # Aumentamos la puntuación
        
        # Generamos una nueva comida en una posición aleatoria
        comida_x = random.randint(0, ancho_tablero - 1)
        comida_y = random.randint(0, alto_tablero - 1)

# Mensaje final cuando se rompe el bucle while
print("===================================")
print(f" FIN DEL JUEGO. Puntuación final: {puntos}")
print("===================================")