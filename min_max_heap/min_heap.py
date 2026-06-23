'''
Min Heap Implementation in Python

Min Heap is a complete binary tree where the value of each node is less than or equal to the values of its children. The root node contains the minimum value in the heap.

heapifyUp: This function is used to maintain the heap property after inserting a new element. It compares the newly added element with its parent and swaps them if the new element is smaller. This process continues until the heap property is restored.

heapifyDown: This function is used to maintain the heap property after removing the minimum element. It compares the root element with its children and swaps them if the root element is greater than either of its children. This process continues until the heap property is restored.

Attributes:
- counter: Keeps track of the number of elements in the heap
- arr: List to store the elements of the heap


Operations:
- insert(val): Insert a new value into the heap
- extractMin(): Remove and return the minimum value from the heap
- getMin(): Return the minimum value in the heap without removing it
- changeKey(idx, val): Change the value of an element at a given index
- isEmpty(): Check if the heap is empty
- size(): Return the number of elements in the heap
- display(): Print the heap array

Time Complexity:
- insert(val): O(log n)
- extractMin(): O(log n)
- getMin(): O(1)
- changeKey(idx, val): O(log n)
- isEmpty(): O(1)
- size(): O(1)
- display(): O(n)
'''


class Implement_heap:
    def __init__(self):
        self.counter = 0
        self.arr = []
    
    def headInitialize(self, ):
        self.counter = 0
        self.arr.clear()
    
    def heapifyUp(self, arr, idx):
        parentIdx = (idx-1)//2
        if idx>0 and arr[idx]<arr[parentIdx]:
            arr[idx], arr[parentIdx] = arr[parentIdx], arr[idx]
            self.heapifyUp(arr, parentIdx)
    
    def heapifyDown(self, arr, idx):
        
        n = len(arr)
        leftchaildIdx = 2*idx + 1
        rightIdx = 2*idx + 2
        
        smallestIdx = idx
        
        if leftchaildIdx<n and arr[leftchaildIdx]<arr[smallestIdx]:
            smallestIdx = leftchaildIdx
        elif rightIdx<n and arr[rightIdx]<arr[smallestIdx]:
            smallestIdx = rightIdx
        
        if smallestIdx!=idx:
            arr[idx], arr[smallestIdx] = arr[smallestIdx], arr[idx]
            self.heapifyDown(arr, smallestIdx)
    
    def insert(self, val):
        self.arr.append(val)
        self.heapifyUp(self.arr, self.counter)
        self.counter+=1
    
    def display(self):
        print("Heap array:", self.arr)
        
    def changeKey(self, idx, val):
        
        if self.arr[idx]>val:
            self.arr[idx] = val
            self.heapifyUp(self.arr, idx)
        elif self.arr[idx]<val:
            self.arr[idx] = val
            self.heapifyDown(self.arr, idx)
    
    def extractMin(self):
        if self.counter==0:
            return None
        minVal = self.arr[0]
        self.arr[0] = self.arr[self.counter-1]
        self.arr.pop()
        self.counter-=1
        self.heapifyDown(self.arr, 0)
        return minVal
    
    def getMin(self):
        if self.counter==0:
            return None
        return self.arr[0]
    
    def isEmpty(self):
        return self.counter==0
    
    def size(self):
        return self.counter
    


def main():
    heap = Implement_heap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    heap.display()
    print("Minimum value:", heap.getMin())
    print("Extracted minimum value:", heap.extractMin())
    heap.display()
    print("Is the heap empty?", heap.isEmpty())
    print("Size of the heap:", heap.size())
main()
