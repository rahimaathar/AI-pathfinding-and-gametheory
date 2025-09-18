from maze_visual import maze, agent
import sys
import argparse
import math
from queue import PriorityQueue

ROWS = 20 
COLS = 20 
m = maze(ROWS, COLS) 

m.LoadMaze(loadMaze='maze_config.csv', theme="dark")

def DFS(maze, start, goal):
    visited_positions = []
    path_to_goal = []
    
    frontiers = [start]
    order = ['E','S','W','N']
    visited_positions.append(start)
    pathtoreverse = {}

    while len(frontiers) != 0:
        currentNode = frontiers.pop()
        if currentNode == goal:
            break
        for direction in order:
            if maze.maze_map[currentNode][direction]==True:
                x, y = currentNode
                if direction == 'E':
                    childNode = (x, y+1)
                elif direction == 'S':
                    childNode = (x+1, y)
                elif direction == 'W':
                    childNode = (x, y-1)
                elif direction == 'N':
                    childNode = (x-1, y)
                if childNode not in visited_positions:
                    visited_positions.append(childNode)
                    frontiers.append(childNode)
                    pathtoreverse[childNode]=currentNode

                    
    path_to_goal = [goal]   
    tempnode = goal

    while tempnode != start:
        tempnode = pathtoreverse[tempnode]
        path_to_goal.append(tempnode)

    path_to_goal.reverse()

    return visited_positions, path_to_goal




def BFS(maze, start, goal):
    visited_positions = []
    path_to_goal = []

    frontiers = [start]
    order = ['N','W','S','E']
    visited_positions.append(start)
    pathtoreverse = {}

    while len(frontiers) != 0:
        currentNode = frontiers.pop(0)
        if currentNode == goal:
            break
        for direction in order:
            if maze.maze_map[currentNode][direction]==True:
                x, y = currentNode
                if direction == 'N':
                    childNode = (x-1, y)
                elif direction == 'W':
                    childNode = (x, y-1)
                elif direction == 'S':
                    childNode = (x+1, y)
                elif direction == 'E':            
                    childNode = (x, y+1)

                if childNode not in visited_positions:
                    visited_positions.append(childNode)
                    frontiers.append(childNode)
                    pathtoreverse[childNode]=currentNode

                    
    path_to_goal = [goal]   
    tempnode = goal

    while tempnode != start:               # the loop continues to run until the start node hasnt reached
        tempnode = pathtoreverse[tempnode] #tempnode= descendant retrieved from the pathtoreverse dictionary
        path_to_goal.append(tempnode)      #append the descendant to the list

    path_to_goal.reverse()                #reverse the list to start from the 'start' node


    return visited_positions, path_to_goal




def heuristic(position, goal):
    '''
    This function should implement Euclidean Distance as the heuristic function used in A* algorithm.
    The inputs to this function are:
        position: The current position of the agent as a tuple (x,y)
        goal: The goal position of the agent as a tuple (x,y)
    The function should return:
        the heuristic value of the given position
    '''
    if position==goal:  #heuristic of goal node is 0
        h = 0
    else:
        x1,y1=position
        x2,y2=goal
        h = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) ##formula applied
    return h

def AStar(maze, start, goal):
    visited_positions = []
    path_to_goal = []
    
    order = ['N','W','S','E']
    visited_positions.append(start)
    pathtoreverse = {}
    
    gn = {}
    fn = {}

    for i in range(1, 21):
        for j in range(1, 21):
            node = (i, j)
            gn[node] = float('inf')
            fn[node] = float('inf')
            
    
    ##for start node
    gn[start]=0         #gn measures distance from start node, so for start node, its 0
    fn[start]=0+heuristic(start,goal)    #fn=gn+hn= 0+hn
    
    frontiers=PriorityQueue()            #a priority queue used in A* search
    frontiers.put((fn[start],heuristic(start,goal),start))  #putting the start node in the queue in the form of tuple
    
    
    while not frontiers.empty():                 
        currentTuple = frontiers.get()
        currentNode = currentTuple[2]     #extracting the 2nd index from the tuple of priority queue

        if currentNode == goal:
            break

        for direction in order:
            if maze.maze_map[currentNode][direction] == True:
                x, y = currentNode
                if direction == 'N':
                    childNode = (x-1, y)
                elif direction == 'W':
                    childNode = (x, y-1)
                elif direction == 'S':
                    childNode = (x+1, y)
                elif direction == 'E':
                    childNode = (x, y+1)

                newgn = gn[currentNode] + 1         #next gn =current cost +1
                newfn = newgn + heuristic(childNode, goal) #total=fn=gn+hn

                if newfn < fn[childNode]:     # we choose nodes with lower fn (low cost)
                    gn[childNode] = newgn
                    fn[childNode] = newfn
                    frontiers.put((newfn,heuristic(childNode,goal),childNode))  
                    visited_positions.append(childNode)
                    pathtoreverse[childNode]=currentNode
                    
                    
                               
    path_to_goal = [goal]   
    tempnode = goal

    while tempnode != start:               # the loop continues to run until the start node hasnt reached
        tempnode = pathtoreverse[tempnode] #tempnode= descendant retrieved from the pathtoreverse dictionary
        path_to_goal.append(tempnode)      #append the descendant to the list

    path_to_goal.reverse()                #reverse the list to start from the 'start' node
                    

    return visited_positions, path_to_goal



# DO NOT CHANGE THE LINES OF CODE BELOW
# -------------------------------------
# This part of the code calls the search algorithms implemented above and displays the results on the maze
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bfs", help="Run BFS", action="store_true")
    parser.add_argument("-d", "--dfs", help="Run DFS", action="store_true")
    parser.add_argument("-a", "--astar", help="Run A* Search", action="store_true")

    args = parser.parse_args()

    start = (ROWS, COLS)
    goal = (1,1)

    explored, path_to_goal = [], []

    if args.bfs:
        explored, path_to_goal = BFS(m, start, goal)
    elif args.dfs:
        explored, path_to_goal = DFS(m, start, goal)
    elif args.astar:
        explored, path_to_goal = AStar(m, start, goal)
    else:
        print("No search algorithm specified. See help below.")
        parser.print_help()
        sys.exit()

    a = agent(m, ROWS, COLS, filled=True)
    b = agent(m, ROWS, COLS, color="red")

    m.tracePath({a: explored}, delay=20)
    m.tracePath({b: path_to_goal}, delay=50)

    m.run()


if __name__ == "__main__":
    main()











