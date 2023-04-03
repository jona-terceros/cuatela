import copy  
from game import *
import os


def game():
    print("GAME CUATELA")
    turn = 1
    # Una ficha = [fila,columna,nombre]
    black_piece = [[0, 0, "X"], [1, 1, "X"], [2, 2, "X"], [3, 3, "X"]]
    white_piece = [[3, 0, "O"], [2, 1, "O"], [1, 2, "O"], [0, 3, "O"]]
    board = default_board(create_board(), black_piece)
    board = default_board(board, white_piece)

    human_piece = choose_piece()
    if human_piece == 'X':
        ai_piece = 'O'
    else:
        ai_piece = 'X'

    while True:
        os.system("clear")
        show_board(board)
        if ai_piece == 'O':
            if turn % 2 == 0:
                print("Player 2 White chips: AI")
                show_players_piece(black_piece)

                ai_piece = 'O'  # the AI always plays with the black tiles
                action_ai = alpha_beta_search(board, ai_piece)
                print(action_ai)
                if copy.deepcopy(action_ai) != None:
                    board = copy.deepcopy(action_ai)

                #print(board)  # show board here
                # print("Elección de ficha: ", FICHA_ELEGIDA_POR_IA)
                # print("Elección de Movimiento (N,S,E,O,NE,NO,SE,SO): ", MOVIMIENTO_ELEGIDO_POR_IA)
                # ficha = white_piece[FICHA_ELEGIDA_POR_IA - 1]
                # white_piece[piece_number - 1] = move_piece(board, ficha, MOVIMIENTO_ELEGIDO_POR_IA)


            else:
                # turn Human with X play first
                print("Black pieces of player 1 You")
                ##minmax_decision(board, "O")
                show_players_piece(black_piece)
                piece_number = int(input("Choose your piece: "))
                movement = input("Choose your Movement (N,S,E,O,NE,NO,SE,SO): ")
                piece = black_piece[piece_number - 1]
                black_piece[piece_number - 1] = move_piece(board, piece, movement)
                 
                # validacion = False
                # while validacion != True:
                #     print("Jugador: tu")
                #     print("Movimientos (N,S,E,O,NE,NO,SE,SO): Ejm C2 NE")
                #     validacion = turnJugador(board,black_piece, 'X')

        else:
            if turn % 2 == 0:
                print("Fichas blancas del jugador 2: Tú")
                show_players_piece(white_piece)
                piece_number = int(input("Choose your piece: "))
                movement = input("Choose your Movement (N,S,E,O,NE,NO,SE,SO): ")
                piece = white_piece[piece_number - 1]
                white_piece[piece_number - 1] = move_piece(board, piece, movement)
                
                
                
                # validacion = False
                # while validacion != True:
                    
                #     print("Jugador: tu")
                #     print("Movimientos (N,S,E,O,NE,NO,SE,SO): Ejm C2 NE")
                #     validacion = turnJugador(board,black_piece, 'X')
                
            else:
                # turn ia con X
                # turn humano con X juega primero
                print("Fichas negras del jugador 1: IA")
                ai_piece = choose_piece()
                show_players_piece(black_piece)
                action_ai = alpha_beta_search(board, ai_piece)
                print(action_ai)
                move_piece(board, ai_piece, action_ai)  # actualizar ficha en el tablero
 
                # board = copy.deepcopy(action_ai)
                # print(board)

                # print("Elección de ficha: ", FICHA_ELEGIDA_POR_IA)
                # print("Elección de Movimiento (N,S,E,O,NE,NO,SE,SO): ", MOVIMIENTO_ELEGIDO_POR_IA)
                # ficha = black_piece[FICHA_ELEGIDA_POR_IA - 1]
                # black_piece[piece_number - 1] = move_piece(board, ficha, MOVIMIENTO_ELEGIDO_POR_IA)
            # ficha = input("Insertar ficha en (fila,columna,ficha) o salir: ")
            # datos_ficha = ficha.split(sep=",")
        ''' 
        if verificar_victoria(board):
            if turn % 2 == 0:
                print("¡Victoria para las fichas blancas!")
            else:
                print("¡Victoria para las fichas negras!")
            break
        if verificar_victoria2(board):
            if turn % 2 == 0:
                print("¡Victoria para las fichas blancas!")
            else:
                print("¡Victoria para las fichas negras!")
            break
        if verificar_victoria3(board):
            if turn % 2 == 0:
                print("¡Victoria para las fichas blancas!")
            else:
                print("¡Victoria para las fichas negras!")
            break'''
            
        continuar = input("Do you wish to continue? (Y,N): ")
        if continuar == "N":
            return False
        else:
            turn += 1


if __name__ == "__main__":
    game()