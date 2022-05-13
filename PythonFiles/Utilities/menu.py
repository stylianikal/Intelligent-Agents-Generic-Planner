from PythonFiles.Utilities.SearchAlgorithms import bfs
from PythonFiles.Utilities.Utilities import gcd

from sys import exit

from PythonFiles.Utilities.Constants import MSG_SELECT_GAME


def _exit():
    print("Thank you for using our application.")
    exit()


def jugsProblem():
    x_capacity = input("Enter Jug 1 capacity:")
    y_capacity = input("Enter Jug 2 capacity:")
    end = input("Enter target volume:")
    start = [0, 0]

    if end % gcd(x_capacity, y_capacity) == 0:
        print("Solution for water jug problem")
        print(bfs(start, end, x_capacity, y_capacity))
    else:
        print("No solution possible for this combination.")


def blockWorld():
    print()


def showMenu():
    problem = str(input(MSG_SELECT_GAME))

    if problem == "1":
        print("1")
    elif problem == "2":
        print("2")
    elif problem.upper() == "Q":
        _exit()
