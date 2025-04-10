# class Solution(object):
#     def dfs(self, visited, recursionStack, adjList, node):
#         visited[node] = True
#         recursionStack[node] = True
#         for neighbor in adjList[node]:
#             if not visited[neighbor]:
#                 if self.dfs(visited, recursionStack, adjList, neighbor):
#                     return True
#             elif recursionStack[neighbor]:
#                 return True
#         recursionStack[node] = False
#         return False

#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
#         if len(prerequisites) == 0:
#             return True

#         adjList = [[] for _ in range(numCourses)]

#         for i in prerequisites:
#             adjList[i[1]].append(i[0])

#         visited = [False] * numCourses
#         recursion_stack = [False] * numCourses

#         for i in range(numCourses):
#             if not visited[i]:
#                 if self.dfs(visited, recursion_stack, adjList, i):
#                     return False
#         return True

# from collections import deque
# class Solution:
#     def canFinish(self, numCourses, prerequisites):
#         inDegree = [0] * numCourses
#         adjList = [[] for _ in range(numCourses)]

#         for prerequisite in prerequisites:
#             adjList[prerequisite[1]].append(prerequisite[0])
#             inDegree[prerequisite[0]] += 1

#         queue = deque()

#         for i in range(numCourses):
#             if inDegree[i] == 0:
#                 queue.append(i)

#         nodesVisited = 0

#         while queue:
#             node = queue.popleft()
#             nodesVisited += 1
#             for neighbour in adjList[node]:
#                 inDegree[neighbour] -= 1
#                 if inDegree[neighbour] == 0:
#                     queue.append(neighbour)

#         return nodesVisited == numCourses


# class Solution:
#     def dfs(self, visited, pathStack, key, adjList):
#         visited[key] = True
#         pathStack[key] = True

#         for node in adjList[key]:
#             if not visited[node]:
#                 if self.dfs(visited, pathStack, node, adjList):
#                     return True
#             elif pathStack[node]:
#                 return True
#         pathStack[key] = False
#         return False

#     def canFinish(self, numCourses, prerequisites):
#         if len(prerequisites) == 0:
#             return True

#         visited = [False] * numCourses
#         pathStack = [False] * numCourses
#         adjList = [[] for _ in range(numCourses)]

#         for prerequisite in prerequisites:
#             adjList[prerequisite[1]].append(prerequisite[0])

#         for key in range(numCourses):
#             if not visited[key]:
#                 if self.dfs(visited, pathStack, key, adjList):
#                     return False
#         return True


class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjList = [[] for _ in range(numCourses)]
        visited = [False] * (numCourses)
        for prerequisite in prerequisites:
            adjList[prerequisite[1]].append(prerequisite[0])

        visitedCoursesPath = [False] * numCourses

        def dfs(node):
            if visitedCoursesPath[node]:
                return False
            if visited[node]:
                return True
            visitedCoursesPath[node] = True
            for neighbour in adjList[node]:
                value = dfs(neighbour)
                if value is False:
                    return False
            visitedCoursesPath[node] = False
            visited[node] = True
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


value = Solution().canFinish(2, [[1, 0], [0, 1]])
value = Solution().canFinish(2, [[1, 0]])
value = Solution().canFinish(1, [])
value = Solution().canFinish(2, [[0, 1]])
value = Solution().canFinish(3, [[0, 1], [0, 2], [1, 2]])
value = Solution().canFinish(3, [[0, 1], [1, 2], [2, 0]])
value = Solution().canFinish(3, [[1, 0], [2, 1], [2, 0]])
value = Solution().canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
value = Solution().canFinish(
    20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
)

print(value)
