from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash = {}
        # heap = []
        # for num in nums:
        #     if num in hash:
        #         hash[num] += 1
        #     else:
        #         hash[num] = 1

        # for key, value in hash.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (value, key))
        #     else:
        #         if value > heap[0][0]:
        #             heapq.heappop(heap)
        #             heapq.heappush(heap, (value, key))

        # result = []
        # while heap:
        #     result.append(heapq.heappop(heap)[1])
        # return result[::-1]

        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # arr = []
        # for num, count in freq.items():
        #     arr.append([count, num])
        # arr.sort()

        # result = []
        # while len(result) < k:
        #     result.append(arr.pop()[1])
        # return result

        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # heap = []
        # for num in freq.keys():
        #     heapq.heappush(heap, (num, freq[num]))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # result = []
        # for i in range(k):
        #     result.append(heapq.heappop(heap)[1])
        # return result

        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for n, value in count.items():
            frequency[value].append(n)

        result = []

        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result


value = Solution()
dummy = value.topKFrequent([1, 1, 1, 2, 2, 3], 2)
# dummy2 = value.topKFrequent([1], 1)
# dummy3 = value.topKFrequent([1,2], 2)
print(dummy)
# print(dummy2)
# print(dummy3)
