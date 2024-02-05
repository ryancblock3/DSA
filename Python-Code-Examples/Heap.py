class MaxHeap:
    def __init__(self):
        # Initialize an empty list to represent the heap
        self.heap = []

    def _left_child(self, index):
        # Calculate the index of the left child for a given index
        return 2 * index + 1
    
    def _right_child(self, index):
        # Calculate the index of the right child for a given index
        return 2 * index + 2
    
    def _parent(self, index):
        # Calculate the index of the parent for a given index
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        # Swap elements at two given indices in the heap
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        # Move the element down the heap to maintain the max-heap property
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # Compare with left child and update max_index if necessary
            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            # Compare with right child and update max_index if necessary
            if (right_index < len(self.heap) and
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            
            # If max_index is updated, swap and continue sinking down
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value):
        # Insert a new value into the heap
        self.heap.append(value)
        current = len(self.heap) - 1
        # Move the newly inserted element up the heap to maintain the max-heap property
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        # Remove and return the maximum value (root) from the heap
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        # Replace the root with the last element and sink it down to maintain the max-heap property
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

# Testing Constructor, and insert.
            
# myheap = MaxHeap()
# myheap.insert(99)
# myheap.insert(72)
# myheap.insert(61)
# myheap.insert(58)
# print(myheap.heap)
# myheap.insert(100)
# print(myheap.heap)
# myheap.insert(75)
# print(myheap.heap)

# Testing Remove

# myheap = MaxHeap()
# myheap.insert(95)
# myheap.insert(75)
# myheap.insert(80)
# myheap.insert(55)
# myheap.insert(60)
# myheap.insert(50)
# myheap.insert(65)

# print(myheap.heap)

# myheap.remove()

# print(myheap.heap)

# myheap.remove()

# print(myheap.heap)
