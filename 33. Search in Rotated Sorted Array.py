from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid

        #     if nums[mid] > nums[right]:
        #         if nums[left] <= target < nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     else:
        #         if nums[mid] < target <= nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        # return -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
# print(Solution().search(nums = [4,5,6,7,0,1,2], target = 3))
# print(Solution().search(nums = [1], target = 0))
