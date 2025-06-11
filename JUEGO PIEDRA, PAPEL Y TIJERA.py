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

