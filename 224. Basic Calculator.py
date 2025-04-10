class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operand = 0
        sign = 1
        result = 0

        for char in s:
            if char.isdigit():
                operand = (10 * operand) + int(char)

            elif char == "+":
                result += operand * sign
                sign = 1
                operand = 0

            elif char == "-":
                result += operand * sign
                sign = -1
                operand = 0

            elif char == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0

            elif char == ")":
                result += sign * operand
                result *= stack.pop()
                result += stack.pop()
                sign = 1
                operand = 0
        return sign * operand + result


# print(Solution().calculate("1 + 1"))
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
