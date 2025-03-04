class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        values = set(nums)
        return len(values) != len(nums)
    

if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,4]))

        
        