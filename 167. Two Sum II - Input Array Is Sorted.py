class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        array = []
        left1 = 0
        right = len(numbers) - 1
        while left1 < right:
            value = numbers[left1] + numbers[right]
            if value == target:
                array.append(left1+1)
                array.append(right + 1)
                return array
            elif value > target:
                right -=1
            else:
                left1 +=1
        
print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([2,3,4], 6))
print(Solution().twoSum([-1,0], -1))
print(Solution().twoSum([0,0,3,4], 0))

