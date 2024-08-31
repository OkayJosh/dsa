"""
Implementation of max heap.
In a Max heap the value of the
parent node must be greater
than or equal to the value of its children node
"""


class MaxHeap:
    """
    Implementation of max heap
    """
    def __init__(self):
        self.heap = []

    def _parent_index(self, index):
        """
        This calculates the index of the parent of an element
        (index-1) // 2
        :param index:
        :return:
        """
        return (index - 1) // 2

    def _left_child_index(self, index) -> int:
        """
        Calculates the index of the left child of an element
        2 * index + 1
        :param index:
        :return int:
        """
        return 2 * index + 1

    def _right_child_index(self, index) -> int:
        """
        Calculates the index of the right child of an element
        2 * index + 2
        :param index:
        :return int:
        """
        return 2 * index + 2

    def _heapify_up(self, index):
        """
        Ensures that the max-heap property is maintained
        when a new element is added to the heap
        :param index:
        :return:
        """
        parent_index = self._parent_index(index)
        # at index is 1, parent_index = 0
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            # I would not get there if index is 0
            # [5, 7]
            # at index = 1
            # at parent_index = 0
            # self.heap[1] = 7,
            # self.heap[0] = 5,
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # swapping occurs, index becomes parent_index and parent_index becomes index
            self._heapify_up(parent_index)
            # Recurs

    def _heapify_down(self, index):
        """
        Ensures that the max-heap property is maintained
        when a root element is removed from the heap
        :param index:
        :return:
        """
        # if index is 0
        # left_index = 1
        left_index = self._left_child_index(index)
        # right_index = 2
        right_index = self._right_child_index(index)
        # largest = 0
        largest = index

        # Find the largest among the current node and its children
        if left_index < len(self.heap) and self.heap[left_index] > self.heap[largest]:
            largest = left_index

        if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
            largest = right_index

        # If the largest is not the current node, swap and continue heapifying down
        if largest != index:
            # if largest != index then swap
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            # then recurse
            self._heapify_down(largest)

    def insert(self, element) -> None:
        """
        Insert an element into the max heap
        :param element:
        :return None:
        """
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self) -> int or None:
        """
        This extracts the max element from the heap
        in other words this pops the max element from the heap
        :return int:
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # self.heap = [7, 5]
        # max_element = 7
        max_element = self.heap[0]
        # pop is removing the last elements not the first element at index 0
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_element

    def get_max(self) -> int:
        """
        This returns the maximum element in the heap
        without popping it,
        in other word the root of the heap
        :return int:
        """
        return self.heap[0] if self.heap else None

    def size(self) -> int:
        """
        This method returns the size of the heap
        :return int:
        """
        return len(self.heap)

    def is_empty(self) -> bool:
        """
        This check of the heap is empty
        :return bool:
        """
        return len(self.heap) == 0


# Example usage:
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(15)
max_heap.insert(15)
max_heap.insert(15)
max_heap.insert(30)
max_heap.insert(40)
max_heap.insert(40)

print("Max Element:", max_heap.extract_max())  # Output: 40
print("Max Element:", max_heap.extract_max())  # Output: 30

"""
Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Solve with heap without without sorting?

Given an Integer Array Numbers
Fist largest ELement, 2nd largest Element, .... K th largest Element
What happens as K approaches N
"""

import heapq


def find_kth_largest(nums, k):
    # Convert the nums array into a max-heap by inverting the values
    max_heap = [-num for num in nums]
    # we convert to negative because: when we do the largest element becomes the lowest value
    # and the lowest value becomes the root of the heap

    # Convert the list into a heap
    heapq.heapify(max_heap)

    # Extract the maximum element K times
    kth_largest = None
    for _ in range(k):
        # we multiply by negative to get back the original value
        # we pop the lowest value and by negating it we get the largest value
        kth_largest = -heapq.heappop(max_heap)

    return kth_largest


# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
result = find_kth_largest(nums, k)
print(f"The {k}th largest element is {result}")
