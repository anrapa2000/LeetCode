from collections import Counter
import heapq


# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         priorityQueue = [(-count, char) for char, count in Counter(s).items()]
#         heapq.heapify(priorityQueue)
#         result = []

#         while priorityQueue:
#             count_1, char_1 = heapq.heappop(priorityQueue)
#             if char_1 not in result or result[-1] != char_1:
#                 result.append(char_1)
#                 count_1 = count_1 + 1
#                 if count_1 != 0:
#                     heapq.heappush(priorityQueue, (count_1, char_1))
#             else:
#                 if not priorityQueue:
#                     return ""
#                 count_2, char_2 = heapq.heappop(priorityQueue)
#                 if char_2 not in result or result[-1] != char_2:
#                     result.append(char_2)
#                     count_2 = count_2 + 1
#                 if count_2 != 0:
#                     heapq.heappush(priorityQueue, (count_2, char_2))
#                 heapq.heappush(priorityQueue, (count_1, char_1))
#         return "".join(result)


class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)
        maxCount, maxCountChar = 0, ""
        result = [""] * len(s)
        index = 0

        for char, count in char_count.items():
            if count > maxCount:
                maxCount = count
                maxCountChar = char

        if maxCount > (len(s) + 1) // 2:
            return ""

        while char_count[maxCountChar] != 0:
            result[index] = maxCountChar
            char_count[maxCountChar] -= 1
            index += 2

        for char, count in char_count.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                result[index] = char
                count -= 1
                index += 2
    
        return "".join(result)


print(Solution().reorganizeString("aab"))
print(Solution().reorganizeString("aaab"))

