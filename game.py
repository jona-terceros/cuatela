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
            nueva_ficha = [ficha[0] - i+1, ficha[1] + i -1, ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)

    if (movimiento == "SE"):  # Sur Este, Diagonal inferior derecha
        i = 1
        while limite_matriz(ficha[0] + i, ficha[1] + i) and tabla[ficha[0] + i][ficha[1] + i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] + i -1, ficha[1] + i-1, ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)

    if (movimiento == "SO"):  # Diagonal inferior izquierda
        i = 1
        while limite_matriz(ficha[0] + i, ficha[1] - i) and tabla[ficha[0] + i][ficha[1] - i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] + i-1, ficha[1] - i-1, ficha[2]]
            tabla = insertar_en_tabla([ficha[0], ficha[1], "-"], tabla)
            tabla = insertar_en_tabla(nueva_ficha, tabla)

    if (movimiento == "NO"):  # Diagonal superior izquierda
        i = 1
        while limite_matriz(ficha[0] - i, ficha[1] - i) and tabla[ficha[0] - i][ficha[1] - i] == "-":
            i += 1
        if i > 1:
            nueva_ficha = [ficha[0] - i-1, ficha[1] - i-1, ficha[2]]
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