class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <=1:
            return False
        dict = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        stack = []
        for i in s:
            if(i in dict):
                stack.append(i)
            elif len(stack)==0:
                return False
            else:
                openBracket = stack.pop()
                if(dict[openBracket] != i): 
                    return False
        if len(stack) == 0: 
            return True
        else: 
            return False


value = Solution()
print(value.isValid("()"))
print(value.isValid("()[]{}"))
print(value.isValid("(]"))
print(value.isValid("([])"))
print(value.isValid("){"))
print(value.isValid("(){}}{"))
