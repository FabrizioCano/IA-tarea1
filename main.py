from algoritmos_busqueda import BFS, AStar_search
import random
from time import time

def solucionable(tablero,n):
    flat_board = [num for row in tablero for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_board)):
        for j in range(i + 1, len(flat_board)):
            if flat_board[i] > flat_board[j]:
                inversions += 1 
    
    if n%2==1:
        #si es un tablero impar, el número de inversiones debe ser par
        return inversions%2==0
    else:
        #si es un tablero par, hay que chequear la posición de la casilla vacía
        empty_row = next(i for i in range(n) if 0 in tablero[i])
        #convertimos la posición de la casilla vacía a la fila desde abajo
        #número de filas desde abajo
        row_from_bottom = n - empty_row
        #si el número de filas desde abajo es par, el número de inversiones debe ser impar
        if row_from_bottom % 2 == 0:
            return inversions % 2 == 1
        #si el número de filas desde abajo es impar, el número de inversiones debe ser par
        else:
            return inversions % 2 == 0
    
def generar_tablero_inicial(n):
    # Generar una lista con los números del 0 al n*n-1
    estado = list(range(n * n))
    # Convertir la lista en una matriz de n x n
    while True:
        # Mezclar la lista de forma aleatoria
        random.shuffle(estado)
        tablero = [estado[i * n:(i + 1) * n] for i in range(n)]

        if solucionable(tablero,n):
            # Si el tablero es solucionable, lo devolvemos
            return estado
def print_board(board, n):
    for i in range(n):
        row = board[i * n:(i + 1) * n]
        print(" ".join(f"{num:2}" if num != 0 else " ▢" for num in row))
    print()



    
    
#estado inicial
n=int(input("Ingrese N: "))
heuristic=int(input("Ingrese heuristica para el algoritmo A* (0 para Distancia de Manhattan, 1 para Casillas Mal Colocadas): "))
tablero_inicial=generar_tablero_inicial(n)

print("Estado inicial:")
print_board(tablero_inicial,n)

#resolver por Busqueda en anchura
time_ibfs=time()
tablero_BFS=BFS(tablero_inicial,n)
time_fbfs=time()-time_ibfs
print("Tablero solucion de BFS: ")
print_board(tablero_BFS[0][-1], n)  # Solo imprime el último estado

print("Tiempo de Busqueda en Anchura: ",time_fbfs)
print(f'Numero de nodos expandidos: {tablero_BFS[1]}')


#resolver por A*
time_iastar=time()
tablero_Astar=AStar_search(tablero_inicial,n,heuristic)
time_astar=time()-time_iastar
print("Tablero Solucion de A*: ")
print_board(tablero_Astar[0][-1],n)
print("Tiempo de A*: ",time_astar)
print(f'Numero de nodos expandidos: {tablero_Astar[1]}')





