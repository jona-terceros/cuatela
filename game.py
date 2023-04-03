import sys
sys.setrecursionlimit(10000)
import copy

def create_board():
    board = [["_","_","_","_"],
             ["_","_","_","_"],
             ["_","_","_","_"],
             ["_","_","_","_"],]
    return board


def show_board(board):
    print("    A   B   C   D ")
    print("  +---+---+---+---+")
    for i in range(4):
        print(str(i+1) + " | " + " | ".join(board[i]) + " |")
        print("  +---+---+---+---+")
        

def piece_format(piece):
    column = int(piece[0])
    row = int(piece[1])
    piece_name = piece[2]
    return [column, row, piece_name]

def insert_into_table(piece_data, table):
    column = int(piece_data[0])
    row = int(piece_data[1])
    piece = piece_data[2]

    table[column][row] = piece
    return table

def default_board(table,piece_list):
    for piece in piece_list:
        table = insert_into_table(piece,table)
    return table

def show_players_piece(piece_list):
    counter = 1
    for piece in piece_list:
        print(f"Piece {counter}: ({piece[0]},{piece[1]})")
        counter += 1

def matrix_limit(row, column):
    if row < 0 or row > 3 or column < 0 or column > 3:
        return False 
    else:
        return True
def choose_piece():
    piece=None
    if piece:
        return piece
    return "O"

def move_piece(table, piece, movement):
    new_piece = piece
    if (movement == "N"):  # Up
        i = 1
        while matrix_limit(piece[0]-i, piece[1]) and table[piece[0]-i][piece[1]] == "_":
            i += 1
        if i > 1:
            new_piece = [piece[0]-i+1, piece[1], piece[2]]
            table = insert_into_table([piece[0], piece[1], "_"], table)
            table = insert_into_table(new_piece, table)
        else:
            print("Invalid movement")
    if (movement == "E"):  # Right
        i = 1
        while matrix_limit(piece[0], piece[1]+i) and table[piece[0]][piece[1]+i] == "_":
            i += 1
        if i > 1:
            new_piece = [piece[0], piece[1]+i-1, piece[2]]
            table = insert_into_table([piece[0], piece[1], "_"], table)
            table = insert_into_table(new_piece, table)
        else:
            print("Invalid movement")
    if (movement == "S"):  # Down
        i = 1
        while matrix_limit(piece[0]+i, piece[1]) and table[piece[0]+i][piece[1]] == "_":
            i += 1
        if i > 1:
            new_piece = [piece[0]+i-1, piece[1], piece[2]]
            table = insert_into_table([piece[0], piece[1], "_"], table)
            table = insert_into_table(new_piece, table)
        else:
            print("Invalid movement")
    if (movement == "O"):  # Left
        i = 1
        while matrix_limit(piece[0], piece[1]-i) and table[piece[0]][piece[1]-i] == "_":
            i += 1
        if i > 1:
            new_piece = [piece[0], piece[1]-i+1, piece[2]]
            table = insert_into_table([piece[0], piece[1], "_"], table)
            table = insert_into_table(new_piece, table)
        else:
            print("Invalid movement")
    if (movement == "NE"):  # Upper right diagonal
        i = 1
        while matrix_limit(piece[0]-i, piece[1]+i) and table[piece[0]-i][piece[1]+i] == "_":
            i += 1
        if i > 1:
            new_piece = [piece[0]-(i-1), piece[1]+(i-1), piece[2]]
            table = insert_into_table([piece[0], piece[1], "_"], table)
            table = insert_into_table(new_piece, table)

    if (movement == "SE"):  # Lower right diagonal
        i = 1
        while matrix_limit(piece[0]+i, piece[1]+i) and table[piece[0]+i][piece[1]+i] == "_":
            i += 1
        if i > 1:
            new_piece = [piece[0]+(i-1), piece[1]+(i-1), piece[2]]
            table = insert_into_table([piece[0], piece[1], "_"], table)
            table = insert_into_table(new_piece, table)

    if (movement == "SO"): # Lower left diagonal
        i = 1
        while matrix_limit(piece[0] + i, piece[1] - i) and table[piece[0] + i][piece[1] - i] == "_":
            i += 1
        if i > 1:
            new_piece = [piece[0] + (i-1), piece[1] - (i-1), piece[2]]
            table = insert_into_table([piece[0], piece[1], "_"], table)
            table = insert_into_table(new_piece, table)

    if (movement == "NO"): # Upper left diagonal
        i = 1
        while matrix_limit(piece[0] - i, piece[1] - i) and table[piece[0] - i][piece[1] - i] == "_":
            i += 1
        if i > 1:
            new_piece = [piece[0] - (i-1), piece[1] - (i-1), piece[2]]
            table = insert_into_table([piece[0], piece[1], "_"], table)
            table = insert_into_table(new_piece, table)

    return new_piece


def verify_victory(table):
    if type(table) is not list:
        return False

    if table[0][0] != "-" and table[0][0] == table[0][3] == table[3][0] == table[3][3]:
        return True
    else:
        return False

def verify_victory2(table):
    # row
    for row in table:
        if isinstance(row, list) and all(cell == row[0] and cell != "-" for cell in row):
            return True

    # column
    for j in range(4):
        if all(table[i][j] == table[0][j] and table[i][j] != "-" for i in range(4)):
            return True
    return False


def verify_victory3(table):
    
    if table[0][0] != "-" and table[0][0] == table[0][1] == table[1][0] == table[1][1]:
        return True
    if table[0][1] != "-" and table[0][1] == table[0][2] == table[1][1] == table[1][2]:
        return True
    if table[0][2] != "-" and table[0][2] == table[0][3] == table[1][2] == table[1][3]:
        return True
    if table[1][0] != "-" and table[1][0] == table[1][1] == table[2][0] == table[2][1]:
        return True
    if table[1][1] != "-" and table[1][1] == table[1][2] == table[2][1] == table[2][2]:
        return True
    if table[1][2] != "-" and table[1][2] == table[1][3] == table[2][2] == table[2][3]:
        return True
    if table[2][0] != "-" and table[2][0] == table[2][1] == table[3][0] == table[3][1]:
        return True
    if table[2][1] != "-" and table[2][1] == table[2][2] == table[3][1] == table[3][2]:
        return True
    if table[2][2] != "-" and table[2][2] == table[2][3] == table[3][2] == table[3][3]:
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
    if verify_victory(table):
        return True
    if verify_victory2(table):
        return True
    if verify_victory3(table):
        return True
    # comprueba si hay empate creo que en este juego no hay empate no termina si no hay ganador

    return False

<<<<<<< HEAD
=======
def actions(table, piece):
  res = []
  cf = [-1, -1, -1, 0, 0, 1, 1, 1]
  cc = [-1, 0, 1, -1, 1, -1, 0, 1]

  for i in range(len(table)):
    for j in range(len(table[i])):
      if table[i][j]==piece:
        # Mueves
        f, c = i,j
        c_table = copy.deepcopy(table)
        for k in range(8):
          nf, nc = f + cf[k], c + cc[k]
          if nf>=0 and nf<4 and nc>=0 and nc<4:
            if c_table[nf][nc]=='_':
              c_table[f][c]='_'
              c_table[nf][nc] = piece
              res.append(c_table)
  return res # devuelve una lista de matrices que son las acciones

>>>>>>> 53362cc2578da408240ce18e8bb90cfec9da79d8

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
<<<<<<< HEAD

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
                    while 0 <= nf < len(tabla) and 0 <= nc < len(tabla[i]) and tabla[nf][nc] == '-':
                        new_tabla = copy.deepcopy(tabla)
                        new_tabla[i][j] = '-'
                        new_tabla[nf][nc] = piece
                        res.append(new_tabla)
                        nf, nc = nf + cf[k], nc + cc[k]
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
    else:
        continuar = input("Desea Continuar (S,N): ")
=======
    
def game():
    print("GAME CUATELA")
    turn = 1
    # Una ficha = [fila,columna,nombre]
    black_piece = [[0, 0, "X"], [1, 1, "X"], [2, 2, "X"], [3, 3, "X"]]
    white_piece = [[3, 0, "O"], [2, 1, "O"], [1, 2, "O"], [0, 3, "O"]]
    board = default_board(create_board(), black_piece)
    board = default_board(board, white_piece)

    while True:
        os.system("clear")
        show_board(board)
        if ai_piece == 'O':
            if turn % 2 == 0:
                print("Fichas blancas del jugador 2: Tú")  
      
                show_players_piece(black_piece)
                action_ai = alpha_beta_pruning(board)
                move_piece(board, ai_piece, action_ai)  


            else:
                # turn Human with X play first
                    print("Black pieces of player 1 You")
                    ##minmax_decision(board, "O")
                    show_players_piece(black_piece)
                    piece_number = int(input("Choose your piece: "))
                    movement = input("Choose your Movement (N,S,E,O,NE,NO,SE,SO): ")
                    piece = black_piece[piece_number - 1]
                    black_piece[piece_number - 1] = move_piece(board, piece, movement)

        else:
            if turn % 2 == 0:
                print("Fichas blancas del jugador 2: Tú")
                show_players_piece(black_piece)
                action_ai = alpha_beta_pruning(board)
                #print(action_ai)
                move_piece(board, ai_piece, action_ai)  

            else:
                # turn ia con X
                # turn humano con X juega primero
                print("Fichas blancas del jugador 2: Tú")
                show_players_piece(white_piece)
                piece_number = int(input("Choose your piece: "))
                movement = input("Choose your Movement (N,S,E,O,NE,NO,SE,SO): ")
                piece = white_piece[piece_number - 1]
                white_piece[piece_number - 1] = move_piece(board, piece, movement)

        continuar = input("Do you wish to continue? (Y,N): ")
>>>>>>> 53362cc2578da408240ce18e8bb90cfec9da79d8
        if continuar == "N":
            juego = False
        else:
<<<<<<< HEAD
            juego = True
=======
            turn += 1


if __name__ == "__main__":
    game()

>>>>>>> 53362cc2578da408240ce18e8bb90cfec9da79d8
