import sys

# Heuristic function (Manhattan distance)
def heuristic(state, goal_state):
    distance = 0
    ### your implementation ####
    ############################
    return distance

# Successor function
def successors(state):
    successors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_i, empty_j = i, j

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        new_i, new_j = empty_i + move[0], empty_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[empty_i][empty_j] = new_state[new_i][new_j]
            new_state[new_i][new_j] = 0
            successors.append(new_state)

    return successors

# Goal test function
def is_goal(state, goal_state):
    return state == goal_state

# Print puzzle 
def print_puzzle(state):
    for row in state:
        print(row)

# Recursive Best-First Search
def rbfs(state, goal_state, f_limit):
    if is_goal(state, goal_state):
        return state

    ### your implementation ###
    ###########################


# Example input
initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
f_limit = heuristic(initial_state, goal_state)
result = rbfs(initial_state, goal_state, f_limit)


print("Initial state:")
print_puzzle(initial_state)

if result is not None:
    print("Goal state reached:")
    print_puzzle(result)
else:
    print("Goal state could not be reached.")
