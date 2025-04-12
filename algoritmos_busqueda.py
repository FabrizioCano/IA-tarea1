from state import State
from queue import PriorityQueue,LifoQueue
from queue import Queue



def BFS(given_state, n):
    #nodo inicial
    root = State(given_state, None, None, 0, 0)
    #verifica si el nodo inicial es la solucion
    if root.test():
        return root.solution()
    #crea la cola de nodos por explorar y la lista de nodos explorados
    #inicializa la cola con el nodo inicial y una lista de nodos explorados vacia
    frontier = Queue()
    frontier.put(root)
    explored = set()

    #mientras la cola no este vacia, se extrae el nodo actual y se expande
    while not frontier.empty():
        current_node = frontier.get() 
        explored.add(tuple(current_node.state)) #se agrega el nodo actual a la lista de nodos explorados
        children = current_node.expand(n) #se expanden los nodos hijos del nodo actual
        for child in children: #se itera sobre los nodos hijos
            if tuple(child.state) not in explored: #si el nodo hijo no ha sido explorado
                if child.test(): #verifica si el nodo hijo es la solucion
                    return child.solution(), len(explored) #si es la solucion, devuelve la secuencia de tableros y el numero de nodos explorados
                frontier.put(child) #si no es la solucion, se agrega el nodo hijo a la cola de nodos por explorar
                explored.add(tuple(child.state)) #se agrega el nodo hijo a la lista de nodos explorados
    
    return  #si no se encuentra la solucion, devuelve None

def DFS(given_state , n): 
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth #current depth
        explored.append(current_node.state)
        
        if max_depth == 30:
            continue #go to the next branch

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return (("Couldn't find solution in the limited depth."), len(explored))

def AStar_search(given_state, n, heuristic):
    frontier = PriorityQueue()  # Cola de prioridad
    frontier_dict = {}  # Diccionario para optimizar la gestión de nodos en la cola
    explored = set()  # Conjunto de nodos explorados
    counter = 0
    
    root = State(given_state, None, None, 0, 0)
    if heuristic == 0:
        evaluation = root.Manhattan_Distance(n)
    else:
        evaluation = root.Misplaced_Tiles(n)
    
    frontier.put((evaluation, counter, root))
    frontier_dict[tuple(root.state)] = (evaluation, counter)  # Agregar el nodo inicial al diccionario

    while not frontier.empty():
        current_node = frontier.get()  # Obtener el nodo con menor evaluación A*
        current_node = current_node[2]
        
        if tuple(current_node.state) in explored:  # Si el nodo ya ha sido explorado
            continue
        
        explored.add(tuple(current_node.state))  # Agregar a nodos explorados

        if current_node.test():  # Si el nodo es la solución
            return current_node.solution(), len(explored)
        
        children = current_node.expand(n)  # Expandir nodos hijos
        for child in children:
            if tuple(child.state) not in explored:
                counter += 1
                if heuristic == 0:
                    evaluation = child.Manhattan_Distance(n)
                else:
                    evaluation = child.Misplaced_Tiles(n)

                # Verificar si el hijo ya está en la cola y si tiene una mejor evaluación
                if tuple(child.state) not in frontier_dict or frontier_dict[tuple(child.state)][0] > evaluation:
                    frontier.put((evaluation, counter, child))
                    frontier_dict[tuple(child.state)] = (evaluation, counter)  # Actualizar el diccionario

    return  # No se encuentra la solucion, devuelve None
