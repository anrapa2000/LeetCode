class Solution(object):
    def canJump(self, nums):
        GOOD, BAD, UNKNOWN = 1, 0, -1
        memo = [UNKNOWN] * len(nums)
        memo[-1] = GOOD
        for i in range(len(nums) - 2, -1, -1):
            print(i, nums[i], i + nums[i])
            furthest_jump = min(i + nums[i], len(nums) - 1)
            print(furthest_jump)
            for j in range(i + 1, furthest_jump + 1):
                print("j", j)
                print("memo", memo)
                if memo[j] == GOOD:
                    memo[i] = GOOD
                    break
        return memo[0] == GOOD


print(Solution().canJump([2, 3, 1, 1, 4]))
