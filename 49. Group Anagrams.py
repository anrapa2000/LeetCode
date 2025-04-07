import collections


class Solution(object):
    def groupAnagrams(self, strs):
        # Brute Force
        # result = collections.defaultdict(list)
        # for word in strs:
        #     sortedString = "".join(sorted(word))
        #     result[sortedString].append(word)
        # return result.values()

        result = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(word)
        return result.values()


value = Solution()
print(value.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
