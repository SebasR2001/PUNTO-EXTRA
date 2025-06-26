# PUNTO-EXTRA
# Juego Piedra, Papel o Tijera en Python con validaciones y mejoras

# Definimos variables para almacenar nombres y resultados
nombre1 = ""  # Nombre del jugador 1
nombre2 = ""  # Nombre del jugador 2
opcion1 = ""  # Opción elegida por el jugador 1 (Piedra, Papel o Tijera)
opcion2 = ""  # Opción elegida por el jugador 2 (Piedra, Papel o Tijera)
seguir = ""   # Variable para controlar si los jugadores desean seguir jugando
gana1 = 0     # Contador de victorias del jugador 1
gana2 = 0     # Contador de victorias del jugador 2
empates = 0   # Contador de empates

# Diccionario para saber qué opción gana a cuál
ganador = {
    'piedra': 'tijera',
    'tijera': 'papel',
    'papel': 'piedra'
}

# Solicitar nombres de los jugadores
nombre1 = input("Ingrese el nombre del jugador 1: ")
nombre2 = input("Ingrese el nombre del jugador 2: ")

# Iniciar el juego y repetir mientras los jugadores deseen seguir jugando
while seguir != 'no':
    # JUGADOR 1: elegir y validar su opción
    try:
        opcion1 = input(f"{nombre1}, elige: Piedra, Papel o Tijera: ").lower()
        while opcion1 not in ['piedra', 'papel', 'tijera']:
            print("Opción inválida. Intenta de nuevo:")
            opcion1 = input().lower()
    except:
        print("Ocurrió un error al ingresar la opción. Intenta de nuevo.")
        continue  # vuelve a empezar el bucle

    # JUGADOR 2: elegir y validar su opción
    try:
        opcion2 = input(f"{nombre2}, elige: Piedra, Papel o Tijera: ").lower()
        while opcion2 not in ['piedra', 'papel', 'tijera']:
            print("Opción inválida. Intenta de nuevo:")
            opcion2 = input().lower()
    except:
        print("Ocurrió un error al ingresar la opción. Intenta de nuevo.")
        continue  # vuelve a empezar el bucle

    # COMPARAR OPCIONES Y ASIGNAR RESULTADO
    if opcion1 == opcion2:
        print("¡Empate!")
        empates += 1
    elif ganador[opcion1] == opcion2:
        print(nombre1 + " gana esta ronda!")
        gana1 += 1
    else:
        print(nombre2 + " gana esta ronda!")
        gana2 += 1

    # Preguntar si desean seguir jugando
    seguir = input("¿Quieren seguir jugando? (si/no): ").lower()
    while seguir not in ['si', 'no']:
        seguir = input("Respuesta inválida. Escribe 'si' o 'no': ").lower()

# MOSTRAR RESUMEN FINAL
print("\nResumen de resultados:")
print('------------------------------------')
print(f"{nombre1} ganó {gana1} veces.")
print(f"{nombre2} ganó {gana2} veces.")
print(f"Empates: {empates}")
print('------------------------------------')

# DETERMINAR AL GANADOR GENERAL
if gana1 > gana2:
    print(f"{nombre1}, ganaste el juego completo. ¡Felicidades!")
elif gana2 > gana1:
    print(f"{nombre2}, ganaste el juego completo. ¡Felicidades!")
else:
    print(f"Hubo un empate general entre {nombre1} y {nombre2}.")
=======
# Definir variables para almacenar nombres, opciones y resultados del juego
nombre1 = ""  # Nombre del jugador 1
nombre2 = ""  # Nombre del jugador 2
opcion1 = ""  # Opción elegida por el jugador 1 (Piedra, Papel o Tijera)
opcion2 = ""  # Opción elegida por el jugador 2 (Piedra, Papel o Tijera)
seguir = ""   # Variable para controlar si los jugadores desean seguir jugando
gana1 = 0     # Contador de victorias del jugador 1
gana2 = 0     # Contador de victorias del jugador 2
empates = 0   # Contador de empates

# Solicitar nombres de los jugadores
nombre1 = input("Ingrese el nombre del jugador 1: ")
nombre2 = input("Ingrese el nombre del jugador 2: ")

# Iniciar el juego y repetir mientras los jugadores deseen seguir jugando
while seguir != 'no':
    # Jugador 1 elige una opción (Piedra, Papel o Tijera)
    print(nombre1 + ', elige: Piedra, Papel o Tijera')
    opcion1 = input().lower()
    
    # Validar la opción elegida por el jugador 1
    while opcion1 != 'piedra' and opcion1 != 'papel' and opcion1 != 'tijera':
        print('Opción inválida. Intenta de nuevo:')
        opcion1 = input().lower()

    # Jugador 2 elige una opción (Piedra, Papel o Tijera)
    print(nombre2 + ', elige: Piedra, Papel o Tijera')
    opcion2 = input().lower()
    
    # Validar la opción elegida por el jugador 2
    while opcion2 != 'piedra' and opcion2 != 'papel' and opcion2 != 'tijera':
        print('Opción inválida. Intenta de nuevo:')
        opcion2 = input().lower()

    # Determinar el resultado de la ronda
    if opcion1 == opcion2:
        print('Empate!')
        empates += 1  # Incrementar el contador de empates si las opciones son iguales
    elif (opcion1 == 'piedra' and opcion2 == 'tijera') or \
         (opcion1 == 'papel' and opcion2 == 'piedra') or \
         (opcion1 == 'tijera' and opcion2 == 'papel'):
        print(nombre1 + ' gana esta ronda!')
        gana1 += 1  # Incrementar el contador de victorias del jugador 1 si gana
    else:
        print(nombre2 + ' gana esta ronda!')
        gana2 += 1  # Incrementar el contador de victorias del jugador 2 si gana

    # Preguntar a los jugadores si desean seguir jugando
    seguir = input('¿Quieren seguir jugando? (si/no)').lower()

# Mostrar resumen de resultados al finalizar el juego
print('Resumen de resultados:')
print('------------------------------------')
print(nombre1 + ' ganó ' + str(gana1) + ' veces.')
print(nombre2 + ' ganó ' + str(gana2) + ' veces.')
print('Empates: ' + str(empates))
print('------------------------------------')

# Determinar y mostrar al ganador general del juego
if gana1 > gana2:
    print(nombre1 + ', ganaste, ¡felicidades!')
elif gana2 > gana1:
    print(nombre2 + ', ganaste, ¡felicidades!')
else:
    print('Hubo un empate general entre ' + nombre1 + ' y ' + nombre2)
