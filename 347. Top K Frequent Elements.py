from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        heap = []
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        for key, value in hash.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                if value > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))

        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result[::-1]

value = Solution()
dummy = value.topKFrequent([1,1,1,2,2,3], 2)
# dummy2 = value.topKFrequent([1], 1)
# dummy3 = value.topKFrequent([1,2], 2)
print(dummy)
# print(dummy2)
# print(dummy3)