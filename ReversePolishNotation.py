class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for value in tokens:
                if value == "+":
                    stack.append(stack.pop() + stack.pop())
                elif value == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif value == "/":
                    a, b = stack.pop(), stack.pop()
                    # print(b, a)
                    # print(float(b))
                    # print(float(b)/a)
                    # print(int(float(b)/a))
                    # print(int(b/a))
                    stack.append(int(float(b)/a))
                elif value == "*":
                    stack.append(stack.pop() * stack.pop()) 
                else:
                     stack.append(int(value))
        if len(stack)==1:
            return stack.pop()
        


# value = Solution().evalRPN(["2","1","+","3","*"])
# value2 = Solution().evalRPN(["4","13","5","/","+"])
value3 = Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
# print(value)
# print(value2)
# print(value3)