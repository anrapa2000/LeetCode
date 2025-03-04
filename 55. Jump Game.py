# from typing import List


# class Solution:
#     def canJumpFromPos(self, position, nums):
#         if position == len(nums) - 1:
#             return True
#         furthestPos = min(nums[position] + position, len(nums) - 1)
#         for i in range(position + 1, furthestPos + 1):
#             if self.canJumpFromPos(i, nums):
#                 return True
#             return False

#     def canJump(self, nums: List[int]) -> bool:
#         return self.canJumpFromPos(0, nums)


# class Solution:
#     def __init__(self):
#         self.nums = []
#         self.memo = []

#     def canJumpPosition(self, position):
#         if position == len(self.nums) - 1:
#             return True
#         furthestPosition = min(position + self.nums[position], len(self.nums) - 1)
#         for i in range(position + 1, furthestPosition + 1):
#             if self.canJumpPosition(i):
#                 self.memo[position] = 1
#                 return True
#         self.memo[position] = 0
#         return False

#     def canJump(self, nums):
#         self.nums = nums
#         self.memo = [-1] * len(nums)
#         self.memo[-1] = 1
#         return self.canJumpPosition(0)


# class Solution:
#     def canJump(self, nums):
#         memo = [-1] * len(nums)
#         memo[-1] = 1
#         for i in range(len(nums) - 2, -1, -1):
#             furthestPos = min(nums[i] + i, len(nums) - 1)
#             for j in range(i + 1, furthestPos + 1):
#                 if memo[j] == 1:
#                     memo[i] = 1
#                     break
#         return memo[0] == 1


class Solution:
    def canJump(self, nums):
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= lastPos:
                lastPos = i
        return lastPos == 0


print(Solution().canJump([2, 3, 1, 1, 4]))
print(Solution().canJump([3, 2, 1, 0, 4]))
