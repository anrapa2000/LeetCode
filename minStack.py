class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min_stack:
            mini = min(val, self.min_stack[-1])
            self.min_stack.append(mini)
        else:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        """
        :rtype: int
        """

        return self.stack[len(self.stack)-1]

    def getMin(self):
        """
        :rtype: int
        """
        # min = self.stack[0]
        # for i in self.stack:
        #     if i < min:
        #         min = i
        # return min
        # above approach is 0(n)

        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
# obj.push(-4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)