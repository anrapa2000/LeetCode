# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         hash1 = {}
#         hash2 = {}

#         for i in s:
#             hash1[i] = hash1.get(i, 0) + 1

#         for j in t:
#             hash2[j] = hash2.get(j, 0) + 1

#         return hash1 == hash2

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        for char in set(s):
            print(char)
            if s.count(char) != t.count(char):
                return False

        return True

if __name__ == '__main__':
    print(Solution().isAnagram("anagram", "nagaram"))
