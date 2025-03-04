class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_string = ''
        i = j = 0
        while(i < len(word1) and j < len(word2)):
            merged_string += word1[i] + word2[j]
            i += 1
            j += 1
        
        if i < len(word1):
            merged_string += word1[i:]
        if j < len(word2):
            merged_string += word2[j:]
        return merged_string
value = Solution().mergeAlternately("abc", "pqrs")
print(value)