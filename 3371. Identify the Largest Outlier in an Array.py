# class Solution(object):
#     def getLargestOutlier(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         total = sum(nums)
#         result = float("-inf")
#         hash = {}

#         for j in nums:
#             if j in hash:
#                 hash[j] = hash[j] + 1
#             else:
#                 hash[j] = 1

#         for i in range(len(nums)):
#             outlier = total - nums[i] - nums[i]
#             if outlier in hash and (hash[nums[i]] > 1 or outlier != nums[i]):
#                 result = max(result, outlier)
#         return result


class Solution:
    def getLargestOutlier(self, nums):
        total = sum(nums)
        result = float("-inf")
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        for i in range(len(nums)):
            value = total - (nums[i] * 2)
            if value in hash and (hash[nums[i]] > 1 or value != nums[i]):
                result = max(result, value)
        return result


value = Solution()
print(value.getLargestOutlier([2, 3, 5, 10]))  # 10
print(value.getLargestOutlier([-2, -1, -3, -6, 4]))  # 4
print(value.getLargestOutlier([6, -31, 50, -35, 41, 37, -42, 13]))  # -35
print(value.getLargestOutlier([1, 1, 1, 1, 1, 5, 5]))  # 5
