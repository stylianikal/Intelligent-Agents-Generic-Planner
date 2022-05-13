def bfs(start, end, x_capacity, y_capacity):
    path = []
    front = [start]
    visited = []

    while not (not front):
        current = front.pop()
        x = current[0]
        y = current[1]
        path.append(current)
        if x == end or y == end:
            print("Found!")
            return path
        # rule 1
        if current[0] < x_capacity and ([x_capacity, current[1]] not in visited):
            front.append([x_capacity, current[1]])
            visited.append([x_capacity, current[1]])

        # rule 2
        if current[1] < y_capacity and ([current[0], y_capacity] not in visited):
            front.append([current[0], y_capacity])
            visited.append([current[0], y_capacity])

        # rule 3
        if current[0] > x_capacity and ([0, current[1]] not in visited):
            front.append([0, current[1]])
            visited.append([0, current[1]])

        # rule 4
        if current[1] > y_capacity and ([x_capacity, 0] not in visited):
            front.append([x_capacity, 0])
            visited.append([x_capacity, 0])

        # rule 5
        # (x, y) -> (min(x + y, x_capacity), max(0, x + y - x_capacity)) if y > 0
        if current[1] > 0 and ([min(x + y, x_capacity), max(0, x + y - x_capacity)] not in visited):
            front.append([min(x + y, x_capacity), max(0, x + y - x_capacity)])
            visited.append([min(x + y, x_capacity), max(0, x + y - x_capacity)])

        # rule 6
        # (x, y) -> (max(0, x + y - y_capacity), min(x + y, y_capacity)) if x > 0
        if current[0] > 0 and ([max(0, x + y - y_capacity), min(x + y, y_capacity)] not in visited):
            front.append([max(0, x + y - y_capacity), min(x + y, y_capacity)])
            visited.append([max(0, x + y - y_capacity), min(x + y, y_capacity)])

    return "Not found"