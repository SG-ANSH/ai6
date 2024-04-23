from collections import deque

# Define the goal state of the 8 Puzzle (1 represents empty space)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def bfs_8_puzzle(initial_state):
    """Implement Breadth-First Search (BFS) to solve the 8 Puzzle problem."""
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path  # Return the path to reach the goal state

        zero_index = current_state.index(0)
        row, col = zero_index // 3, zero_index % 3

        # Generate possible moves (up, down, left, right)
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + move[0], col + move[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(current_state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    return None  # If no solution found

def print_solution(solution):
    """Print the solution path."""
    if solution:
        print("Solution Path:")
        for i, state in enumerate(solution):
            print(f"Step {i + 1}:")
            print_board(state)
            print("")
    else:
        print("No solution found.")

def print_board(state):
    """Print the current state of the 8 Puzzle."""
    for i in range(3):
        print(" | ".join(str(state[i * 3 + j]) if state[i * 3 + j] != 0 else " " for j in range(3)))
        print("-" * 9)

if __name__ == "__main__":
    # Example initial state (customize as needed)
    initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)

    print("Initial State:")
    print_board(initial_state)
    print("")

    # Solve using BFS
    solution = bfs_8_puzzle(initial_state)

    # Print the solution path
    print_solution(solution)
