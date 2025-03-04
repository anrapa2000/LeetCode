class MinHeap():
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2
    
    def leftChild(self, index):
        return 2 * index + 1
    
    def rightChild(self, index):
        return 2 * index + 2
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        temp = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return temp
    
    def heapify_down(self, index):
        smallValue = index
        left = self.leftChild(index)
        right = self.rightChild(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallValue]:
            smallValue = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallValue]:
            smallValue = right

        if smallValue!=index:
            self.heap[smallValue], self.heap[index] = self.heap[index], self.heap[smallValue]
            self.heapify_down(smallValue)

    def get_min(self):
        if self.is_empty():
            return "Heap is empty"
        return self.heap[0]
    
    def size(self):
        return len(self.heap)

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False
    
    def display(self):
        print(self.heap)

heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(2)

heap.display()  # Output: [2, 5, 20, 10]

print(heap.get_min())  # Output: 2

print(heap.extract_min())  # Output: 2
heap.display()  # Output: [5, 10, 20]