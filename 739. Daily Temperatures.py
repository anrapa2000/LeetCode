class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = (i - index) 
            stack.append([temperatures[i], i])
        return result

value = Solution()

print(value.dailyTemperatures([73,74,75,71,69,72,76,73]))
# print(value.dailyTemperatures([30,40,50,60]))
# print(value.dailyTemperatures([30,60,90]))