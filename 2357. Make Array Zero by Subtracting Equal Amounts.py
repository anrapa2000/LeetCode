import heapq
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # count = 0
        # while nums != [0] * len(nums):
        #     min_elem = min([i for i in nums if i > 0])
        #     count += 1
        #     for i in range(0, len(nums)):
        #         if nums[i] == 0:
        #             continue
        #         nums[i] -= min_elem
        # return count

        # heapq.heapify(nums)
        # count = 0
        # while nums:
        #     x = heapq.heappop(nums)
        #     print(x)
        #     if x == 0:
        #         continue
        #     else:
        #         for i in range(len(nums)):
        #             nums[i] -= x
        #     count += 1
        # return count

        return len({num for num in nums if num != 0})


print(Solution().minimumOperations([1, 5, 0, 3, 5]))
