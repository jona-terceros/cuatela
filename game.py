import sys
sys.setrecursionlimit(10000)

import copy
def crear_tabla():
    tabla = [["-", "-", "-", "-"],
             ["-", "-", "-", "-"],
             ["-", "-", "-", "-"],
             ["-", "-", "-", "-"], ]
    return tabla


def mostrar_tabla(tabla):
    for fila in tabla:
        print(fila)


def formato_ficha(ficha):
    columna = int(ficha[0])
    fila = int(ficha[1])
    nombre_ficha = ficha[2]
    return [columna, fila, nombre_ficha]


def insertar_en_tabla(datos_ficha, tabla):
    columna = int(datos_ficha[0])
    fila = int(datos_ficha[1])
    ficha = datos_ficha[2]

    tabla[columna][fila] = ficha
    return tabla


def tabla_por_defecto(tabla, lista_Fichas):
    for ficha in lista_Fichas:
        tabla = insertar_en_tabla(ficha, tabla)
    return tabla


def mostrar_fichas_del_jugador(lista_fichas):
    contador = 1
    for ficha in lista_fichas:
        print(f"Ficha {contador}: ({ficha[0]},{ficha[1]})")
        contador += 1


def limite_matriz(fila, columna):
    if fila < 0 or fila > 3 or columna < 0 or columna > 3:
        return False
    else:
        return True


def mover_ficha(tabla, ficha, movimiento):
    nueva_ficha = ficha
    if (movimiento == "N"):  # Arriba
        i = 1
        while limite_matriz(ficha[0] - i, ficha[1]) and tabla[ficha[0] - i][ficha[1]] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] - i + 1, ficha[1], ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)
        else:
            print("Movimiento invalido")
    if (movimiento == "E"):  # derecha
        i = 1
        while limite_matriz(ficha[0], ficha[1] + i) and tabla[ficha[0]][ficha[1] + i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0], ficha[1] + i - 1, ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)
        else:
            print("Movimiento invalido")
    if (movimiento == "S"):  # Abajo
        i = 1
        while limite_matriz(ficha[0] + i, ficha[1]) and tabla[ficha[0] + i][ficha[1]] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] + i - 1, ficha[1], ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)
        else:
            print("Movimiento invalido")
    if (movimiento == "O"):  # izquierda
        i = 1
        while limite_matriz(ficha[0], ficha[1] - i) and tabla[ficha[0]][ficha[1] - i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0], ficha[1] - i + 1, ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)
        else:
            print("Movimiento invalido")
    if (movimiento == "NE"):  # Diagonal superior derecha
        i = 1
        while limite_matriz(ficha[0] - i, ficha[1] + i) and tabla[ficha[0] - i][ficha[1] + i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] - (i - 1), ficha[1] + (i - 1), ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)

    if (movimiento == "SE"):  # Sur Este, Diagonal inferior derecha
        i = 1
        while limite_matriz(ficha[0] + i, ficha[1] + i) and tabla[ficha[0] + i][ficha[1] + i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] + (i - 1), ficha[1] + (i - 1), ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)

    if (movimiento == "SO"):  # Diagonal inferior izquierda
        i = 1
        while limite_matriz(ficha[0] + i, ficha[1] - i) and tabla[ficha[0] + i][ficha[1] - i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] + (i - 1), ficha[1] - (i - 1), ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)

    if (movimiento == "NO"):  # Diagonal superior izquierda
        i = 1
        while limite_matriz(ficha[0] - i, ficha[1] - i) and tabla[ficha[0] - i][ficha[1] - i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] - (i - 1), ficha[1] - (i - 1), ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)
    return nueva_ficha


def verificar_victoria(tabla):
    esquina_superior_izquierda = tabla[0][0]
    esquina_superior_derecha = tabla[0][3]
    esquina_inferior_izquierda = tabla[3][0]
    esquina_inferior_derecha = tabla[3][3]

    if esquina_superior_izquierda != "-" and esquina_superior_izquierda == esquina_superior_derecha == esquina_inferior_izquierda == esquina_inferior_derecha:
        return True
    else:
        return False


def verificar_victoria2(tabla):
    # fila
    for fila in tabla:
        if all(celda == fila[0] and celda != "-" for celda in fila):
            return True

    # columna
    for j in range(4):
        if all(tabla[i][j] == tabla[0][j] and tabla[i][j] != "-" for i in range(4)):
            return True
    return False


def verificar_victoria3(tabla):
    if tabla[0][0] != "-" and tabla[0][0] == tabla[0][1] == tabla[1][0] == tabla[1][1]:
        return True
    if tabla[0][1] != "-" and tabla[0][1] == tabla[0][2] == tabla[1][1] == tabla[1][2]:
        return True
    if tabla[0][2] != "-" and tabla[0][2] == tabla[0][3] == tabla[1][2] == tabla[1][3]:
        return True
    if tabla[1][0] != "-" and tabla[1][0] == tabla[1][1] == tabla[2][0] == tabla[2][1]:
        return True
    if tabla[1][1] != "-" and tabla[1][1] == tabla[1][2] == tabla[2][1] == tabla[2][2]:
        return True
    if tabla[1][2] != "-" and tabla[1][2] == tabla[1][3] == tabla[2][2] == tabla[2][3]:
        return True
    if tabla[2][0] != "-" and tabla[2][0] == tabla[2][1] == tabla[3][0] == tabla[3][1]:
        return True
    if tabla[2][1] != "-" and tabla[2][1] == tabla[2][2] == tabla[3][1] == tabla[3][2]:
        return True
    if tabla[2][2] != "-" and tabla[2][2] == tabla[2][3] == tabla[3][2] == tabla[3][3]:
        return True

    return False


def utility(table, player_ai):
    values_list = []

    cant_O_corners = 0
    cant_X_corners = 0

    # ---------------- count those aligned horizontally-------------------
    rows = len(table)
    col = len(table[0])

    # initialize count lists to zero
    cont_O = [0] * rows
    cont_X = [0] * rows

    # count the number of X's and O's in each row of the board
    for i in range(rows):
        for j in range(col):
            if table[i][j] == "O":
                cont_O[i] += 1
            elif table[i][j] == "X":
                cont_X[i] += 1
    # obtain the best value
    if player_ai == 'X':
        best = max(cont_X)
        values_list.append(best)
    else:
        best = max(cont_O)
        values_list.append(best)

    # ---------------- count those aligned vertically-------------------
    cont_O = [0] * col
    cont_X = [0] * col
    for i in range(rows):
        for j in range(col):
            if table[i][j] == "O":
                cont_O[j] += 1
            elif table[i][j] == "X":
                cont_X[j] += 1
    # obtain the best value
    if player_ai == 'X':
        best = max(cont_X)
        values_list.append(best)
    else:
        best = max(cont_O)
        values_list.append(best)

    # --------------------------- corners ----------------------------
    if table[0][0] == "O":
        cant_O_corners += 1
    elif table[0][0] == "X":
        cant_X_corners += 1

    if table[0][-1] == "O":
        cant_O_corners += 1
    elif table[0][-1] == "X":
        cant_X_corners += 1

    if table[-1][0] == "O":
        cant_O_corners += 1
    elif table[-1][0] == "X":
        cant_X_corners += 1

    if table[-1][-1] == "O":
        cant_O_corners += 1
    elif table[-1][-1] == "X":
        cant_X_corners += 1

    # append to value list
    if player_ai == 'X':
        values_list.append(cant_X_corners)
    else:
        values_list.append(cant_O_corners)

    # ------------------------------------ square ----------------------------------------

    list_of_lists_O = [[0 for j in range(col - 1)] for i in range(rows - 1)]
    list_of_lists_X = [[0 for j in range(col - 1)] for i in range(rows - 1)]

    for i in range(rows - 1):
        for j in range(col - 1):
            subtable = [[table[i][j], table[i][j + 1]],
                        [table[i + 1][j], table[i + 1][j + 1]]]
            num_O = sum(row.count("O") for row in subtable)
            num_X = sum(row.count("X") for row in subtable)
            list_of_lists_O[i][j] = num_O
            list_of_lists_X[i][j] = num_X
    # inspired by: https://es.stackoverflow.com/questions/461876/
    # append to value list
    if player_ai == 'X':
        best = max(max(i) for i in list_of_lists_X)
        values_list.append(best)
    else:
        best = max(max(i) for i in list_of_lists_O)
        values_list.append(best)

    rep_2 = values_list.count(2)
    rep_3 = values_list.count(3)
    max_value = max(values_list)

    if rep_2 == 2:
        max_value += 1
    if rep_2 == 3:
        max_value += 2
    if rep_3 == 2:
        max_value += 3
    if rep_3 == 3:
        max_value += 4
    return max_value


import math

memo = []
max_depth = 20


def alpha_beta_pruning(table):
    global memo
    maximizing_player = True
    alpha = -math.inf
    beta = math.inf
    best_action = None
    memo = [-1] * (3 ** 17 + 10)
    if maximizing_player:  # Maximizing player
        best_value = -math.inf
        for action in actions(table, ai_piece):
            value = min_value(result(table, action), 0, ai_piece, alpha, beta)
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
    else:
        best_value = math.inf
        for action in actions(table, ai_piece):
            value = max_value(result(table, action), 0, ai_piece, alpha, beta)
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(beta, best_value)
            if beta <= alpha:
                break

    return best_action, best_value


def get_id_of_table(table):
    result = 0
    for i in range(4):
        for j in range(4):
            if table[i][j] == 'X':
                result += (3 ** (i * 4 + j))
            elif table[i][j] == 'O':
                result += 2 * (3 ** (i * 4 + j))
    return result


def max_value(table, depth, piece, alpha, beta):
    global memo
    id = get_id_of_table(table)
    if depth > max_depth:
        memo[id] = utility(table, piece)
        return memo[id]
    if memo[id] != -1:
        return memo[id]
    if (terminal_test(table)):
        memo[id] = utility(table, piece)
        return memo[id]

    v = -math.inf
    for action in actions(table, piece):
        if piece == ai_piece:
            v = max(v, min_value(action, depth + 1, human_piece, alpha, beta))
        else:
            v = max(v, min_value(action, depth + 1, ai_piece, alpha, beta))
        if v >= beta:
            memo[id] = v
            return memo[id]
        alpha = max(alpha, v)
    memo[id] = v
    return memo[id]


def min_value(table, depth, piece, alpha, beta):
    global memo
    id = get_id_of_table(table)
    if depth > max_depth:
        memo[id] = utility(table, piece)
        return memo[id]
    if memo[id] != -1:
        return memo[id]
    if (terminal_test(table)):
        memo[id] = utility(table, piece)
        return memo[id]

    v = math.inf
    for action in actions(table, piece):
        if piece == ai_piece:
            v = min(v, max_value(action, depth + 1, human_piece, alpha, beta))
        else:
            v = min(v, max_value(action, depth + 1, ai_piece, alpha, beta))
        if v <= alpha:
            memo[id] = v
            return memo[id]
        beta = min(beta, v)
    memo[id] = v
    return memo[id]


def result(table, action):
    table = copy.deepcopy(action)
    return table


def terminal_test(table):  # jugador actual #recibiria tambien el turno no
    # compureba si alguien a ganado , dudas
    if verificar_victoria(table):
        return True
    if verificar_victoria2(table):
        return True
    if verificar_victoria3(table):
        return True
    # comprueba si hay empate creo que en este juego no hay empate no termina si no hay ganador

    return False


def choose_piece():
    piece = input("¿Qué ficha deseas jugar? (X / O): ").upper()
    while piece != 'X' and piece != 'O':
        piece = input("Ingresa una opción válida. ¿Qué ficha deseas jugar? (X / O): ").upper()
    return piece


from copy import deepcopy
# from game import *
import os

human_piece = choose_piece()
if human_piece == 'X':
    ai_piece = 'O'
else:
    ai_piece = 'X'

import copy

human_piece = choose_piece()
if human_piece == 'X':
    ai_piece = 'O'
else:
    ai_piece = 'X'

fichas_negras = [[0, 0, "X"], [1, 1, "X"], [2, 2, "X"], [3, 3, "X"]]
fichas_blancas = [[3, 0, "O"], [2, 1, "O"], [1, 2, "O"], [0, 3, "O"]]
tabla = tabla_por_defecto(crear_tabla(), fichas_negras)
tabla = tabla_por_defecto(tabla, fichas_blancas)
mostrar_tabla(tabla)

cf = [-1, -1, 0, 1, 1, 1, 0, -1]
cc = [0, 1, 1, 1, 0, -1, -1, -1]


def actions(tabla, piece):
    res = []
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if tabla[i][j] == piece:
                for k in range(8):
                    nf, nc = i + cf[k], j + cc[k]
                    if 0 <= nf < len(tabla) and 0 <= nc < len(tabla[i]) and tabla[nf][nc] == '-':
                        new_tabla = copy.deepcopy(tabla)
                        new_tabla[i][j] = '-'
                        new_tabla[nf][nc] = piece
                        res.append(new_tabla)
    return res


juego = True
while juego == True:

    if ai_piece == 'O':
        print("Fichas negras del jugador 1 Tú")
        ##minmax_decision(tabla, "O")
        mostrar_fichas_del_jugador(fichas_negras)
        numero_ficha = int(input("Elije tu ficha: "))
        movimiento = input("Elige tu Movimiento (N,S,E,O,NE,NO,SE,SO): ")
        ficha = fichas_negras[numero_ficha - 1]
        fichas_negras[numero_ficha - 1], tabla = mover_ficha(tabla, ficha, movimiento)
        mostrar_tabla(tabla)

        print("Fichas blancas del jugador 2: IA")
        # minmax_decision(tabla, "X")
        mostrar_fichas_del_jugador(fichas_blancas)
        action_ai, value = alpha_beta_pruning(tabla)
        tabla = []
        tabla = copy.deepcopy(action_ai)
        mostrar_tabla(tabla)



    else:
        # turno ia con X
        # turno humano con X juega primero
        print("Fichas negras del jugador 1: IA")
        ##minmax_decision(tabla, "O")
        mostrar_fichas_del_jugador(fichas_negras)
        action_ai, value = alpha_beta_pruning(tabla)
        tabla = []
        tabla = copy.deepcopy(action_ai)
        mostrar_tabla(tabla)

        print("Fichas blancas del jugador 2: Tú")
        # minmax_decision(tabla, "X")
        mostrar_fichas_del_jugador(fichas_blancas)
        numero_ficha = int(input("Elije tu ficha: "))
        movimiento = input("Elige tu Movimiento (N,S,E,O,NE,NO,SE,SO): ")
        ficha = fichas_blancas[numero_ficha - 1]
        fichas_blancas[numero_ficha - 1], tabla = mover_ficha(tabla, ficha, movimiento)
        mostrar_tabla(tabla)

    if verificar_victoria(tabla) == True or verificar_victoria2(tabla) == True or verificar_victoria3(tabla) == True:
        print('el juego ha terminado')
        juego = False
    else:
        continuar = input("Desea Continuar (S,N): ")
        if continuar == "N":
            juego = False
        else:
            juego = True