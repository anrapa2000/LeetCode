from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hour_eating = 0

            for pile in piles:
                hour_eating += math.ceil(pile / mid)
            print(hour_eating)

            if hour_eating <= h:
                right = mid
            else:
                left = mid + 1

        return right


value = Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8)
print(value)
