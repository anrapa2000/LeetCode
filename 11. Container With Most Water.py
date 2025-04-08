class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max = 0
        # i = 0
        # k = len(height) - 1
        # while i < k:
        #     area = min(height[i], height[k]) * (k - i)
        #     if area > max: 
        #         max = area
        #     if height[i] < height[k]:
        #         i+=1
        #     else:
        #         k-=1
        # return max
        
        
        
        
        
        
        
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(area, maxArea)
            if height[left]<height[right]:
                left +=1
            else: 
                right -=1
        return maxArea
        
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))       