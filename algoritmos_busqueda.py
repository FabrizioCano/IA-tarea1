from state import State
from queue import PriorityQueue
from queue import Queue



def BFS(given_state, n):
    #nodo inicial
    root = State(given_state, None, None, 0, 0, n)
    #verifica si el nodo inicial es la solucion
    if root.test():
        return root.solution()
    #crea la cola de nodos por explorar y la lista de nodos explorados
    #inicializa la cola con el nodo inicial y una lista de nodos explorados vacia
    frontier = Queue()
    frontier.put(root)
    explored = []

    #mientras la cola no este vacia, se extrae el nodo actual y se expande
    while not frontier.empty():
        current_node = frontier.get() 
        explored.append(current_node.state) #se agrega el nodo actual a la lista de nodos explorados
        children = current_node.expand() #se expanden los nodos hijos del nodo actual
        for child in children: #se itera sobre los nodos hijos
            if child.state not in explored: #si el nodo hijo no ha sido explorado
                if child.test(): #verifica si el nodo hijo es la solucion
                    return child.solution(), len(explored) #si es la solucion, devuelve la secuencia de tableros y el numero de nodos explorados
                frontier.put(child) #si no es la solucion, se agrega el nodo hijo a la cola de nodos por explorar
    
    return None  #si no se encuentra la solucion, devuelve None


def AStar_search(given_state, n, heuristic):
    frontier = PriorityQueue() #se crea la cola de prioridad para los nodos por explorar
    #se inicializa el nodo inicial y se verifica si es la solucion
    explored = []
    counter = 0
    #se crea el nodo inicial con el estado dado, sin padre, sin movimiento, profundidad 0, costo 0 y tamaño n
    root = State(given_state, None, None, 0, 0, n)
    #si la heuristica es 0, se calcula la distancia de manhattan, si no, se calcula el numero de casillas mal colocadas
    if heuristic == 0:
        root.Manhattan_Distance(n)
    else:
        root.Misplaced_Tiles(n)

    #se agrega el nodo inicial a la cola de prioridad con su evaluacion A* y un contador
    #para el numero de nodos explorados
    frontier.put((root.AStar_evaluation, counter, root))

    #mientras la cola de prioridad no este vacia, se extrae el nodo actual y se expande
    while not frontier.empty():
        _, _, current_node = frontier.get() #se extrae el nodo con menor evaluacion A*
        explored.append(current_node.state) #se agrega el nodo actual a la lista de nodos explorados

        if current_node.test(): #si el nodo actual es la solucion
            return current_node.solution(), len(explored) #se devuelve la secuencia de tableros y el numero de nodos explorados

        children = current_node.expand() #se expanden los nodos hijos del nodo actual
        for child in children: #se itera sobre los nodos hijos
            if child.state not in explored: #si el nodo hijo no ha sido explorado se incrementa el contador
                counter += 1
                if heuristic == 0: #si la heuristica es 0, se calcula la distancia de manhattan, si no, se calcula el numero de casillas mal colocadas
                    child.Manhattan_Distance(n)
                else:
                    child.Misplaced_Tiles(n)
                frontier.put((child.AStar_evaluation, counter, child)) #se agrega el nodo hijo a la cola de prioridad con su evaluacion A* y el contador si ninguno de los nodos hijos es la solucion

    return None  # No se encuentra la solucion, devuelve None
