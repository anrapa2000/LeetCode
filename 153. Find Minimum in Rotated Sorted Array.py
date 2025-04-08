from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums) - 1
        # if nums[left] < nums[right]:
        #     return nums[left]

        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return nums[left]

        left = 0
        right = len(nums)-1
        result = float("inf")
        while left < right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            mid = (left + right) // 2
            if nums[mid] < result:
                result = nums[mid]
            elif nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return result


print(Solution().findMin(nums=[3, 4, 5, 1, 2]))
print(Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(Solution().findMin(nums=[11, 13, 15, 17]))
