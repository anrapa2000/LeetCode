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

        #     result = []
        #     nums.sort()

        #     for i in range(len(nums)):
        #         if i == 0 or nums[i - 1] != nums[i]:
        #             self.twoSumSorted(nums, i, result)
        #     return result

        # def twoSumSorted(self, nums, i, result):
        #     low = i + 1
        #     high = len(nums) - 1

        #     while low < high:
        #         sum = nums[low] + nums[i] + nums[high]
        #         if sum == 0:
        #             result.append([nums[i], nums[low], nums[high]])
        #             low += 1
        #             high -= 1
        #             while low < high and nums[low] == nums[low - 1]:
        #                 low += 1
        #         elif sum > 0:
        #             high -= 1
        #         else:
        #             low += 1

        result = []
        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, result)
        return result

    def twoSum(self, nums, i, result):
        map = set()
        j = i + 1
        while j < len(nums):
            value = -nums[i] - nums[j]
            if value in map:
                result.append([nums[i], value, nums[j]])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            map.add(nums[j])
            j += 1


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
# print(Solution().threeSum([]))
# print(Solution().threeSum([0]))
# print(Solution().threeSum([-1, 0, 1, 0]))
