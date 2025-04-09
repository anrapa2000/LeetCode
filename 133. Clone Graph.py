# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            clone = Node(node.val, [])
            visited[node] = clone
            for neighbour in node.neighbours:
                value = dfs(neighbour)
                clone.neighbors.append(value)

        if not node:
            return
        dfs(node)
        return visited[node]
