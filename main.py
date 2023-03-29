from game import *
import os


def juego():
    print("Juego cautela")
    turno = 1
    #Una ficha = [fila,columna,nombre]
    fichas_negras = [[0,0,"X"],[1,1,"X"],[2,2,"X"],[3,3,"X"]]
    fichas_blancas = [[3,0,"O"],[2,1,"O"],[1,2,"O"],[0,3,"O"]]
    tabla = tabla_por_defecto(crear_tabla(),fichas_negras)
    tabla = tabla_por_defecto(tabla,fichas_blancas)
    while True:
        os.system("clear")
        mostrar_tabla(tabla)
        if turno % 2 == 0:
            print("Fichas blancas del jugador 2")
            mostrar_fichas_del_jugador(fichas_blancas)
            numero_ficha = int(input("Elije tu ficha: "))
            movimiento = input("Elige tu Movimiento (N,S,E,O,NE,NO,SE,SO): ")
            ficha = fichas_blancas[numero_ficha - 1]
            fichas_blancas[numero_ficha - 1] = mover_ficha(tabla,ficha,movimiento)
        else:
            print("Fichas negras del jugador 1")
            mostrar_fichas_del_jugador(fichas_negras)
            numero_ficha = int(input("Elije tu ficha: "))
            movimiento = input("Elige tu Movimiento (N,S,E,O,NE,NO,SE,SO): ")
            ficha = fichas_negras[numero_ficha - 1]
            fichas_negras[numero_ficha - 1] = mover_ficha(tabla,ficha,movimiento)
        #ficha = input("Insertar ficha en (fila,columna,ficha) o salir: ")
        #datos_ficha = ficha.split(sep=",")
        continuar = input("Desea Continuar (S,N): ")
        if continuar == "N":
            return False
        else:
            #tabla = insertar_en_tabla(datos_ficha,tabla)
            #print(datos_ficha)
            turno +=1


if __name__ == "__main__":
    juego()
