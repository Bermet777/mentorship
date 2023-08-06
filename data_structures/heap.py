class MaxHeap:
    def __init__(self):
        self.heap_list = []

    def insert(self, value):
        self.heap_list.append(value)
        self._heapify_up(len(self.heap_list) - 1)

    def _heapify_up(self, i):
        parent_idx = (i - 1) // 2
        while i > 0 and self.heap_list[i] > self.heap_list[parent_idx]:
            self.heap_list[i], self.heap_list[parent_idx] = self.heap_list[parent_idx], self.heap_list[i]
            i = parent_idx
            parent_idx = (i - 1) // 2

    def remove_max(self):
        if not self.heap_list:
            raise IndexError("Heap is empty.")
        self.heap_list[0], self.heap_list[-1] = self.heap_list[-1], self.heap_list[0]
        max_value = self.heap_list.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_down(self, i):
        while True:
            left_child_idx = 2 * i + 1
            right_child_idx = 2 * i + 2
            largest_idx = i

            if left_child_idx < len(self.heap_list) and self.heap_list[left_child_idx] > self.heap_list[largest_idx]:
                largest_idx = left_child_idx

            if right_child_idx < len(self.heap_list) and self.heap_list[right_child_idx] > self.heap_list[largest_idx]:
                largest_idx = right_child_idx

            if largest_idx == i:
                break

            self.heap_list[i], self.heap_list[largest_idx] = self.heap_list[largest_idx], self.heap_list[i]
            i = largest_idx

    def peek_max(self):
        if not self.heap_list:
            raise IndexError("Heap is empty.")
        return self.heap_list[0]

    def is_empty(self):
        return len(self.heap_list) == 0


if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(5)
    heap.insert(10)
    heap.insert(7)
    heap.insert(3)

    print(heap.peek_max())  

    print(heap.remove_max())  
    print(heap.peek_max())  
