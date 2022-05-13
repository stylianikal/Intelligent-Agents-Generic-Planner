from PythonFiles.Utilities.SearchAlgorithms import bfs
from PythonFiles.Utilities.Utilities import gcd, _exit


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
