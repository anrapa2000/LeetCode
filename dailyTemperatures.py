class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answers = [0] * len(temperatures)

        for i,j in enumerate(temperatures):
            while stack and j > stack[-1][0]:
                a, b = stack.pop()
                answers[b] = i - b
            else: 
                stack.append((j, i))
        return answers


value = Solution()

print(value.dailyTemperatures([73,74,75,71,69,72,76,73]))
# print(value.dailyTemperatures([30,40,50,60]))
# print(value.dailyTemperatures([30,60,90]))