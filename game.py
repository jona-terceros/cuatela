import math
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
        
        
# def turnoJugador(tabla, listaFichas, jugador):
#     validacion = False
#     cadenaFicha = input("Ficha --> ") 
#     ficha, movimiento = crear_ficha(cadenaFicha, jugador)
#     for i, elemento in enumerate(listaFichas):
#         if elemento == ficha:
#             iterador = i
#             validacion = True
#             break
    
#     if validacion:
#         listaFichas[iterador] = move_piece(tabla,ficha,movimiento)
#     else:
#         print("Movimiento Invalido")
#     return validacion
       
# def crear_ficha(cadena, piezaJugador):
#     datosColumna = [{'A':0},{'B':1},{'C':2},{'D':3}]
#     datosFicha = cadena.split(" ")
#     coordenadas = datosFicha[0]
#     movimiento = datosFicha[1]
#     columna = coordenadas[0]
#     fila = coordenadas[1]

#     valorColumna = columna
#     for diccionario in datosColumna:
#         if columna in diccionario:
#             valorColumna = diccionario.get(columna)
#     return [valorColumna, int(fila)-1, piezaJugador], movimiento

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


# Alpha-Betha pruning algorithm

def alpha_beta_search(table, ai_piece):
    alpha = -math.inf
    beta = math.inf
    best_action = None
    if ai_piece == 'X': #if maximaxing player
        for start_pos, end_pos in actions(table, ai_piece):
            v = min_value(result(table, start_pos, end_pos), alpha, beta, 0, 3)
            if v > alpha:
                alpha = v
                best_action = (start_pos, end_pos)
               
    else:
        for start_pos, end_pos in actions(table, ai_piece):
            v = max_value(result(table, start_pos, end_pos), alpha, beta, 0, 3)
            if v < beta:
                beta = v
                best_action = (start_pos, end_pos)  
                   

    return best_action


'''
def alpha_beta(table,  maximizing_player):
  alpha = -math.inf
  beta = math.inf
  if terminal_test(table):
      return utility(table)
  if maximizing_player:
      v = -math.inf
      for action in actions(table, ai_piece):
          v = max(v, alpha_beta(action, alpha, beta, False))
          alpha = max(alpha, v)
          if beta <= alpha:
              break
      return v
  else:
      v = math.inf
      for action in actions(table, ai_piece):
          v = min(v, alpha_beta(action, alpha, beta, True))
          beta = min(beta, v)
          if beta <= alpha:
              break
      return v
'''
def alpha_beta_pruning(table):
    maximizing_player=True
    ai_piece = choose_piece(ai_piece)
    best_action = None
    if maximizing_player:  # Maximizing player
        best_value = -math.inf
        for action in actions(table, ai_piece):
            value = min_value(result(table, action), alpha, beta,3)
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
    else:  # Minimizing player
        best_value = math.inf
        human_piece = choose_piece(human_piece)
        for action in actions(table, human_piece):
            value = max_value(result(table, action), alpha, beta,3)
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(beta, best_value)
            if beta <= alpha:
                break

    return best_action, best_value

def max_value(table, alpha, beta, depth, max_depth):
    if depth >= max_depth:
        return utility(table)
    
    ai_piece = choose_piece()
    if (terminal_test(table)):
        return utility(table)
    
    v = -math.inf
    for action in actions(table, ai_piece):
        v = max(v, min_value(result(table, action), alpha, beta, depth + 1, max_depth))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(table, alpha, beta, depth, max_depth):
    if depth >= max_depth:
        return utility(table)
    
    human_piece = choose_piece()
    if (terminal_test(table)):
        return utility(table)
    
    v = math.inf
    for action in actions(table, human_piece):
        v = min(v, max_value(result(table, action), alpha, beta, depth + 1, max_depth))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

# functions for alpha-beta def
def actions(table, ai_piece):
    res = []
    cf = [-1,-1,-1,0,0,1,1,1]
    cc = [-1,0,1,-1,1,-1,0,1]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == ai_piece:
                # Move
                f, c = i, j
                for k in range(8):
                    nf, nc = f + cf[k], c + cc[k]
                    if nf >= 0 and nf < 4 and nc >= 0 and nc < 4:
                        if table[nf][nc] == '-':
                            res.append(((i, j), (nf, nc)))
    return res

def result(board, piece, movement):
    new_board = copy.deepcopy(board)
    # Make the move on the new board
    new_board = move_piece(new_board, piece, movement)
    return new_board

def terminal_test(table):  # jugador actual #recibiria tambien el turno no
    # compureba si alguien a ganado , dudas
    if verify_victory(table):
        return True
    # if verify_victory2(table):
    #     return True
    # if verify_victory3(table):
    #     return True
    # comprueba si hay empate creo que en este juego no hay empate no termina si no hay ganador

    return False
def utility(table):
    # ganar en una fila o columna
    ai_piece = choose_piece()
    for i in range(4):
        
        if all(cell == ai_piece for cell in table[i]):
            return 1
        elif all(cell != "-" for cell in table[i]):
            return -1
        if all(cell == ai_piece for cell in [table[0][i], table[1][i], table[2][i], table[3][i]]):
            return 1
        elif all(cell != "-" for cell in [table[0][i], table[1][i], table[2][i], table[3][i]]):
            return -1
    # ganar cuatro esquinas
    if table[0][0] == ai_piece and table[0][3] == ai_piece and table[3][0] == ai_piece and table[3][3] == ai_piece:
        return 1
    # cuadrado pequeño
    for i in range(3):
        for j in range(3):
            if all(cell == ai_piece for cell in [table[i][j], table[i][j+1], table[i+1][j], table[i+1][j+1]]):
                return 1
            elif all(cell != "-" for cell in [table[i][j], table[i][j+1], table[i+1][j], table[i+1][j+1]]):
                return -1
    # no hay ganador
    return 0


# function for main
