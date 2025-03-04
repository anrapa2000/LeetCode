class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = []
        # nums.sort()

        # for key, value in enumerate(nums):
        #     if key > 0 and value == nums[key - 1]:
        #         continue
        #     left = key + 1
        #     right = len(nums) - 1
        #     while left < right:
        #         threeSum = value + nums[left] + nums[right]
        #         if threeSum > 0:
        #             right -= 1
        #         elif threeSum < 0:
        #             left += 1
        #         else:
        #             result.append([value, nums[left], nums[right]])
        #             left += 1
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1
        # return result

        # res = []
        # hash = {}

        # for key, target in enumerate(nums):
            


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
# print(Solution().threeSum([]))
# print(Solution().threeSum([0]))
print(Solution().threeSum([-1,0,1,0]))
