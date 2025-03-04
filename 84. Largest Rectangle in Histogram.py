class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # maxArea = 0
        # for i in range(len(heights)):
        #     leftMinIndex = i
        #     rightMinIndex = i + 1
        #     while heights[leftMinIndex] >= heights[i] and leftMinIndex >= 0:
        #         leftMinIndex -=1
        #     while rightMinIndex < len(heights) and heights[rightMinIndex] >= heights[i] :
        #         rightMinIndex +=1
        #     leftMinIndex +=1
        #     rightMinIndex -=1
        #     maxArea = max(maxArea, heights[i] * (rightMinIndex - leftMinIndex + 1))
        # return maxArea

        stack = [-1]
        maxArea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)

        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        return maxArea


value = Solution()
print(value.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(value.largestRectangleArea([2, 4]))
