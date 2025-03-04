from collections import defaultdict

class detectCycle:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, visited, recursion_stack, node):
        visited[node] = True
        recursion_stack[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.is_cyclic_util(visited, recursion_stack, neighbor):
                    return True
            elif recursion_stack[neighbor]:
                return True

        recursion_stack[node] = False
        return False

    def isCyclic(
        self,
    ):
        visited = [False] * self.vertices
        recursion_stack = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                if self.is_cyclic_util(visited, recursion_stack, i):
                    return True
        return False


graphImp = detectCycle(4)
graphImp.add_edge(0, 1)
graphImp.add_edge(0, 2)
graphImp.add_edge(1, 2)
graphImp.add_edge(2, 0)
graphImp.add_edge(2, 3)
graphImp.add_edge(3, 3)

if graphImp.isCyclic():
    print("True")
else:
    print("False")
