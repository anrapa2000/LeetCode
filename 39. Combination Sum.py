class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []

        def backtrack(first, array, remains):
            if remains < 0:
                return
            elif remains == 0:
                dummy = array.copy()
                output.append(dummy)

            for i in range(first, len(candidates)):
                array.append(candidates[i])
                backtrack(i, array, remains - candidates[i])
                array.pop()

        backtrack(0, [], target)
        return output


dummy = Solution().combinationSum([3, 4, 5], 8)
print(dummy)
