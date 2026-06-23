'''
Building a max heap and min heap from a given array can be done using the "heapify" process. The idea is to start from the last non-leaf node and move upwards, ensuring that each subtree satisfies the heap property.

Intuition:
- A max heap is a complete binary tree where the value of each node is greater than or equal to the values of its children. The root node contains the maximum value in the heap.
- A min heap is a complete binary tree where the value of each node is less than or equal to the values of its children. The root node contains the minimum value in the heap.
- To build a max heap or min heap from a given array, we can start from the last non-leaf node and move upwards, applying the heapify process to each node. This ensures that each subtree satisfies the heap property, resulting in a valid max heap or min heap.
- The last non-leaf node in a complete binary tree can be found at index (n//2 - 1), where n is the number of elements in the array. We only need to apply the heapify process to the nodes from this index down to the root (index 0).

Time Complexity:
- The time complexity of building a max heap or min heap from a given array is O(n), where n is the number of elements in the array. This is because we are applying the heapify process to each node, and the number of nodes at each level decreases exponentially as we move up the tree. The total number of operations is proportional to the number of elements in the array.

- The space complexity is O(1) as we are not using any additional data structures that scale with the input size. The heap is built in place within the given array.

- The functions `build_max_heap` and `build_min_heap` take an array as input and return the array transformed into a max heap or min heap, respectively.    
'''



def heapify(arr, n, i):
    largest = i

    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr


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


def build_min_heap(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        min_heapify(arr, n, i)

    return arr


arr = [4,6,8,12,16,13,19,21]
print(build_max_heap(arr))
print(build_min_heap(arr))