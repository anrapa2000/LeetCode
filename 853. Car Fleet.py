from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(pos, sp) for pos, sp in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            timeTaken = (target - p) / s
            if len(stack) == 0:
                stack.append(timeTaken)
            elif timeTaken > stack[-1]:
                stack.append(timeTaken)
        return len(stack)


value = Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
# # value = Solution().carFleet(100, [0,2,4], [4,2,1])
# value = Solution().carFleet(target=10, position=[3], speed=[3])
print(value)
