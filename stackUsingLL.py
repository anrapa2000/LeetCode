class Node(object):
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp
    
    def peek(self):
        if self.head is None:
            return -1
        return self.head.data
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False

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