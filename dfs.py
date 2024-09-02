"""
Depth First Search Implementations using:
1. Adjacency list
2. Adjacency Matrix
3. Tree Node
4. Edge List
"""

def dfs_adjacent_list(graph, start_vertex, visited=None):
    """
    Implementation of the Depth First Search algorithm using Adjacency List
    :param graph:
    :param start_vertex:
    :param visited:
    :return:
    """
    if visited is None:
        visited = set()

    visited.add(start_vertex)

    # Process the Vertex/Node i.e Print it
    print(start_vertex, end=" ")

    for neighour in graph[start_vertex]:
        if neighour not in visited:
            dfs_adjacent_list(graph, neighour, visited)

        # At some point when all neighour is in visited then this recursion would end

graph_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs_adjacent_list(graph_list, 'A')


def dfs_adjacent_matrix(graph, start_vertex):
    """
    Implementation of the Depth First Search algorithm using Adjacency Matrix
    :param graph:
    :param start_vertex:
    :return:
    """
    visited = [False] * len(graph)
    stack = [start_vertex]

    while stack:
        # another noticeable difference between depth first search and breath first search
        # is the data structure being used
        # DFS | stack(FILO)
        # BFS | queue(FIFO)
        vertex = stack.pop()
        if not visited[vertex]:

            # Process the vertex i.e print it
            print(vertex, end=" ")

            # Mark it as Visited
            visited[vertex] = True

            # now Push all Adjacent Nodes/vertex that has not being visited onto the stack
            for i in range(len(graph) -1, -1, -1):
                # Reverse Order for consistent Ordering when pop
                if graph[vertex][i] == 1 and not visited[i]:
                    stack.append(i)


# Example graph as an adjacency matrix
graph_matrix = [
    [0, 1, 1, 0, 0, 0], # node/vertex 0
    [1, 0, 0, 1, 1, 0], # node/vertex 1
    [1, 0, 0, 0, 0, 1], # node/vertex 2
    [0, 1, 0, 0, 0, 0], # node/vertex 3
    [0, 1, 0, 0, 0, 1], # node/vertex 4
    [0, 0, 1, 0, 1, 0] # node/vertex 5
]
print()
dfs_adjacent_matrix(graph_matrix, 0)  # Start BFS from vertex 0 (which represents 'A')

# Depth First Search in the context of Tree
print()

class TreeNode:
    """
    A Basic Tree Node Implementation
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_tree(root):
    """
    Depth First Search Implementation using Tree Node structure
    :param root:
    :return:
    """
    if root:
        # Process the Node/vertex i.e print it
        print(root.value, end=" ")

        dfs_tree(root.left)
        dfs_tree(root.right)

# Example tree
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.left = TreeNode('F')

dfs_tree(root)

# Depth First Search in the context of Edge list
print()


def dfs_adjacent_list_from_edge(edges):
    """
    Convert an Edge list into a Adjacency List
    :param edges:
    :return:
    """
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u) # if undirected graph
    return graph

def dfs_edge_list(edges, start_vertex):
    """
    Implementation of the Depth First Search algorithm using Edge List
    :param edges:
    :param start_vertex:
    :return:
    """
    graph = dfs_adjacent_list_from_edge(edges)
    visited = set()
    dfs_adjacent_list(graph, start_vertex, visited)

# Example graph as an edge list
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]

print()
dfs_edge_list(edges, 'A')



# Maze solving with DFS:

def dfs_maze(maze, start_vertex, end_vertex):
    """
    Solution to the Maze problem using DFS Algorithm
    :param maze:
    :param start_vertex:
    :param end_vertex:
    :return:
    """
    # Dimension of the Maze
    rows, cols = len(maze), len(maze[0])

    # stack to keep track of path
    stack = [start_vertex]

    # Set: To keep track of visited node
    visited = set()
    visited.add(start_vertex)

    # Possible direction to move: up, down, left right
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    while stack:
        # get the current position
        vertex = stack.pop()

        # if current position is the end return the truth
        if vertex == end_vertex:
            return True

        # Explore the neighbouring cells
        for direction in directions:
            next_row, next_col = vertex[0] + direction[0], vertex[1] + direction[1]

            next_pos = (next_row, next_col)

            # Check if the next position is within bound and not visited
            if 0 <= next_row < rows and 0 <= next_col < cols and next_pos not in visited:
                if maze[next_row][next_col] == 0:
                    stack.append(next_pos)
                    visited.add(next_pos)
                    print()
                    print(next_pos, end=" ")

    return False


# Example Maze (0: open space, 1: wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting position
end = (4, 4)    # End position

# Run DFS to solve the maze
Found = dfs_maze(maze, start, end)
print("Path found:", Found)
