from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLength = len(matrix)
        columnLength = len(matrix[0])
        length = rowLength * columnLength
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            element = matrix[mid // columnLength][mid % columnLength]
            print(element)
            if element == target:
                return True
            elif element > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


value = Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
print(value)
