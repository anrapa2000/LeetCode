class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []

        def backtrack(array):
            if len(array) == len(nums):
                output.append(list(array))
                return
            for i in range(len(nums)):
                if nums[i] not in array:
                    array.append(nums[i])
                    backtrack(array)
                    array.pop()

        backtrack([])
        return output


value = Solution().permute([1, 2, 3])
print(value)
