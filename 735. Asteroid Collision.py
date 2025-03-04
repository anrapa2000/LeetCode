from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            while stack and val < 0 < stack[-1]:
                if -val > stack[-1]:
                    stack.pop()
                    continue
                elif -val == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(val)

        return stack


print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([-1, -2, 2, 1]))
print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
