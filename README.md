# Shortest Path Algorithm

This script is designed to solve the shortest path problem using Dijkstra's Algorithm. The script contains two main functions: one to create a graph from an adjacency matrix, and the other to compute the shortest path. If you already have the matrix created, you can proceed directly to the main function.

## Function 1: Create Graph from Adjacency Matrix

This function converts an adjacency matrix into a graph representation.

### How to Use

Enter the adjacency matrix in the standard format:

```python
matrix = [
    [0, 5, 3, 0, 11, 0],  # A
    [5, 0, 1, 0, 0, 2],   # B
    [3, 1, 0, 1, 5, 0],   # C
    [0, 0, 1, 0, 9, 3],   # D
    [11, 0, 5, 9, 0, 0],  # E
    [0, 2, 0, 3, 0, 0]    # F
]
```

Define nodes as list : 

``` nodes = ['A', 'B', 'C', 'D', 'E', 'F'] ```

Then, call the create_graph_from_matrix(matrix, nodes) function.

## Function 2: Main function.
Once the matrix is defined proceed with the the main function call.
```
shortest_path(graph, start, target=''):
```
**Parameters:**

**graph**: The graph represented by the adjacency matrix.

**start**: The starting node — specify the node from which you want to start finding the shortest path.

**target (optional)**: The target node — specify the node to find the shortest path between the start and target. If omitted, the function will find the shortest paths to all nodes.
