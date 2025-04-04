from state import State
from queue import PriorityQueue
from queue import Queue



def BFS(given_state, n):
    root = State(given_state, None, None, 0, 0, n)
    if root.test():
        return root.solution()
    
    frontier = Queue()
    frontier.put(root)
    explored = []

    while not frontier.empty():
        current_node = frontier.get()
        explored.append(current_node.state)
        children = current_node.expand()
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    
    return None  # No solution found


from queue import PriorityQueue

def AStar_search(given_state, n, heuristic):
    frontier = PriorityQueue()
    explored = []
    counter = 0

    root = State(given_state, None, None, 0, 0, n)
    if heuristic == 0:
        root.Manhattan_Distance(n)
    else:
        root.Misplaced_Tiles(n)

    frontier.put((root.AStar_evaluation, counter, root))

    while not frontier.empty():
        _, _, current_node = frontier.get()
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand()
        for child in children:
            if child.state not in explored:
                counter += 1
                if heuristic == 0:
                    child.Manhattan_Distance(n)
                else:
                    child.Misplaced_Tiles(n)
                frontier.put((child.AStar_evaluation, counter, child))

    return None  # No solution found
