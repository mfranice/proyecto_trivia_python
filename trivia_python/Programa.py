import csv
import random

archivo = 'Preguntas y respuestas.csv'

def agregar_preguntas():

    while True:

        #La función solicita el ingreso de una pregunta, 4 posibles respuestas de las cuales una debe ser correcta, y la respusta correcta.
        #Cada una de las peticiones del programa se guarda en una variable:

        print('Ingrese la nueva pregunta:')
        pregunta = str(input())
        
        print('Ingrese la opción A):')
        opcion_a = str(input())

        print('Ingrese la opción B):')
        opcion_b = str(input())

        print('Ingrese la opción C):')
        opcion_c = str(input())   

        print('Ingrese la opción D):')
        opcion_d = str(input())

        print('Ingrese la respuesta correcta:')
        respuesta_correcta = str(input())
        
        #Con las variables ingresadas por el usuario se genera un diccionario:
        
        nueva_pregunta = {'pregunta': pregunta, 'opcion_a': opcion_a, 'opcion_b': opcion_b, 'opcion_c': opcion_c, 'opcion_d': opcion_d, 'respuesta_correcta': respuesta_correcta}

        #Se muestra al usuario nuevamente la la pregunta, opciones y respuesta correta ingresados para que el mismo las pueda verificar 
        #antes de concretar la carga.

        print('La nueva pregunta que se cargará es la siguiente:\n')
        print('Pregunta:', pregunta,'\n')
        print('Opcion A)', opcion_a)
        print('Opcion B)', opcion_b)
        print('Opcion C)', opcion_c)
        print('Opcion D)', opcion_d,'\n')
        print('La respuesta correcta es:', respuesta_correcta,'\n')

        #Se consulta al usuario si está seguro de proseguir con la carga:

        cargar = str(input('¿Desea cotinuar con la carga? S/N\n'))

        #Si el usuario confirma, se procede a la carga de una nueva fila en el archivo de 'Preguntas y respuestas.csv':

        if cargar.lower() == 's':

            header = ['pregunta', 'opcion_a', 'opcion_b', 'opcion_c', 'opcion_d', 'respuesta_correcta']
            csvfile = open(archivo, 'a')
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writerow(nueva_pregunta)
            csvfile.close()

        #Se consulta al usuario si desea continuar con la carga de preguntas y respuestas, en caso contrario, el programa sale de la función.

        continuar = str(input('¿Desea continuar con la carga de nuevas preguntas y respuestas? S/N'))
        if continuar == 'N' or continuar == 'n':
            break

    return


def buscar_pregunta():

    csvfile = open(archivo)
    preguntas = list(csv.DictReader(csvfile))
    csvfile.close()

    cantidad_de_preguntas = len(preguntas)

    #Selección de una pregunta al azar en la fila número "indice".
    #Se guardan la pregunta, las opciones y la respuesta en variables auxiliares.

    indice_pregunta = random.randrange(0, cantidad_de_preguntas)

    pregunta = preguntas[indice_pregunta] ['pregunta']
    opcion_a = preguntas[indice_pregunta] ['opcion_a']
    opcion_b = preguntas[indice_pregunta] ['opcion_b']
    opcion_c = preguntas[indice_pregunta] ['opcion_c']
    opcion_d = preguntas[indice_pregunta] ['opcion_d']
    rta_correcta = preguntas[indice_pregunta] ['respuesta_correcta']

    print('Pregunta:', pregunta)
    print('A)', opcion_a)
    print('B)', opcion_b)
    print('C)', opcion_c)
    print('D)', opcion_d)

    print('La cantidad de preguntas cargadas es:', cantidad_de_preguntas)

    #Selección de opción del usuario:
    print('Seleccione la opción correcta:')

    puntaje = 0

    while True:
        op_elegida = str(input())

    #Para facilitar las comparaciones, se sobreescriben las variables de opciones  y respuesta correcta como todo texto en minúscula

        op_elegida = op_elegida.lower()
        opcion_a = opcion_a.lower()
        opcion_b = opcion_b.lower()
        opcion_c = opcion_c.lower()
        opcion_d = opcion_d.lower()
        rta_correcta = rta_correcta.lower()

    #Comparación de la respuesta elegida es la correcta:

        #Si se ingresan las letras A, B, C, o D ya sea en mayúscula o minúscula se compara con la respuesta correcta.

        if (op_elegida == 'a') and (opcion_a == rta_correcta):
            puntaje = 10
            print('La opción elegida es correcta! Sumas 10 puntos')
            break

        elif (op_elegida == 'b') and (opcion_b == rta_correcta):
            puntaje = 10
            print('La opción elegida es correcta! Sumas 10 puntos')
            break

        elif (op_elegida == 'c') and (opcion_c == rta_correcta):
            puntaje = 10
            print('La opción elegida es correcta! Sumas 10 puntos')
            break

        elif (op_elegida == 'd') and (opcion_d == rta_correcta):
            puntaje = 10
            print('La opción elegida es correcta! Sumas 10 puntos')
            break

        #Se compara si el jugador ingresó la respuesta de forma escrita, si corresponde a la respuesta correcta

        elif (op_elegida == rta_correcta):
            puntaje = 10
            print('La opción elegida es correcta! Sumas 10 puntos')
            break

        #Se compara si la respuesta escogida es efectivamente A, B, C o D, pero la respuesta NO es correcta:

        elif (op_elegida == 'a') or (op_elegida == 'b') or (op_elegida == 'c') or (op_elegida == 'd'):
            print('Lo siento, la opción ingresada es incorrecta, nos sumas puntos :(')
            break

        #Si el jugador ingresa como texto la respuesta y la misma NO es la correcta:

        elif (op_elegida == opcion_a) or (op_elegida == opcion_b) or (op_elegida == opcion_c) or (op_elegida == opcion_d):
            print('Lo siento, la opción ingresada es incorrecta, nos sumas puntos :(')
            break

        #Si es jugador ingresa por teclado cualquier texto diferente de A, B, C o D o las opciones disponibles, el programa evalúa la
        #el texto ingresado como inválido solicitando que se ingrese la respuesta nuevamente.

        elif (op_elegida != opcion_a) and (op_elegida != opcion_b) and (op_elegida != opcion_c) and (op_elegida != opcion_d):
            print('La opción ingresada no es válida, por favor ingrese un valor válido')

        #La función devuelve la variable "puntaje" que valdrá 10 si la respuesta elegida fue correcta y 0 en caso contrario.
            
    return puntaje


if __name__ == '__main__':
    print("\n¡Bienvenidos a TRIVIA! ¡Juego de preguntas y respuestas!\n")

    print ('¡Trivia se puede jugar de 2 hasta 5 jugadores!\n')

    while True:

        while True:

            cantidad_jugadores = input('¿Cuántos desean jugar?\n')
            cantidad_jugadores = cantidad_jugadores.lower()

            #Si el usuario ingresa la palabra carga, ingresa a la opción de carga de una nueva pregunta y sus respectivas respuestas:
            #al finalizar cada carga de preguntas y respuestas el programa consultará si se desea continuar, en caso contrario, finalizará.

            if cantidad_jugadores == 'carga':
                agregar_preguntas()

            else:
                try:
                    cantidad_jugadores = int(cantidad_jugadores)
                except:
                    print('Por favor ingrese un número válido de jugadores')

            if cantidad_jugadores >= 2 and cantidad_jugadores <= 5:
                print('¡Perfecto!¡A jugar!')
                break
            else:
                print('Por favor ingrese una cantidad de jugadores entre 2 y 5 personas')

        x = 0
        jugadores_puntajes = {}
        ganadores = []

        while x < cantidad_jugadores:
            x += 1
            jugador = 'Jugador ' + str(x)
            jugadores_puntajes[jugador] = 0

        while True:

            for i in range(len(jugadores_puntajes)):       
                x = i+1
                jugador = 'Jugador ' + str(x)
                print('Turno del ', jugador, ':\n')
                puntaje = buscar_pregunta()
                jugadores_puntajes[jugador] = jugadores_puntajes[jugador] + puntaje
                print ('Puntajes obtenidos hasta el momento:', jugadores_puntajes, '\n')

            for i in range(len(jugadores_puntajes)):       
                x = i+1
                jugador = 'Jugador ' + str(x)
                if jugadores_puntajes[jugador] >= 30:
                    ganadores.append(jugador)

            if len(ganadores) == 1:
                print('¡Felicitaciones {} es el ganador!'.format(ganadores))
                break
            elif len(ganadores) > 1:
                print('¡Los ganadores son {}!'.format(ganadores))
                break

        continuar = str(input('¿Desea jugar nuevamente? S/N'))
        if continuar == 'N' or continuar == 'n':
            break




