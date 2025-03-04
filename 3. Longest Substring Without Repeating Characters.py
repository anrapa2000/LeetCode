class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        left = 0
        result = 0
        for i in range(len(s)):
            if s[i] in dict:
                left = max(dict[s[i]] + 1, left)
            dict[s[i]] = i
            result = max(result, i - left + 1)
        return result







# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         hash = {}
#         left = 0
#         for i in range(len(s)):
#             if s[i] in hash:





value = Solution()
print(value.lengthOfLongestSubstring("abcabcbb"))
# print(value.lengthOfLongestSubstring("bbbbb"))
# print(value.lengthOfLongestSubstring("pwwkew"))

        