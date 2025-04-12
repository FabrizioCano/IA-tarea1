#Reference: https://github.com/Pariasrz/N-Puzzle-solver-with-Search-Algorithms/blob/main

class State:
    
    AStar_evaluation = None
    heuristic = None
    goal = None
    def __init__(self, state, parent, direction, depth, cost):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth

        if parent:
            self.cost = parent.cost + cost

        else:
            self.cost = cost

        if State.goal is None:
            n = int(len(state) ** 0.5)  # Calcular n a partir de la longitud del estado
            State.goal = self.generate_goal_state(n)  
     
    def generate_goal_state(self, n):
        #Generar el estado meta basado en el tamaño de n
        return list(range(1, n * n)) + [0]
    
    def test(self): #check if the given state is goal
        if self.state == self.goal:
            return True
        return False
        
    #heuristic function based on Manhattan distance
    def Manhattan_Distance(self ,n): 
        self.heuristic = 0
        for i in range(1 , n*n):
            distance = abs(self.state.index(i) - self.goal.index(i))
            
            #manhattan distance between the current state and goal state
            self.heuristic = self.heuristic + distance/n + distance%n
   
        self.AStar_evaluation = self.heuristic + self.cost
        
        return self.AStar_evaluation


    #heuristic function based on number of misplaced tiles
    def Misplaced_Tiles(self,n): 
        self.heuristic = sum(1 for i in range(n*n) if self.state[i] != 0 and self.state[i] != self.goal[i]) 
        self.AStar_evaluation = self.heuristic + self.cost
        return self.AStar_evaluation
                
                    


    @staticmethod
    
    #this would remove illegal moves for a given state
    def available_moves(x,n): 
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n*n - 1:
            moves.remove('Down')

        return moves

    #produces children of a given state
    def expand(self,n): 
        x = self.state.index(0)
        moves = self.available_moves(x,n)
        children = []
        opposite = {'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}
        last_move = self.direction
        for direction in moves:
            if last_move and direction == opposite.get(last_move):
                continue
                
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]
          
            
            children.append(State(temp, self, direction, self.depth + 1, 1)) 
        return children


    

    # Devuelve la secuencia de tableros desde el inicial hasta el actual
    def solution(self):
        solution = []
        solution.append(self.direction)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution
