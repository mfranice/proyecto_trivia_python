import csv
import random

archivo = 'Preguntas y respuestas.csv'

def agregar_preguntas():

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
    
    nueva_pregunta = {'pregunta': pregunta, 'opcion_a': opcion_a, 'opcion_b': opcion_b, 'opcion_c': opcion_c, 'opcion_d': opcion_d, 'respuesta_correcta': respuesta_correcta}

    
    
    header = ['pregunta', 'opcion_a', 'opcion_b', 'opcion_c', 'opcion_d', 'respuesta_correcta']
    csvfile = open(archivo, 'a')
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writerow(nueva_pregunta)
    csvfile.close()


def buscar_pregunta ():

    csvfile = open(archivo)
    preguntas = list(csv.DictReader(csvfile))
    csvfile.close()

    cantidad_de_preguntas = 0

    for pregunta in preguntas:
        cantidad_de_preguntas += 1

    indice_pregunta = random.randrange(0, cantidad_de_preguntas)
#    pregunta_elegida = {}
#    pregunta_elegida = preguntas[indice_pregunta]

    print(preguntas[indice_pregunta] ['pregunta'])
    print(preguntas[indice_pregunta] ['opcion_a'])
    print(preguntas[indice_pregunta] ['opcion_b'])
    print(preguntas[indice_pregunta] ['opcion_c'])
    print(preguntas[indice_pregunta] ['opcion_d'])

    print('La cantidad de preguntas cargadas es:', cantidad_de_preguntas)

#    if preguntas[indice_pregunta] ['opcion_a'] == preguntas[indice_pregunta] ['respuesta_correcta']:
#        opcion_correcta = 'a'
#    elif preguntas[indice_pregunta] ['opcion_b'] == preguntas[indice_pregunta] ['respuesta_correcta']:
#        opcion_correcta = 'b'
#    elif preguntas[indice_pregunta] ['opcion_c'] == preguntas[indice_pregunta] ['respuesta_correcta']:
#        opcion_correcta = 'c'
#    elif preguntas[indice_pregunta] ['opcion_d'] == preguntas[indice_pregunta] ['respuesta_correcta']:
#        opcion_correcta = 'd'


    print('Seleccione la opción correcta:')

    puntaje = 0

    while True:
        op_elegida = str(input())
        if (op_elegida == 'a') or (op_elegida == 'b') or (op_elegida == 'c') or (op_elegida == 'd') or (op_elegida == 'A') or (op_elegida == 'B') or (op_elegida == 'C') or (op_elegida == 'D'):
            break
        else:
            print('La opción ingresada no es válida, por favor ingrese las opciones A, B, C o D de acuerdo considere la opción correcta.')


    if (op_elegida == 'a') and (preguntas[indice_pregunta] ['opcion_a'] == preguntas[indice_pregunta] ['respuesta_correcta']):
        puntaje = 10
        print('La opción elegida es correcta! Sumas 10 puntos')

    elif (op_elegida == 'b') and (preguntas[indice_pregunta] ['opcion_b'] == preguntas[indice_pregunta] ['respuesta_correcta']):
        puntaje = 10
        print('La opción elegida es correcta! Sumas 10 puntos')

    elif (op_elegida == 'c') and (preguntas[indice_pregunta] ['opcion_c'] == preguntas[indice_pregunta] ['respuesta_correcta']):
        puntaje = 10
        print('La opción elegida es correcta! Sumas 10 puntos')

    elif (op_elegida == 'd') and (preguntas[indice_pregunta] ['opcion_d'] == preguntas[indice_pregunta] ['respuesta_correcta']):
        puntaje = 10
        print('La opción elegida es correcta! Sumas 10 puntos')

    return puntaje



if __name__ == '__main__':
    print("¡Bienvenidos a TRIVIA! ¡Juego de preguntas y respuestas!")
#    agregar_preguntas()
#    modificar_datos()

    print ('¡Ingrese entrar para comenzar a jugar!')

#ingresar cantidad de juegadores? o preguntar los nombres y al finalizar cada uno consultar
#si desea agregar uno más?
#Generar lista de jugadores, después para saber cuantos son puedo medir la longitud
    while True:
        #agregar_preguntas()
        print('Desea continuar S/N:')
        continuar = str(input())
        if continuar == 'N' or continuar == 'n':
            break

        puntaje = buscar_pregunta()

        print('Su puntaje es:', puntaje)

        


#    question = buscar_pregunta()
#    print(question['pregunta'])
#    print('A) ', question['opcion_a'])
#    print('B) ', question['opcion_b'])
#    print('C) ', question['opcion_c'])
#    print('D) ', question['opcion_d'])