# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         # solution 1 - O(n^2)
#         # value = 0
#         # for i in range(0, len(height)):
#         #     l = r = height[i]
#         #     for j in range(0, i):
#         #         if height[j] > l:
#         #             l = height[j]

#         #     for k in range(i + 1, len(height)):
#         #         if height[k] > r:
#         #             r = height[k]

#         #     value = value + min(l, r) - height[i]
#         # return value

#         #Solution 2 - using stack
#         value = 0
#         stack = []
#         stack.append(height[0])
#         for i in range(1, len(height) - 1):
#             if height[i] > stack[-1]:
#                 key = stack.pop()
#                 sum = min(height[i], key)
#                 value += height[i] - sum
#                 stack.append(height[i])
# return value

# class Solution:
#     def trap(self, height):
#         ans = 0
#         current = 0
#         st = []
#         while current < len(height):
#             while len(st) != 0 and height[current] > height[st[-1]]:
#                 top = st[-1]
#                 st.pop()
#                 if len(st) == 0:
#                     break
#                 distance = current - st[-1] - 1
#                 print("distance", distance)
#                 bounded_height = (
#                     min(height[current], height[st[-1]]) - height[top]
#                 )
#                 print("bounded_height", bounded_height)
#                 ans += distance * bounded_height
#             print("current", current)
#             st.append(current)
#             print("stack", st)
#             current += 1
#         return ans


class Solution:
    def trap(self, height):
        value = 0
        stack = []
        i = 0
        while i < len(height):
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                value += distance * bounded_height
            stack.append(i)
            i += 1
        return value


value = Solution()
print(value.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(value.trap([4, 2, 0, 3, 2, 5]))
