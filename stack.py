class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        return - 1
    
    def isEmpty(self):
        return len(self.stack) == 0

value = Stack()
value.push(1)
value.push(2)
value.push(3)
print(value.peek())
value.pop()
print(value.peek())
value.push(4)
print(value.isEmpty())
value.pop()
print(value.peek())
print(value.isEmpty())
value.pop()
print(value.peek())
print(value.isEmpty())
value.pop()
print(value.peek())
print(value.isEmpty())

