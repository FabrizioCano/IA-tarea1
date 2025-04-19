import tkinter as tk
from tkinter import messagebox
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
    while True:
        estado_inicial = estado_meta[:-1]
        random.shuffle(estado_inicial)
        estado_inicial.append(0)
        if solvable(estado_inicial):
            return estado_inicial, estado_meta


def display_board(board, n):
    return "\n".join(str(board[i * n:(i + 1) * n]) for i in range(n))


def resolver():
    try:
        n = int(entry_n.get())
        if n < 2:
            raise ValueError("N debe ser mayor o igual a 2")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")
        return

    tablero_inicial, estado_meta = generar_tablero_inicial(n)
    result_output.delete("1.0", tk.END)

    result_output.insert(tk.END, f"Estado meta:\n{display_board(estado_meta, n)}\n\n")
    result_output.insert(tk.END, f"Estado inicial (solucionable):\n{display_board(tablero_inicial, n)}\n\n")


    # A* Manhattan
    t0 = time()
    resultado_astar = AStar_search(tablero_inicial, n, 0)
    t_astar = time() - t0
    result_output.insert(tk.END, "=== A* (Distancia Manhattan) ===\n")
    if resultado_astar[1] == "TIMEOUT":
        result_output.insert(tk.END, "No se pudo resolver: complejidad espacial muy grande (timeout).\n\n")
        messagebox.showwarning("A* Manhattan", "No se pudo resolver: complejidad espacial muy grande.")
    else:
        result_output.insert(tk.END, f"Tiempo: {t_astar:.6f} s\n")
        result_output.insert(tk.END, f"Nodos expandidos: {resultado_astar[1] if resultado_astar is not None and resultado_astar[1] is not None else "0"}\n\n")
        result_output.insert(tk.END,f"Movimientos:  {resultado_astar[0] if  resultado_astar is not None and resultado_astar[0] is not None else "0"}\n\n") 

    # A* Piezas mal colocadas
    t0 = time()
    resultado_astar2 = AStar_search(tablero_inicial, n, 1)
    t_astar2 = time() - t0
    result_output.insert(tk.END, "=== A* (Piezas mal colocadas) ===\n")
    if resultado_astar2[1] == "TIMEOUT":
        result_output.insert(tk.END, "No se pudo resolver: complejidad espacial muy grande (timeout).\n\n")
        messagebox.showwarning("A* Manhattan", "No se pudo resolver: complejidad espacial muy grande.")
    else:
        result_output.insert(tk.END, f"Tiempo: {t_astar:.6f} s\n")
        result_output.insert(tk.END, f"Nodos expandidos: {resultado_astar2[1] if resultado_astar2 is not None and resultado_astar2[1] is not None else "0"}\n\n")
        result_output.insert(tk.END,f"Movimientos:  {resultado_astar2[0] if  resultado_astar2 is not None and resultado_astar2[0] is not None else "0"}\n\n")  

    # BFS
    t0 = time()
    resultado_bfs = BFS(tablero_inicial, n)
    t_bfs = time() - t0
    result_output.insert(tk.END, "=== BFS ===\n")
    if len(resultado_bfs) > 1 and resultado_bfs[1] == "TIMEOUT":
        result_output.insert(tk.END, "No se pudo resolver: complejidad espacial muy grande (timeout).\n\n")
        messagebox.showwarning("BFS", "No se pudo resolver: complejidad espacial muy grande.")
    else:
        result_output.insert(tk.END, f"Tiempo: {t_bfs:.6f} s\n")
        result_output.insert(tk.END, f"Nodos expandidos: {resultado_bfs[1] if len(resultado_bfs) > 1 and resultado_bfs[1] is not None else "0"}\n\n")
        result_output.insert(tk.END,f"Movimientos: {resultado_bfs[0] if len(resultado_bfs) > 1 and resultado_bfs[0] is not None else "0"}\n\n")

  
    # DFS
   
    t0 = time()
    resultado_dfs = DFS(tablero_inicial, n)
    t_dfs = time() - t0
    result_output.insert(tk.END, "=== DFS ===\n")
    
    result_output.insert(tk.END, f"Tiempo: {t_dfs:.6f} s\n")
    result_output.insert(tk.END, f"Nodos expandidos: {resultado_dfs[1] if len(resultado_dfs) > 1 and resultado_dfs[1] is not None else "0"}\n\n")
    result_output.insert(tk.END,f"Movimientos: {resultado_dfs[0] if len(resultado_dfs) > 1 and resultado_dfs[0] is not None else "0"}\n\n")
    
    with open("resultados.txt", "a") as f:
        f.write(result_output.get("1.0", tk.END))


# === GUI setup ===
root = tk.Tk()
root.title("N-Puzzle Solver GUI")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Ingrese N (dimensión del tablero):").grid(row=0, column=0)
entry_n = tk.Entry(frame)
entry_n.grid(row=0, column=1)

tk.Button(frame, text="Generar y Resolver", command=resolver).grid(row=0, column=2, padx=10)

result_output = tk.Text(root, width=70, height=30)
result_output.pack(padx=10, pady=10)

root.mainloop()