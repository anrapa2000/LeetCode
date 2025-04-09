# BFS
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         numberofIslands = 0
#         rowLength = len(grid)
#         columnLength = len(grid[0])
#         queue = []
#         for row in range(rowLength):
#             for column in range(columnLength):
#                 if grid[row][column] == '1':
#                     grid[row][column] = '0'
#                     numberofIslands +=1
#                     queue.append((row, column))
#                     while queue:
#                         current_row, current_column = queue.pop(0)
#                         if current_row+1 < rowLength and grid[current_row+1][current_column] == '1' :
#                             queue.append((current_row+1, current_column))
#                             grid[current_row+1][current_column] = '0'
#                         if current_column+1<columnLength and grid[current_row][current_column+1] =='1':
#                             queue.append((current_row, current_column+1))
#                             grid[current_row][current_column+1] = '0'
#                         if current_row - 1 >= 0 and grid[current_row-1][current_column] == '1' :
#                             queue.append((current_row-1, current_column))
#                             grid[current_row-1][current_column] = '0'
#                         if current_column - 1 >= 0 and grid[current_row][current_column-1] =='1':
#                             queue.append((current_row, current_column-1))
#                             grid[current_row][current_column-1] = '0'
#         return numberofIslands

# DFS
class Solution(object):
    def numIslands(self, grid):
        if grid is None or grid[0] is None:
            return 0
        rowLength = len(grid)
        columnLength = len(grid[0])
        numberOfIslands = 0

        def dfs(row, column):
            if (
                row >= rowLength
                or row < 0
                or column >= columnLength
                or column < 0
                or grid[row][column] != "1"
            ):
                return
            grid[row][column] = "0"
            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

        for row in range(rowLength):
            for column in range(columnLength):
                if grid[row][column] == "1":
                    dfs(row, column)
                    numberOfIslands += 1
        return numberOfIslands


value = Solution()
print(
    value.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print(
    value.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
print(value.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
print(value.numIslands([["1", "0", "1", "1", "0", "1", "1"]]))
print(
    value.numIslands(
        [
            [
                "1",
                "0",
                "0",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
            ],
            [
                "1",
                "0",
                "0",
                "1",
                "1",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "0",
                "0",
                "1",
                "0",
            ],
            [
                "0",
                "0",
                "0",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "0",
                "1",
                "1",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
            ],
            [
                "0",
                "0",
                "0",
                "1",
                "1",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
                "1",
                "1",
                "0",
                "0",
                "1",
                "0",
                "0",
                "1",
            ],
            [
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "1",
                "1",
                "1",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
            ],
            [
                "1",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "1",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
            ],
            [
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
            ],
            [
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "0",
                "1",
                "1",
                "0",
                "1",
                "0",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "0",
            ],
            [
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "1",
                "1",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
            ],
            [
                "0",
                "0",
                "1",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
                "0",
            ],
            [
                "1",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "0",
            ],
            [
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "0",
                "0",
            ],
            [
                "1",
                "1",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
            ],
            [
                "0",
                "1",
                "0",
                "0",
                "1",
                "1",
                "1",
                "0",
                "0",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "0",
                "0",
                "0",
            ],
            [
                "0",
                "0",
                "1",
                "1",
                "1",
                "0",
                "0",
                "0",
                "1",
                "1",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
            ],
            [
                "1",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "1",
            ],
            [
                "1",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
            ],
            [
                "0",
                "1",
                "1",
                "0",
                "0",
                "0",
                "1",
                "1",
                "1",
                "0",
                "1",
                "0",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "0",
                "0",
            ],
            [
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "1",
                "1",
                "0",
                "0",
                "1",
                "0",
                "1",
                "0",
                "0",
                "1",
                "0",
                "0",
                "1",
                "1",
            ],
            [
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "0",
                "0",
                "0",
                "1",
                "1",
                "0",
                "0",
                "0",
            ],
        ]
    )
)
