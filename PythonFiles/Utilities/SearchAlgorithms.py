from PythonFiles.Classes.Problem import Problem
from PythonFiles.Classes.Node import Node
from PythonFiles.Classes.PriorityQueue import PriorityQueue
from PythonFiles.Utilities.Utilities import memoize

from PythonFiles.Utilities.Constants import MSG_FOUND_SOLUTION_WATER, MSG_NO_SOLUTION_WATER, INFINITY


def bfs(final_destination, jug_1_capacity, jug_2_capacity):
    final_path = []
    front = [[0, 0]]
    visited = []
    while not (not front):
        current = front.pop()
        x = current[0]
        y = current[1]
        final_path.append(current)

        if x == final_destination or y == final_destination:
            print(MSG_FOUND_SOLUTION_WATER)
            return final_path

        # rule 1
        if current[0] < jug_1_capacity and ([jug_1_capacity, current[1]] not in visited):
            front.append([jug_1_capacity, current[1]])
            visited.append([jug_1_capacity, current[1]])

        # rule 2
        if current[1] < jug_2_capacity and ([current[0], jug_2_capacity] not in visited):
            front.append([current[0], jug_2_capacity])
            visited.append([current[0], jug_2_capacity])

        # rule 3
        if current[0] > jug_1_capacity and ([0, current[1]] not in visited):
            front.append([0, current[1]])
            visited.append([0, current[1]])

        # rule 4
        if current[1] > jug_2_capacity and ([jug_1_capacity, 0] not in visited):
            front.append([jug_1_capacity, 0])
            visited.append([jug_1_capacity, 0])

        # rule 5
        # (x, y) -> (min(x + y, jug_1_capacity), max(0, x + y - jug_1_capacity)) if y > 0
        if current[1] > 0 and ([min(x + y, jug_1_capacity), max(0, x + y - jug_1_capacity)] not in visited):
            front.append([min(x + y, jug_1_capacity), max(0, x + y - jug_1_capacity)])
            visited.append([min(x + y, jug_1_capacity), max(0, x + y - jug_1_capacity)])

        # rule 6
        # (x, y) -> (max(0, x + y - jug_2_capacity), min(x + y, jug_2_capacity)) if x > 0
        if current[0] > 0 and ([max(0, x + y - jug_2_capacity), min(x + y, jug_2_capacity)] not in visited):
            front.append([max(0, x + y - jug_2_capacity), min(x + y, jug_2_capacity)])
            visited.append([max(0, x + y - jug_2_capacity), min(x + y, jug_2_capacity)])

    return MSG_NO_SOLUTION_WATER


def best_first_graph_search(problem: Problem, f):  # nope
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()

    while frontier:

        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)

    return None


def a_star(problem: Problem, h=None):
    """A* search is best-first graph search with f(n) = g(n) + h(n)."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))
