class MyQueue(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
    
    def push(self, x):
        self.stack_1.append(x)

    def pop(self):
        if self.stack_2 is not None:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()
        else:
            while self.stack_2:
                self.stack_1.append(self.stack_2.pop())
            return self.stack_1.pop()
    
    def peek(self):
        if self.stack_1:
            return self.stack_1[0]
        else:
            return self.stack_2[0]
    
    def empty(self):
        if len(self.stack_1) == 0 and len(self.stack_2)==0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
# print(param_2)
obj.push(5)
# param_3 = obj.pop()
# print(param_3)
# param_4 = obj.pop()
# print(param_4)
# param_5 = obj.pop()
# print(param_5)
# param_6 = obj.pop()
# print(param_6)
# param_4 = obj.empty()