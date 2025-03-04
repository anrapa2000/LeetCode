class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rowLength = len(board)
        columnLength = len(board[0])

        for i in range(rowLength):
            for j in range(columnLength):
                if self.dfs(i, j, board, word, 0):
                    return True
        return False

    def dfs(self, row, column, board, word, stringLengthPlace):
        if stringLengthPlace == len(word):
            return True
        if (
            row >= len(board)
            or row < 0
            or column >= len(board[0])
            or column < 0
            or board[row][column] != word[stringLengthPlace]
        ):
            return False

        temp = board[row][column]
        board[row][column] = "0"

        if (
            self.dfs(row, column + 1, board, word, stringLengthPlace + 1)
            or self.dfs(row, column - 1, board, word, stringLengthPlace + 1)
            or self.dfs(row + 1, column, board, word, stringLengthPlace + 1)
            or self.dfs(row - 1, column, board, word, stringLengthPlace + 1)
        ):
            return True

        board[row][column] = temp
        return False


value = Solution()
print(
    value.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
)
print(
    value.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
    )
)
print(
    value.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
)
