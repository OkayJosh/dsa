"""
Creating a Breadth first search algorithm using the concepts of:
Adjacency List
Adjacency Matrix
Tree
"""
from collections import deque

# Breadth First Search in the context of Adjacency List

def bfs_adjacent_list(graph, start_vertex):
    """
    Breadth First Search Algorithm implementation using the Adjacency List Structure
    :param graph:
    :param start_vertex:
    :return:
    """
    # keep track of visited vertex
    visited  = set()
    # Initialized a queue with the start
    queue = deque([start_vertex])

    while queue:
        vertex = queue.popleft() # This condition allows for at some point the queue would be empty
        if vertex not in visited:
            # process the vertex, in this instance we print it
            print(vertex, end=" ")
            visited.add(vertex)
            # Enqueue all adjacent vertices that has not being visited
            queue.extend(neigbour for neigbour in graph[vertex] if neigbour not in visited)

graph_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs_adjacent_list(graph_list, 'A')

# Breadth First Search in the context of Adjacency Matrix
print()

def bfs_adjacent_matrix(graph, start_vertex):
    """
    Breadth First Search Algorithm implementation using the Adjacency Matrix Structure
    :param graph:
    :param start_vertex:
    :return:
    """
    # Keep Track of visited Vetices
    visited = [False] * len(graph)
    # Initialize a queue with the start_vertex
    queue = deque([start_vertex])

    while queue:
        vertex = queue.popleft()
        if not visited[vertex]:
            # process the vertex e.g print it
            print(vertex, end=" ")
            visited[vertex] = True

            # Enqueue all Adjacent vertex that has not been visited
            for i in range(len(graph)):
                if graph[vertex][i] == 1 and not visited[i]:
                    queue.append(i)


# Example graph as an adjacency matrix
graph_matrix = [
    [0, 1, 1, 0, 0, 0], # node/vertex 0
    [1, 0, 0, 1, 1, 0], # node/vertex 1
    [1, 0, 0, 0, 0, 1], # node/vertex 2
    [0, 1, 0, 0, 0, 0], # node/vertex 3
    [0, 1, 0, 0, 0, 1], # node/vertex 4
    [0, 0, 1, 0, 1, 0] # node/vertex 5
]

bfs_adjacent_matrix(graph_matrix, 0)  # Start BFS from vertex 0 (which represents 'A')

# Breadth First Search in the context of Tree
print()

class TreeNode:
    """
    A Basic Tree Node Implementation
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_tree(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        # process the Node i.e Print it
        print(vertex.value, end=" ")

        # Enqueue the left and right child of the current node
        if vertex.left is not None:
            queue.append(vertex.left)

        if vertex.right is not None:
            queue.append(vertex.right)

# Example tree
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.left = TreeNode('F')

bfs_tree(root)


