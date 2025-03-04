class MaxHeap():
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2
    
    def leftChild(self, index):
        return (2 * index) + 1
    
    def rightChild(self, index):
        return (2 * index) + 2
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        print(self.heap[index], self.heap[self.parent(index)])
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_max(self):
        temp = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return temp
    
    def heapify_down(self, index):
        largeValue = index
        left = self.leftChild(index)
        right = self.rightChild(index)
        print("printing index", largeValue, left, right)

        if left < len(self.heap) and self.heap[left] > self.heap[largeValue]:
            largeValue = left

        if right < len(self.heap) and self.heap[right] > self.heap[largeValue]:
            largeValue = right

        if largeValue!=index:
            self.heap[largeValue], self.heap[index] = self.heap[index], self.heap[largeValue]
            self.heapify_down(largeValue)

    def get_max(self):
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

heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(2)

heap.display()  

print(heap.get_max()) 

print(heap.extract_max())  
heap.display() 