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


def build_max_heap(arr):
    n = len(arr)
    explore = (n//2 - 1)

    for i in range(explore, -1, -1):
        leftChildIdx = 2*i + 1
        rightChildIdx = 2*i + 2

        largestIdx = i

        if leftChildIdx < n and arr[leftChildIdx] > arr[largestIdx]:
            largestIdx = leftChildIdx

        if rightChildIdx < n and arr[rightChildIdx] > arr[largestIdx]:
            largestIdx = rightChildIdx

        if largestIdx != i:
            arr[i], arr[largestIdx] = arr[largestIdx], arr[i]
            build_max_heap(arr)
    return arr

def build_min_heap(arr):
    n = len(arr)
    explore = (n//2 - 1)

    for i in range(explore, -1, -1):
        leftChildIdx = 2*i + 1
        rightChildIdx = 2*i + 2

        smallestIdx = i

        if leftChildIdx < n and arr[leftChildIdx] < arr[smallestIdx]:
            smallestIdx = leftChildIdx

        if rightChildIdx < n and arr[rightChildIdx] < arr[smallestIdx]:
            smallestIdx = rightChildIdx

        if smallestIdx != i:
            arr[i], arr[smallestIdx] = arr[smallestIdx], arr[i]
            build_min_heap(arr)
    return arr

arr = [4,12,8,9,16,1,19,21]
print("Original Array:", arr)
print("Max Heap:",build_max_heap(arr))
print("Min Heap:",build_min_heap(arr))