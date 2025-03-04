# class Solution:
#     def subsets(self, nums):
#         output = [[]]
#         for num in nums:
#             newSubsets = []
#             for curr in output:
#                 temp = curr.copy()
#                 temp.append(num)
#                 newSubsets.append(temp)

#             for curr in newSubsets:
#                 output.append(curr)
#         return output

# class Solution:
#     def subsets(self, nums):
#         self.output = []
#         self.n = len(nums)
#         self.backtrack(0, [], nums)
#         return self.output

#     def backtrack(self, first, curr, nums):
#         # Add the current subset to the output
#         print("beginning of the function - curr", curr)
#         self.output.append(curr[:])
#         print("output", self.output)
#         # Generate subsets starting from the current index
#         for i in range(first, self.n):
#             print("i", i)
#             curr.append(nums[i])
#             print("Inside for loop - curr", curr)
#             self.backtrack(i + 1, curr, nums)
#             curr.pop()
#             print("curr after popping", curr)


class Solution:
    def subsets(self, nums):
        self.output = []
        self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first, curr, nums):
        self.output.append(curr[:])
        for i in range(first, len(nums)):
            print(i)
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()


value = Solution()
dummy = value.subsets([1, 2, 3])
print(dummy)
