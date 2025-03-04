class Node:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.value = value
        self.key = key


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.hash = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, value):
        if key in self.hash:
            node = self.hash[key]
            self.remove(node)

        if len(self.hash) >= self.capacity:
            delNode = self.head.next
            self.remove(delNode)
            del self.hash[delNode.key]

        newNode = Node(key, value)
        self.add(newNode)
        self.hash[key] = newNode

        print(self.hash)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.hash:
            return -1
        self.remove(self.hash[key])
        self.add(self.hash[key])
        return self.hash[key].value


# obj = LRUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))
# obj.put(3, 3)
# print(obj.get(2))
# obj.put(4, 4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

obj = LRUCache(2)
print(obj.get(2))
obj.put(2, 6)
print(obj.get(1))
obj.put(1, 5)
obj.put(1, 2)
print(obj.get(1))
print(obj.get(2))
