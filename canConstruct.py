class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = {}
        for i in magazine:
            if i in hash:
                hash[i] +=1
            else:
                hash[i] = 1
        for i in ransomNote:
            if i not in hash:
                return False
            if hash[i] == 0:
                return False
            hash[i] -= 1
        return True
value = Solution()
print(value.canConstruct("a", "b"))
print(value.canConstruct("aa", "ab"))
print(value.canConstruct("aa", "aab"))

