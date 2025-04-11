class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashMap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, value):
        if key in self.hashMap:
            self.remove(self.hashMap[key])

        node = Node(key, value)
        self.hashMap[key] = node
        self.add(node)

        if len(self.hashMap) > self.capacity:
            del self.hashMap[self.head.next.key]
            self.remove(self.head.next)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        end = self.tail.prev
        end.next = node
        node.prev = end
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.hashMap:
            return -1
        node = self.hashMap[key]
        self.remove(node)
        self.add(node)
        return node.val


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
