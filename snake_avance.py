import time

# --- 1. MANEJO Y USO DE VARIABLES ---
nombre_jugador = "Invitado"
edad_jugador = "0"
juego_iniciado = False
estado = "JUGANDO"  

# Coordenadas iniciales de la serpiente (en un plano de texto de 10x10)
posicion_x = 5
posicion_y = 5

# --- 2. ESTRUCTURA REPETITIVA PRINCIPAL (BUCLE WHILE) ---
while True:
    
    # FASE 1: REGISTRO DE USUARIO (Solo ocurre al inicio)
    if juego_iniciado == False:
        print("========================================")
        print("      BIENVENIDO AL PROYECTO SNAKE      ")
        print("========================================")
        
        # Pedir datos usando el input clásico de Python
        nombre_jugador = input("Introduce tu nombre: ")
        edad_jugador = input("Introduce tu edad: ")
        
        print("\nCargando entorno...")
        
        # --- USO DE BUCLE FOR E "IN" (Pantalla de carga obligatoria) ---
        # Recorremos una lista de strings para simular que el juego se está preparando
        for punto in [".", ". .", ". . .", ". . . ."]:
            print(punto)
            time.sleep(0.4) # Una pequeña pausa para dar efecto visual
            
        print("\n¡EMPECEMOS!")
        print("========================================\n")
        time.sleep(1)
        juego_iniciado = True

    # FASE 2: EL JUEGO ACTIVO (Por turnos en la consola)
    else:
        print("--------------------------------------------------")
        print(f"JUGADOR: {nombre_jugador} ({edad_jugador} años) | ESTADO: {estado}")
        print(f"Posición actual de la Serpiente: X={posicion_x}, Y={posicion_y}")
        print("--------------------------------------------------")
        
        # Menú de acciones por teclado mediante input()
        print("CONTROLES: W (Arriba) | S (Abajo) | A (Izquierda) | D (Derecha) | P (Pausa)")
        accion = input("¿Qué deseas hacer?: ")
        
        # Validación por si digitan en minúscula
        if accion:
            accion = accion.upper()

        # --- ESTRUCTURAS CONDICIONALES (IF - ELIF - ELSE) ---
        # Evalúa si el usuario quiere pausar o despausar el juego
        if accion == "P":
            if estado == "JUGANDO":
                estado = "PAUSADO"
                print("\n[ JUEGO EN PAUSA ]")
            else:
                estado = "JUGANDO"
                print("\n[ JUEGO REANUDADO ]")
        
        # Control de movimiento: Solo altera las coordenadas numéricas si el estado es JUGANDO
        elif estado == "JUGANDO":
            if accion == "W":
                posicion_y = posicion_y + 1
                print("\n-> La serpiente se movió hacia ARRIBA.")
            elif accion == "S":
                posicion_y = posicion_y - 1
                print("\n-> La serpiente se movió hacia ABAJO.")
            elif accion == "A":
                posicion_x = posicion_x - 1
                print("\n-> La serpiente se movió hacia la IZQUIERDA.")
            elif accion == "D":
                posicion_x = posicion_x + 1
                print("\n-> La serpiente se movió hacia la DERECHA.")
            else:
                print("\n[!] Dirección no válida. Usa W, A, S o D.")
                
        else:
            print("\n[!] El juego está PAUSADO. Presiona 'P' para despausar antes de moverte.")
            
        print("\n") # Espacio en blanco para el siguiente turno
