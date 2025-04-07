class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 0:
        #     return 0

        # longest = 0
        # num_set = set(nums)

        # for num in nums:
        #     if num -1 not in num_set:
        #         current = 1
        #         current_num = num
        #         while current_num + 1 in num_set:
        #             current +=1
        #             current_num +=1
        #         longest = max(current, longest)
        # return longest

        if len(nums) == 0:
            return 0
        longestStreak = 0
        setNum = set(nums)

        for num in nums:
            if num - 1 not in setNum:
                currentStreak = 1
                while num + currentStreak in setNum:
                    currentStreak += 1
                longestStreak = max(longestStreak, currentStreak)
        return longestStreak


value = Solution()
print(value.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(value.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(value.longestConsecutive([1, 2, 0, 1]))
print(value.longestConsecutive([0]))
print(value.longestConsecutive([0, 0]))
print(value.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
print(value.longestConsecutive([]))

# [100,4,200,1,3,2]
# [0,3,7,2,5,8,4,6,0,1]
# [1,2,0,1]
# [0]
# [0,0]
# []
