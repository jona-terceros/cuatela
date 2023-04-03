from copy import deepcopy
from game import *
import os


def juego():
    print("Juego cautela")
    turno = 1
    # Una ficha = [fila,columna,nombre]
    fichas_negras = [[0, 0, "X"], [1, 1, "X"], [2, 2, "X"], [3, 3, "X"]]
    fichas_blancas = [[3, 0, "O"], [2, 1, "O"], [1, 2, "O"], [0, 3, "O"]]
    tabla = tabla_por_defecto(crear_tabla(), fichas_negras)
    tabla = tabla_por_defecto(tabla, fichas_blancas)

    human_piece = choose_piece()
    if human_piece == 'X':
        ai_piece = 'O'
    else:
        ai_piece = 'X'

    while True:
        os.system("clear")
        mostrar_tabla(tabla)
        print(tabla)  # list of lists, returns the final state

        if ai_piece == 'O':
            if turno % 2 == 0:
                print("Fichas blancas del jugador 2: IA")
                # minmax_decision(tabla, "X")
                mostrar_fichas_del_jugador(fichas_blancas)

                action_ai = alpha_beta_search(tabla)
                tabla = copy.deepcopy(action_ai)
                print(tabla)

                # print("Elección de ficha: ", FICHA_ELEGIDA_POR_IA)
                # print("Elección de Movimiento (N,S,E,O,NE,NO,SE,SO): ", MOVIMIENTO_ELEGIDO_POR_IA)
                # ficha = fichas_blancas[FICHA_ELEGIDA_POR_IA - 1]
                # fichas_blancas[numero_ficha - 1] = mover_ficha(tabla, ficha, MOVIMIENTO_ELEGIDO_POR_IA)


            else:
                # turno humano con X juega primero
                print("Fichas negras del jugador 1 Tú")
                ##minmax_decision(tabla, "O")
                mostrar_fichas_del_jugador(fichas_negras)
                numero_ficha = int(input("Elije tu ficha: "))
                movimiento = input("Elige tu Movimiento (N,S,E,O,NE,NO,SE,SO): ")
                ficha = fichas_negras[numero_ficha - 1]
                fichas_negras[numero_ficha - 1] = mover_ficha(tabla, ficha, movimiento)

        else:
            if turno % 2 == 0:
                print("Fichas blancas del jugador 2: Tú")
                # minmax_decision(tabla, "X")
                mostrar_fichas_del_jugador(fichas_blancas)
                numero_ficha = int(input("Elije tu ficha: "))
                movimiento = input("Elige tu Movimiento (N,S,E,O,NE,NO,SE,SO): ")
                ficha = fichas_blancas[numero_ficha - 1]
                fichas_blancas[numero_ficha - 1] = mover_ficha(tabla, ficha, movimiento)

            else:
                # turno ia con X
                # turno humano con X juega primero
                print("Fichas negras del jugador 1: IA")
                ##minmax_decision(tabla, "O")
                mostrar_fichas_del_jugador(fichas_negras)
                action_ai = alpha_beta_search(tabla)
                tabla = copy.deepcopy(action_ai)
                print(tabla)

                # print("Elección de ficha: ", FICHA_ELEGIDA_POR_IA)
                # print("Elección de Movimiento (N,S,E,O,NE,NO,SE,SO): ", MOVIMIENTO_ELEGIDO_POR_IA)
                # ficha = fichas_negras[FICHA_ELEGIDA_POR_IA - 1]
                # fichas_negras[numero_ficha - 1] = mover_ficha(tabla, ficha, MOVIMIENTO_ELEGIDO_POR_IA)
            # ficha = input("Insertar ficha en (fila,columna,ficha) o salir: ")
            # datos_ficha = ficha.split(sep=",")
        ''' 
        if verificar_victoria(tabla):
            if turno % 2 == 0:
                print("¡Victoria para las fichas blancas!")
            else:
                print("¡Victoria para las fichas negras!")
            break
        if verificar_victoria2(tabla):
            if turno % 2 == 0:
                print("¡Victoria para las fichas blancas!")
            else:
                print("¡Victoria para las fichas negras!")
            break
        if verificar_victoria3(tabla):
            if turno % 2 == 0:
                print("¡Victoria para las fichas blancas!")
            else:
                print("¡Victoria para las fichas negras!")
            break'''
        continuar = input("Desea Continuar (S,N): ")
        if continuar == "N":
            return False
        else:
            # tabla = insertar_en_tabla(datos_ficha,tabla)
            # print(datos_ficha)
            turno += 1


if __name__ == "__main__":
    juego()