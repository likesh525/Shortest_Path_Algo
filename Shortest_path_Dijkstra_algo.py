def create_graph_from_matrix(matrix, nodes):
    graph = {}
    for i, node in enumerate(nodes):
        neighbors = []
        for j, weight in enumerate(matrix[i]):
            if weight > 0:  #
                neighbors.append((nodes[j], weight))
        graph[node] = neighbors
    return graph

matrix = [
    [0, 5, 3, 0, 11, 0],  # A
    [5, 0, 1, 0, 0, 2],   # B
    [3, 1, 0, 1, 5, 0],   # C
    [0, 0, 1, 0, 9, 3],   # D
    [11, 0, 5, 9, 0, 0],  # E
    [0, 2, 0, 3, 0, 0]    # F
]

# Corresponding nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

my_graph = create_graph_from_matrix(matrix, nodes)


def shortest_path(graph, start, target=''):
    unvisited = list(graph) # a copy of the graph, list of all the nodes used
    distances = {node: 0 if node == start else float('inf') for node in graph} # distance from each starting node,
    # set to zero for starting node
    paths = {node: [] for node in graph} # keep track of shortest path from starting point
    paths[start].append(start)

    while unvisited: # True as long as unvisited is empty
        current = min(unvisited, key=distances.get) # finds minimum distance node from the starting value
        for node, distance in graph[current]: # referring node and the distance of the shortest node
            if distance + distances[current] < distances[node]: # calculate the potential distance and compare that
                # with calculated distance, if lower then stop
                distances[node] = distance + distances[current] # updating the value
                if paths[node] and paths[node][-1] == node: # checks and replaces the last node value
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current) # removes the node

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start: # doesn't print the distance from starting node
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths

shortest_path(my_graph, 'F')

