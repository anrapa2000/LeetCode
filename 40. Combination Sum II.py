class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        candidates.sort()

        def backtrack(first, array, remain):
            if remain < 0:
                return
            elif remain == 0:
                output.append(list(array))
                return

            for i in range(first, len(candidates)):
                if candidates[i] == candidates[i - 1] and i > first:
                    continue
                array.append(candidates[i])
                backtrack(i + 1, array, remain - candidates[i])
                array.pop()

        backtrack(0, [], target)
        return output


value = Solution().combinationSum2([2, 5, 2, 1, 2], 5)
print(value)
