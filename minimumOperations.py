class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        count = 0
        hash = {}
        while(i < len(nums)):
            if nums[i] in hash:
                j = j + 3
                i = j
                count +=1
                hash = {}
                continue
            else: 
                hash[nums[i]] = 1
                i = i+1
        return count

value = Solution()
print(value.minimumOperations([1,2,3,4,2,3,3,5,7]))
print(value.minimumOperations([4,5,6,4,4]))
print(value.minimumOperations([6,7,8,9]))
