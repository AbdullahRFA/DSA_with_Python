'''
Check if an array follows the min heap property.

Intuition:
- A min heap is a complete binary tree where the value of each node is less than or equal to the values of its children. The root node contains the minimum value in the heap.
- To check if an array follows the min heap property, we can iterate through the array and for each node, check if its value is less than or equal to the values of its children. If we find any node that violates this property, we can conclude that the array does not follow the min heap property.
- The last non-leaf node in a complete binary tree can be found at index (n//2 - 1), where n is the number of elements in the array. We only need to check the nodes from this index down to the root (index 0) because all leaf nodes automatically satisfy the min heap property.

Time Complexity:
- The time complexity of this approach is O(n), where n is the number of elements in the array. This is because we are iterating through the array once and performing constant time checks for each node.
- The space complexity is O(1) as we are not using any additional data structures that scale with the input size.
- The function `check_if_min_heap` takes an array as input and returns True if the array follows the min heap property, and False otherwise.


Space Complexity:   
- The space complexity is O(1) as we are not using any additional data structures that scale with the input size.
'''


def check_if_min_heap(arr):
    n = len(arr)
    explore = (n//2 - 1)

    for i in range(explore, -1, -1):
        leftChildIdx = 2*i + 1
        rightChildIdx = 2*i + 2
        
        if  leftChildIdx < n and  arr[leftChildIdx] < arr[i]:
            return False
        if  rightChildIdx < n and  arr[rightChildIdx] < arr[i]:
            return False
    return True




arr = [4,6,8,12,16,13,19,21]
print(check_if_min_heap(arr))