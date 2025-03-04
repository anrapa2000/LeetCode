class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            rowSet = set()
            for j in range(9):
                if board[i][j] in rowSet:
                    print("rowSet", rowSet)
                    print(board[i][j])
                    return False
                if board[i][j] == ".":
                    continue
                rowSet.add(board[i][j])

        for j in range(9):
            colSet = set()
            for i in range(9):
                if board[i][j] in colSet:
                    return False
                if board[i][j] == ".":
                    continue
                colSet.add(board[i][j])

        sqHash = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                square = (i // 3) * 3 + j // 3
                if board[i][j] in sqHash[square]:
                    return False
                sqHash[square].add(board[i][j])
        return True


value = Solution()
dummy = value.isValidSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
print(dummy)
dummy2 = value.isValidSudoku(
    [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
print(dummy2)
