class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dict = {}
        # left = 0
        # result = 0
        # for i in range(len(s)):
        #     if s[i] in dict:
        #         left = max(dict[s[i]] + 1, left)
        #     dict[s[i]] = i
        #     result = max(result, i - left + 1)
        # return result

        setLength = set()
        maxSub = 0
        left = 0
        for i in range(len(s)):
            while s[i] in setLength:
                setLength.remove(s[left])
                left += 1
            setLength.add(s[i])
            maxSub = max(maxSub, i - left + 1)
        return maxSub


value = Solution()
# print(value.lengthOfLongestSubstring("abcabcbb"))
# print(value.lengthOfLongestSubstring("bbbbb"))
print(value.lengthOfLongestSubstring("pwwkew"))
