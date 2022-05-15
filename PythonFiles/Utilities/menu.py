from PythonFiles.Utilities.SearchAlgorithms import bfs, a_star
from PythonFiles.Utilities.Utilities import gcd, _exit, state_generator
from PythonFiles.Classes.BlocksWorld.BlocksWorldH2 import BlocksWorldH2


from PythonFiles.Utilities.Constants import MSG_SELECT_GAME, ALLOWED_ANSWERS, DEFAULT_ANSWER
from PythonFiles.Utilities.Constants import MSG_INPUT_1, MSG_INPUT_2, MSG_INPUT_TARGET, MSG_NO_POSSIBLE_SOLUTION_WATER


def jugsProblem():
    jug_1_capacity = int(input(MSG_INPUT_1))
    jug_2_capacity = int(input(MSG_INPUT_2))
    final_destination = int(input(MSG_INPUT_TARGET))

    if final_destination % gcd(jug_1_capacity, jug_2_capacity) != 0:
        print(MSG_NO_POSSIBLE_SOLUTION_WATER)
        return

    print(bfs(final_destination, jug_1_capacity, jug_2_capacity))


def blockWorld():
    print("Block world problem")
    blocks = int(input("Number of blocks : "))

    initial_state = state_generator(blocks)  # Generating random states for initial and goal state
    goal_state = state_generator(blocks)
    print("Initial: {}".format(initial_state))
    print("Goal: {}".format(goal_state))

    if initial_state is goal_state:
        print("Initial State is the same with the Goal State")
        return

    problem2 = BlocksWorldH2(initial_state, goal_state)

    a_star_results = a_star(problem2)  # A* search using second heuristic
    a_star_solution = a_star_results.solution()
    a_star_path = a_star_results.path()

    print("{:=^41}".format("Solution"))
    print("{:^16}{:^5}{:<50}".format("ACTION", '|', "STATE"))
    print("{:<16}{:^5}{:<50}".format('Initial State', '|', str(initial_state)))

    for iterator in range(1, len(a_star_path)):
        state = a_star_path[iterator].state
        action = a_star_solution[iterator - 1]

        if action[1] != ' ':
            msg = "Move from {} to {}".format(action[0], action[1])
        else:
            msg = "Move {} down".format(action[0])

        print("{:<16}{:^5}{:<50}".format(msg, '|', str(state)))


def showMenu():
    flag, problem = True, DEFAULT_ANSWER
    while flag:
        problem = str(input(MSG_SELECT_GAME))
        if problem in ALLOWED_ANSWERS:
            flag = False

    if problem == "1":
        jugsProblem()
    elif problem == "2":
        blockWorld()
    elif problem.upper() == "Q":
        _exit()
