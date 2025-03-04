from typing import List


# class Solution:
#     def dfs(self, visited, stack, key, adjList, result, pathStack):
#         stack.append(key)
#         visited[key] = True
#         pathStack[key] = True

#         for node in adjList[key]:
#             if not visited[node]:
#                 if self.dfs(visited, stack, node, adjList, result, pathStack):
#                     return True
#             elif pathStack[node]:
#                 return True

#         pathStack[key] = False
#         result.append(stack.pop())
#         return False

#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         adjList = [[] for _ in range(numCourses)]

#         for prerequisite in prerequisites:
#             adjList[prerequisite[1]].append(prerequisite[0])

#         stack = []
#         result = []
#         visited = [False] * numCourses
#         pathStack = [False] * numCourses

#         for key in range(numCourses):
#             if not visited[key]:
#                 if self.dfs(visited, stack, key, adjList, result, pathStack):
#                     return []

#         result.reverse()
#         return result

from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        result = []

        for prerequisite in prerequisites:
            adjList[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = deque()
        nodesVisited = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            value = queue.popleft()
            result.append(value)
            nodesVisited += 1
            for neighbour in adjList[value]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if nodesVisited < numCourses:
            return []
        else:
            return result


print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(Solution().findOrder(2, [[1, 0], [0, 1]]))
