import time

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.comparisons = 0
        self.swaps = 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.swaps += 1  # Counting each swap


    def insert(self, element):
        """
        Insert a new element to the heap.
        """
        self.heap.append(element)
        current = len(self.heap) - 1

        # Up-heap bubbling
        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.comparisons += 1  # Counting comparison
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def heapify(self, index):
        """
        Ensure the heap property is maintained starting from the given index.
        """
        left = self.left_child(index)
        right = self.right_child(index)
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
            self.comparisons += 1  # Counting comparison
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
            self.comparisons += 1  # Counting comparison
        
        if largest != index:
            self.swap(index, largest)
            self.heapify(largest)

    def remove_max(self):
        """
        Remove and return the maximum element from the heap.
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to root
        self.heapify(0)
        return root

    def max(self):
        """
        Get the maximum element from the heap without removing it.
        """
        return self.heap[0] if self.heap else None


def heap(arr):

    heap = MaxHeap()
    for num in arr:
        heap.insert(num)

    # Perform ⌊n/2⌋ removals
    for _ in range(len(arr) // 2):
        heap.remove_max()

    return heap.max(), heap.comparisons, heap.swaps

# Example call (commented out):
# find_max_after_removals([12, 11, 13, 5, 6, 20, 15])


with open("r15000.txt", "r") as file:
    data = file.readlines()
    for line in data:
        input = line.split()
    input = [int(i) for i in input]
    t_start = time.time()

    max, comparisons, swaps  = heap(input)

    t_end = time.time()

    print("\n\nFor ",file.name )
    print("------------------------")
    print("Max is: ", max)
    print("------------------------")
    print(f"Execution Time in (s): {t_end-t_start}")
    print("------------------------")
    print("Number of operations:", swaps + comparisons)
    print("------------------------\n")



