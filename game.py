import math

def crear_tabla():
    tabla = [["-","-","-","-"],
             ["-","-","-","-"],
             ["-","-","-","-"],
             ["-","-","-","-"],]
    return tabla

def mostrar_tabla(tabla):
    for fila in tabla:
        print(fila)

def formato_ficha(ficha):
    columna = int(ficha[0])
    fila = int(ficha[1])
    nombre_ficha = ficha[2]
    return [columna,fila,nombre_ficha]

def insertar_en_tabla(datos_ficha,tabla):
    columna = int(datos_ficha[0])
    fila = int(datos_ficha[1])
    ficha = datos_ficha[2]

    tabla[columna][fila] = ficha
    return tabla

def tabla_por_defecto(tabla,lista_Fichas):
    for ficha in lista_Fichas:
        tabla = insertar_en_tabla(ficha,tabla)
    return tabla

def mostrar_fichas_del_jugador(lista_fichas):
    contador = 1
    for ficha in lista_fichas:
        print(f"Ficha {contador}: ({ficha[0]},{ficha[1]})")
        contador += 1

def limite_matriz(fila,columna):
    if fila < 0 or fila > 3 or columna < 0 or columna > 3:
        return False
    else:
        return True

def mover_ficha(tabla,ficha,movimiento):
    nueva_ficha=ficha
    if (movimiento == "N"): # Arriba
        i = 1
        while limite_matriz(ficha[0]-i,ficha[1]) and tabla[ficha[0]-i][ficha[1]] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0]-i+1,ficha[1],ficha[2]]
            tabla = insertar_en_tabla([ficha[0],ficha[1],"-"],tabla)
            tabla = insertar_en_tabla(nueva_ficha,tabla)
        else:
            print("Movimiento invalido")
    if (movimiento == "E"): # derecha
        i=1
        while limite_matriz(ficha[0],ficha[1]+i) and tabla[ficha[0]][ficha[1]+i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0],ficha[1]+i-1,ficha[2]]
            tabla = insertar_en_tabla([ficha[0],ficha[1],"-"],tabla)
            tabla = insertar_en_tabla(nueva_ficha,tabla)
        else:
            print("Movimiento invalido")
    if (movimiento == "S"): # Abajo
        i = 1
        while limite_matriz(ficha[0]+i,ficha[1]) and tabla[ficha[0]+i][ficha[1]] == "-":
             i += 1
        if i > 1:
            nueva_ficha = [ficha[0]+i-1,ficha[1],ficha[2]]
            tabla = insertar_en_tabla([ficha[0],ficha[1],"-"],tabla)
            tabla = insertar_en_tabla(nueva_ficha,tabla)
        else:
            print("Movimiento invalido")
    if (movimiento == "O"): # izquierda
        i = 1
        while limite_matriz(ficha[0],ficha[1]-i) and tabla[ficha[0]][ficha[1]-i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0],ficha[1]-i+1,ficha[2]]
            tabla = insertar_en_tabla([ficha[0],ficha[1],"-"],tabla)
            tabla = insertar_en_tabla(nueva_ficha,tabla)
        else:
            print("Movimiento invalido")
    if (movimiento == "NE"):  # Diagonal superior derecha
        i = 1
        while limite_matriz(ficha[0] - i, ficha[1] + i) and tabla[ficha[0] - i][ficha[1] + i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] - (i-1), ficha[1] + (i-1), ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)

    if (movimiento == "SE"):  # Sur Este, Diagonal inferior derecha
        i = 1
        while limite_matriz(ficha[0] + i, ficha[1] + i) and tabla[ficha[0] + i][ficha[1] + i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] + (i -1), ficha[1] + (i-1), ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)

    if (movimiento == "SO"):  # Diagonal inferior izquierda
        i = 1
        while limite_matriz(ficha[0] + i, ficha[1] - i) and tabla[ficha[0] + i][ficha[1] - i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] + (i-1), ficha[1] - (i-1), ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)

    if (movimiento == "NO"):  # Diagonal superior izquierda
        i = 1
        while limite_matriz(ficha[0] - i, ficha[1] - i) and tabla[ficha[0] - i][ficha[1] - i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] - (i-1), ficha[1] - (i-1), ficha[2]]
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
    #fila
    for fila in tabla:
        if all(celda == fila[0] and celda != "-" for celda in fila):
            return True

    #columna
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


# Alpha-Betha pruning algorithm
'''
def alpha_beta_search(table):
    alpha = -math.inf
    beta = math.inf
    best_action = None
    if ai_piece == 'X': #if maximaxing player
      for action in actions(table, ai_piece):
          v = min_value(action, alpha, beta)
          if v > alpha:
              alpha = v
              best_action = action
    else:
      for action in actions(table, ai_piece):
          v = max_value(action, alpha, beta)
          if v < beta:
            beta = v
            best_action = action
    return best_action
'''
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

    best_action = None
    if maximizing_player:  # Maximizing player
        best_value = -math.inf
        for action in actions(table, ai_piece):
            value = min_value(result(table, action), alpha, beta)
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
    else:  # Minimizing player
        best_value = math.inf
        for action in actions(table, human_piece):
            value = max_value(result(table, action), alpha, beta)
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(beta, best_value)
            if beta <= alpha:
                break

    return best_action, best_value

def max_value(table, alpha, beta):
    if (terminal_test(table)):
        return utility(table)
    v = -math.inf
    for action in actions(table, ai_piece):
        v = max(v, min_value(action, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(table, alpha, beta):
    if (terminal_test(table)):
        return utility(table)
    v = math.inf
    for action in actions(table, ai_piece):
        v = min(v, max_value(action, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

# functions for alpha-beta def
def actions(table, ai_piece):
  res = []
  for i in range(len(table)):
    for j in range(len(table[i])):
      if table[i][j]==ai_piece:
        # Mueves
        f, c = i,j
        c_table = copy.deepcopy(table)
        for k in range(8):
          nf, nc = f + cf[k], c + cc[k]
          if nf>=0 and nf<4 and nc>=0 and nc<4:
            if c_table[nf][nc]=='_':
              c_table[f][c]='_'
              c_table[nf][nc] = ai_piece
              res.append(c_table)
  return res # devuelve una lista de matrices que son las acciones
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
def utility(table):
    # ganar en una fila o columna
    for i in range(4):
        if table[i][0] == "X" and table[i][0] == table[i][1] == table[i][2] == table[i][3] != "-":
          return 1
        else:
          return -1
        if table[0][i] == "X" and table[0][i] == table[1][i] == table[2][i] == table[3][i] != "-":
          return 1
        else:
          return -1
    # ganar cuatro esquinas
    if table[0][0] == "X" and table[0][0] == table[0][3] == table[3][0] == table[3][3] != "-":
      return 1
    else:
      return -1
    # cuadrado pequeño
    for i in range(3):
        for j in range(3):
            if (table[i][j] == "X" and table[i][j] == table[i][j+1] == table[i+1][j] == table[i+1][j+1] != "-"):
              return 1
            else:
              return -1
    # no hay ganador
    return 0
# function for main