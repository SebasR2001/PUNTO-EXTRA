# Juego Piedra, Papel o Tijera en Python con validaciones y mejoras

# Definimos variables para almacenar nombres y resultados
nombre1 = ""
nombre2 = ""
opcion1 = ""
opcion2 = ""
seguir = ""
gana1 = 0
gana2 = 0
empates = 0

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