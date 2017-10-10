""" Islands is an array of islands. Each island has a required number of 'bridges' (island[0]) and a list (island[1]) of
other islands it can possibly connect to.
The aim is to build bridges between island so that each island exactly meets it's bridge count requirement and so
that each island is connected to all other island by these bridges"""
islands = [
    (3, [1, 9]),
    (5, [0, 2, 4]),
    (4, [1, 3, 11]),
    (3, [2, 8]),
    (4, [1, 5]),
    (4, [4, 6]),
    (1, [4, 7]),
    (4, [5, 6, 8, 10]),
    (1, [3, 7, 12]),
    (5, [0, 10, 13]),
    (5, [7, 9, 11, 15]),
    (2, [2, 10, 12]),
    (3, [8, 11, 17]),
    (3, [9, 14]),
    (4, [6, 13, 15]),
    (5, [10, 14, 16]),
    (1, [11, 15, 17]),
    (2, [12, 16])
]


def confirm_full_access(map):
    """Ensure that all nodes on the map can be visited from every other node
    For 'node' read 'island[1]' i.e. each node is a list of other nodes it
    is connected to"""
    visited = [False] * len(map)
    to_visit = []
    current = 0

    while False in visited:
        visited[current] = True
        #print('Visit {} to_visit: {}'.format(current, to_visit))
        for link in map[current]:
            if not visited[link]:
                to_visit.append(link)
        if len(to_visit) >0 :
            current = to_visit.pop()

    return False not in visited


if __name__ == "__main__":
    attempt = []
    idx = 0
    for island in islands:
        attempt.append([])
        for connection in island[1]:
            attempt[idx].append(connection)
        idx += 1

    if confirm_full_access(attempt):
        print(attempt)
