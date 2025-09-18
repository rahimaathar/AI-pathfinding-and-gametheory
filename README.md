# AI Algorithms Project

This project implements three classic AI algorithms for my computer science course. I built a web interface to visualize how these algorithms work.

## What's Included

### 1. Pathfinding Algorithms (task1.py)
- **DFS (Depth-First Search)**: Explores paths as deep as possible before backtracking
- **BFS (Breadth-First Search)**: Explores all nodes at the same level before going deeper  
- **A* Search**: Uses heuristics to find the optimal path efficiently

### 2. Graph Coloring (task2.py)
- **Arc Consistency**: Removes inconsistent values from variable domains
- **DFS Backtracking**: Systematic search with constraint satisfaction
- Uses a European map coloring problem as an example

### 3. Game Theory (task3.py)
- **Minimax Algorithm**: Finds the best move for a player assuming optimal play
- **Alpha-Beta Pruning**: Optimizes minimax by cutting off unnecessary branches
- Implemented for Tic-Tac-Toe game

## How to Run

### Prerequisites
- Python 3.8+
- Flask
- NetworkX
- NumPy

### Installation
```bash
pip install -r requirements.txt
```

### Running the Web Demo
```bash
python app.py
```
Then open http://localhost:8080 in your browser.

### Running Individual Algorithms
```bash
# Pathfinding algorithms
python task1.py

# Graph coloring
python task2.py

# Game theory (Tic-Tac-Toe)
python task3.py
```

## Project Structure
```
├── task1.py          # Pathfinding algorithms
├── task2.py          # Graph coloring algorithms  
├── task3.py          # Game theory algorithms
├── app.py            # Flask web application
├── maze_visual.py    # Maze visualization utilities
├── maze_config.csv   # Maze configuration file
├── templates/        # HTML templates
├── static/          # CSS and JavaScript files
└── requirements.txt # Python dependencies
```

## What I Learned

- **Search Algorithms**: How different search strategies work and their trade-offs
- **Constraint Satisfaction**: How to solve problems with constraints
- **Game Theory**: How to implement optimal strategies for games
- **Web Development**: Creating interactive visualizations with Flask and JavaScript

## Challenges Faced

- Getting the A* algorithm to work correctly with the heuristic function
- Implementing alpha-beta pruning without breaking the minimax logic
- Making the web interface responsive and user-friendly
- Debugging the maze visualization (took a while to get the coordinates right!)

## Future Improvements

- Add more algorithms (Dijkstra, genetic algorithms)
- Improve the web interface design
- Add more interactive features
- Implement different game types for the game theory section

## Notes

This was a challenging but fun project! The hardest part was understanding how the different search algorithms work and implementing them correctly. The web interface makes it much easier to see how the algorithms explore the search space.