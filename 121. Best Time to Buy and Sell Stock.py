class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float("inf")
        maxPrice = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxPrice:
                maxPrice = price - minPrice
        return maxPrice
    
# print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
