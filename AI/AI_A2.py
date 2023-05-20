import random

# Function to calculate the number of conflicts (i.e., number of attacking queens) for a given state
def calculate_conflicts(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j]:
                conflicts += 1
            offset = j - i
            if state[i] == state[j] - offset or state[i] == state[j] + offset:
                conflicts += 1
    return conflicts

# Function to generate a random state (i.e., a random arrangement of queens on the board)
def generate_random_state(size):
    state = []
    for i in range(size):
        state.append(random.randint(0, size-1))
    return state

# Function to find the next best state using hill climbing
def hill_climbing(current_state):
    current_conflicts = calculate_conflicts(current_state)
    if current_conflicts == 0:
        return current_state
    best_state = current_state
    best_conflicts = current_conflicts
    for i in range(len(current_state)):
        for j in range(len(current_state)):
            if i != j:
                new_state = list(current_state)
                new_state[i] = j
                new_conflicts = calculate_conflicts(new_state)
                if new_conflicts < best_conflicts:
                    best_state = new_state
                    best_conflicts = new_conflicts
    if best_conflicts < current_conflicts:
        return hill_climbing(best_state)
    else:
        return current_state

# Function to solve the n-queens problem using hill climbing
def solve_n_queens(size):
    current_state = generate_random_state(size)
    solution_state = hill_climbing(current_state)
    return solution_state

# Testing the function for n = 8 queens
n = 8
solution_state = solve_n_queens(n)
print("Solution: " + str(solution_state))

#OUTPUT
#[Running] python -u "c:\Users\Admin\OneDrive\Desktop\Coding\n-queens.py"
#Solution: [0, 4, 6, 1, 2, 6, 3, 7]

#[Done] exited with code=0 in 0.123 seconds


