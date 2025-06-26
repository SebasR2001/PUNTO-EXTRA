Algoritmo PiedraPapelTijera
	Definir nombre1, nombre2, opcion1, opcion2, seguir Como Caracter
	Definir gana1, gana2, empates Como Entero
	gana1 <- 0
	gana2 <- 0
	empates <- 0
	Escribir 'Ingrese el nombre del jugador 1:'
	Leer nombre1
	Escribir 'Ingrese el nombre del jugador 2:'
	Leer nombre2
	Repetir
		Escribir nombre1, ', elige: Piedra, Papel o Tijera'
		Leer opcion1
		opcion1 <- Minusculas(opcion1)
		Mientras opcion1<>'piedra' Y opcion1<>'papel' Y opcion1<>'tijera' Hacer
			Escribir 'Opción inválida. Intenta de nuevo:'
			Leer opcion1
			opcion1 <- Minusculas(opcion1)
		FinMientras
		Escribir nombre2, ', elige: Piedra, Papel o Tijera'
		Leer opcion2
		opcion2 <- Minusculas(opcion2)
		Mientras opcion2<>'piedra' Y opcion2<>'papel' Y opcion2<>'tijera' Hacer
			Escribir 'Opción inválida. Intenta de nuevo:'
			Leer opcion2
			opcion2 <- Minusculas(opcion2)
		FinMientras
		Si opcion1=opcion2 Entonces
			Escribir 'Empate!'
			empates <- empates+1
		SiNo
			Si (opcion1='piedra' Y opcion2='tijera') O (opcion1='papel' Y opcion2='piedra') O (opcion1='tijera' Y opcion2='papel') Entonces
				Escribir nombre1, ' gana esta ronda!'
				gana1 <- gana1+1
			SiNo
				Escribir nombre2, ' gana esta ronda!'
				gana2 <- gana2+1
			FinSi
		FinSi
		Escribir '¿Quieren seguir jugando? (si/no)'
		Leer seguir
		seguir <- Minusculas(seguir)
	Hasta Que seguir='no'
	Escribir 'Resumen de resultados:'
	Escribir '------------------------------------'
	Escribir nombre1, ' ganó ', gana1, ' veces.'
	Escribir nombre2, ' ganó ', gana2, ' veces.'
	Escribir 'Empates: ', empates
	Escribir '------------------------------------'
	Si gana1>gana2 Entonces
		Escribir nombre1, ', ganaste, ¡felicidades!'
	SiNo
		Si gana2>gana1 Entonces
			Escribir nombre2, ', ganaste, ¡felicidades!'
		SiNo
			Escribir 'Hubo un empate general entre ', nombre1, ' y ', nombre2
		FinSi
	FinSi
FinAlgoritmo
