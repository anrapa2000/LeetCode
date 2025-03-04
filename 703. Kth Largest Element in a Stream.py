# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.min_heap = nums[:]
#         self._heapify()  # Build the heap from the initial nums list

#         # Add remaining elements until the size of min_heap is k
#         for num in self.min_heap:
#             self.add(num)

#     def _heapify(self):
#         # Convert the list into a min-heap by calling a helper method
#         n = len(self.min_heap)
#         for i in range(n//2 - 1, -1, -1):
#             self._sift_down(i)

#     def _sift_down(self, i):
#         # Manually move the element at index i down to maintain the min-heap property
#         n = len(self.min_heap)
#         while 2 * i + 1 < n:
#             left_child = 2 * i + 1
#             right_child = 2 * i + 2
#             smallest = i

#             if left_child < n and self.min_heap[left_child] < self.min_heap[smallest]:
#                 smallest = left_child
#             if right_child < n and self.min_heap[right_child] < self.min_heap[smallest]:
#                 smallest = right_child

#             if smallest == i:
#                 break
#             else:
#                 # Swap and move the element down
#                 self.min_heap[i], self.min_heap[smallest] = self.min_heap[smallest], self.min_heap[i]
#                 i = smallest

#     def add(self, val: int) -> int:
#         if len(self.min_heap) < self.k:
#             # If we have space, just append the new element
#             self.min_heap.append(val)
#             self._sift_up(len(self.min_heap) - 1)
#         elif val > self.min_heap[0]:
#             # Replace the smallest element (root of the heap)
#             self.min_heap[0] = val
#             self._sift_down(0)

#         return self.min_heap[0]

#     def _sift_up(self, i):
#         # Move the element at index i up to restore the min-heap property
#         while i > 0:
#             parent = (i - 1) // 2
#             if self.min_heap[i] >= self.min_heap[parent]:
#                 break
#             # Swap and move the element up
#             self.min_heap[i], self.min_heap[parent] = self.min_heap[parent], self.min_heap[i]
#             i = parent


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.minHeap = []

        for num in nums:
            self.add(num)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.minHeap[index] < self.minHeap[parent]:
                self.minHeap[index], self.minHeap[parent] = (
                    self.minHeap[parent],
                    self.minHeap[index],
                )
                index = parent
            else:
                break

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallValue = index

        if left < self.k and self.minHeap[left] < self.minHeap[smallValue]:
            smallValue = left

        if right < self.k and self.minHeap[right] < self.minHeap[smallValue]:
            smallValue = right

        if smallValue != index:
            self.minHeap[smallValue], self.minHeap[index] = (
                self.minHeap[index],
                self.minHeap[smallValue],
            )
            self.heapify_down(smallValue)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.minHeap) < self.k:
            self.minHeap.append(val)
            self.heapify_up(len(self.minHeap) - 1)
        elif val > self.minHeap[0]:
            self.minHeap[0] = val
            self.heapify_down(0)
        return self.minHeap[0]


value = KthLargest(3, [4, 5, 8, 2])
print(value.add(3))
print(value.add(5))
print(value.add(10))
print(value.add(9))
print(value.add(4))


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
