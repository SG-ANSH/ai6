def dfs_water_jug(jug1_capacity, jug2_capacity, target_amount):
    """Implement Depth-First Search (DFS) to solve the Water Jug Problem."""
    visited = set()
    stack = [(0, 0, [])]  # (current_amount_jug1, current_amount_jug2, path)

    while stack:
        current_amount_jug1, current_amount_jug2, path = stack.pop()

        if (current_amount_jug1, current_amount_jug2) in visited:
            continue

        visited.add((current_amount_jug1, current_amount_jug2))

        # Check if target amount is reached
        if current_amount_jug1 == target_amount or current_amount_jug2 == target_amount:
            path.append((current_amount_jug1, current_amount_jug2))
            return path  # Return the path to reach the target amount

        # Define all possible operations (actions)
        operations = [
            ("fill jug1", jug1_capacity, current_amount_jug2),
            ("fill jug2", current_amount_jug1, jug2_capacity),
            ("empty jug1", 0, current_amount_jug2),
            ("empty jug2", current_amount_jug1, 0),
            ("pour jug1 to jug2", max(0, current_amount_jug1 - (jug2_capacity - current_amount_jug2)),
                                  min(jug2_capacity, current_amount_jug1 + current_amount_jug2)),
            ("pour jug2 to jug1", min(jug1_capacity, current_amount_jug1 + current_amount_jug2),
                                  max(0, current_amount_jug2 - (jug1_capacity - current_amount_jug1)))
        ]

        for operation_name, new_amount_jug1, new_amount_jug2 in operations:
            new_path = path + [(current_amount_jug1, current_amount_jug2, operation_name)]
            stack.append((new_amount_jug1, new_amount_jug2, new_path))

    return None  # If target amount cannot be reached

def print_solution(solution):
    """Print the solution path."""
    if solution:
        print("Solution Path:")
        for step in solution:
            print(f"Step: {step[2]}")
            print(f"Jug 1: {step[0]}, Jug 2: {step[1]}")
            print("")
    else:
        print("Target amount cannot be measured.")

if __name__ == "__main__":
    # Example: Solve for measuring 4 units of water using jugs with capacities 5 and 3
    jug1_capacity = 5
    jug2_capacity = 3
    target_amount = 4

    solution = dfs_water_jug(jug1_capacity, jug2_capacity, target_amount)
    print_solution(solution)
