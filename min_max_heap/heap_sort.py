'''
Heap Sort Implementation using Min Heap and Max Heap
The heap sort algorithm is a comparison-based sorting technique that uses a binary heap data structure. It can be implemented using either a min heap or a max heap. The algorithm works by first building a heap from the input data, and then repeatedly extracting the minimum (or maximum) element from the heap and placing it into the sorted array. The process continues until all elements have been extracted from the heap and placed into the sorted array.

The implementation below provides functions to build a max heap and a min heap from a given array, and then uses these heaps to sort the array in ascending and descending order, respectively. The time complexity of heap sort is O(n log n), where n is the number of elements in the array.

Time Complexity:
- The time complexity of building a max heap or min heap from a given array is O(n), where n is the number of elements in the array. This is because we are applying the heapify process to each node, and the number of nodes at each level decreases exponentially as we move up the tree. The total number of operations is proportional to the number of elements in the array.

- The space complexity is O(1) as we are not using any additional data structures that scale with the input size. The heap is built in place within the given array.
- The functions `build_max_heap` and `build_min_heap` take an array as input and return the array transformed into a max heap or min heap, respectively. 


Intuition:  
- A max heap is a complete binary tree where the value of each node is greater than or equal to the values of its children. The root node contains the maximum value in the heap. To build a max heap from an array, we can start from the last non-leaf node and apply the heapify process to each node in reverse level order until we reach the root node.
- A min heap is a complete binary tree where the value of each node is less than or equal to the values of its children. The root node contains the minimum value in the heap. To build a min heap from an array, we can follow the same process as building a max heap, but we will apply the heapify process in a way that ensures the min heap property is maintained.
- The last non-leaf node in a complete binary tree can be found at index (n//2 - 1), where n is the number of elements in the array. We only need   
'''


import random
def max_heapify(arr, n, i):
    largest = i
    
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def min_heapify(arr, n, i):
    smallest = i
    
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

def build_max_heap(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i)

    return arr  


def build_min_heap(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        min_heapify(arr, n, i)

    return arr

arr = random.sample(range(1, 100), 10)
print("Original array:", arr)
# O(n) time complexity
max_heap = build_max_heap(arr)
print("Max heap:", max_heap)

# Heap sort in ascending order
# O(n log n) time complexity
for last in range(len(arr)-1, 0, -1): # O(N)
    arr[0], arr[last] = arr[last], arr[0]
    max_heapify(arr, last, 0) # O(log N)
print("Sorted array Ascending:", arr)

min_heap = build_min_heap(arr)
print("Min heap:", min_heap)
# Heap sort in descending order
# O(n log n) time complexity
for last in range(len(arr)-1, 0, -1): # O(N)
    arr[0], arr[last] = arr[last], arr[0]
    min_heapify(arr, last, 0) # O(log N)
print("Sorted array Descending:", arr)