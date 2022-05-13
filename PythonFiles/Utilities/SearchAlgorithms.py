from PythonFiles.Utilities.Constants import MSG_FOUND_SOLUTION_WATER, MSG_NO_SOLUTION_WATER


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
