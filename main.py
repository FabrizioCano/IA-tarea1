from algoritmos_busqueda import BFS, AStar_search,DFS
import random
from time import time
import random



def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv

def solvable(puzzle):
    inv_counter = inv_num(puzzle)
    if (inv_counter %2 ==0):
        return True
    return False


def generar_tablero_inicial(n):
    #Genera un tablero inicial aleatorio y solucionable para el N-puzzle (n x n). El tablero contiene los números del 1 al n*n - 1 y un 0 que representa el espacio vacío.
    estado_meta = list(range(1, n * n)) + [0]
    print("Estado meta: ")
    print_board(estado_meta,n)
    random.shuffle(estado_meta)  # Mezcla el estado meta para crear un estado inicial aleatorio
    print("Estado inicial: ")
    print_board(estado_meta,n)
    return estado_meta


def print_board(tablero_inicial, n):
    for i in range(n):
        print(tablero_inicial[i * n:(i + 1) * n])
    print("")



    
#estado inicial
n=int(input("Ingrese N: "))
while True:
    tablero_inicial=generar_tablero_inicial(n)

    if solvable(tablero_inicial)==False:
        print("El tablero inicial no es solucionable. Generando otro tablero...")
        continue

    print("El tablero inicial es solucionable")
    print("Resolviendo el tablero inicial...")
    break

#resolver por A*
#distancia de manhattan
time_iastar=time()
tablero_Astar=AStar_search(tablero_inicial,n,0)
time_astar=time()-time_iastar
print("Tablero Solucion de A* (h=Dist.Manhattan): ")
print("Tiempo de A*: ",time_astar)
print(f'Numero de nodos expandidos: {tablero_Astar[1]}')

#piezas mal colocadas
time_iastar1=time()
tablero_Astar2=AStar_search(tablero_inicial,n,1)
time_astar1=time()-time_iastar1
print("Tablero Solucion de A* (h=Piezas mal colocadas): ")
print("Tiempo de A*: ",time_astar1)
print(f'Numero de nodos expandidos: {tablero_Astar2[1]}')

#resolver por Busqueda en profundidad
time_idfs=time()
tablero_DFS=DFS(tablero_inicial,n)
time_fdfs=time()-time_idfs
print("Tablero solucion de DFS: ")
print("Tiempo de Busqueda en profundidad: ",time_fdfs)
print(f'Numero de nodos expandidos: {tablero_DFS[1]}')

#resolver por Busqueda en anchura
time_ibfs=time()
tablero_BFS=BFS(tablero_inicial,n)
time_fbfs=time()-time_ibfs
print("Tablero solucion de BFS: ")
print("Tiempo de Busqueda en Anchura: ",time_fbfs)
print(f'Numero de nodos expandidos: {tablero_BFS[1]}')

with open("resultados.txt","a") as f:
    f.write("Estado inicial:\n")
    for i in range(n):
        f.write(str(tablero_inicial[i * n:(i + 1) * n]) + "\n")
    f.write("\n")
    f.write("=== A* con heuristica: Distancia de Manhattan ===\n")
    f.write(f"Tiempo de ejecucion: {time_astar:.6f} segundos\n")
    f.write(f"Nodos expandidos: {tablero_Astar[1]}\n")
    f.write(f"Movimientos: {tablero_Astar[0]}\n\n") 

    f.write("=== A* con heuristica: Piezas mal colocadas ===\n")
    f.write(f"Tiempo de ejecucion: {time_astar1:.6f} segundos\n")
    f.write(f"Nodos expandidos: {tablero_Astar2[1]}\n")
    f.write(f"Movimientos: {tablero_Astar2[0]}\n\n")

    f.write("=== Busqueda en Profundidad (DFS) ===\n")
    f.write(f"Tiempo de ejecucion: {time_fdfs:.6f} segundos\n")
    f.write(f"Nodos expandidos: {tablero_DFS[1]}\n")
    f.write(f"Movimientos: {tablero_DFS[0]}\n\n")
    
    f.write("=== Busqueda en Anchura (BFS) ===\n")
    f.write(f"Tiempo de ejecucion: {time_fbfs:.6f} segundos\n")
    f.write(f"Nodos expandidos: {tablero_BFS[1]}\n")
    f.write(f"Movimientos: {tablero_BFS[0]}\n\n")
    
    
