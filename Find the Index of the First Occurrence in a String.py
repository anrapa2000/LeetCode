class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0
        p2 = 0
        while p1 < len(haystack) and p2 < len(needle):
            if haystack[p1] == needle[p2]:
                p1 = p1 + 1
                p2 = p2 + 1
            else:
                p1 = p1 + 1
                p2 = 0
        if p2 == len(needle):
            return p1 - p2
        return -1
value = Solution()
# print(value.strStr("sadbutsad", "sad"))
# print(value.strStr("leetcode", "leeto"))
        
