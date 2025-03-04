class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        output = []

        def backtrack(index, array):
            if len(array) == len(digits):
                output.append("".join(array))

            if index >= len(digits):
                return
            letters = keyboard[digits[index]]

            for letter in letters:
                array.append(letter)
                backtrack(index + 1, array)
                array.pop()

        backtrack(0, [])
        return output


value = Solution().letterCombinations("23")
print(value)
