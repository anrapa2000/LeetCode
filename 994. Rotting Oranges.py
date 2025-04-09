import collections


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or grid[0] is None:
            return -1

        rowLength = len(grid)
        columnLength = len(grid[0])
        queue = collections.deque()
        freshOranges = 0
        time = 0

        for row in range(rowLength):
            for column in range(columnLength):
                if grid[row][column] == 2:
                    queue.append((row, column))
                if grid[row][column] == 1:
                    freshOranges += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue and freshOranges > 0:
            for _ in range(len(queue)):
                row, column = queue.popleft()
                for dr, dc in directions:
                    newRow, newColumn = dr + row, dc + column
                    if (
                        newRow < 0
                        or newRow >= rowLength
                        or newColumn < 0
                        or newColumn >= columnLength
                        or grid[newRow][newColumn] != 1
                    ):
                        continue
                    grid[newRow][newColumn] = 2
                    queue.append((newRow, newColumn))
                    freshOranges -= 1
            time += 1

        return time


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
