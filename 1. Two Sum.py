class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums_index = {}
        # for i,n in enumerate(nums):
        #     value = target - n
        #     if value in nums_index:
        #         return [nums_index[value], i]
        #     nums_index[n] = i

        index = {}
        for i in enumerate(nums):
            value = target - nums[i]
            if value in index:
                return [index[value], i]
            index[nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    # print(s.twoSum([2, 7, 11, 15], 9))
    # print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))
    # s.twoSum([3, 3], 6)
