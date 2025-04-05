class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        countMap = {}
        result = 0

        for right in range(len(s)):
            countMap[s[right]] = 1 + countMap.get(s[right], 0)
            if (right - left + 1) - max(countMap.values()) > k:
                countMap[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("AABABBA", 1))