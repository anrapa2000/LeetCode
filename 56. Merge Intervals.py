class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])

        return output


        
value = Solution()      
# print(value.merge([[1,3],[2,6],[15,18],[8,10]]))
# print(value.merge([[1,4],[4,5]]))
print(value.merge([[1,4],[0,0]]))
print(value.merge([[1,3], [2,6] ,[8,10] ,[8,9], [9,11],[15,18], [2,4] ,[16,17]]))


