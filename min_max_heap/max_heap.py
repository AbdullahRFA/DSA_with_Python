'''
Implementation of a max heap data structure in Python. A max heap is a complete binary tree where the value of each node is greater than or equal to the values of its children. This implementation provides methods for inserting elements, extracting the maximum element, changing the value of an element, and checking the size and emptiness of the heap.

Attributes:
- counter: Keeps track of the number of elements in the heap
- arr: List to store the elements of the heap   

Operations:
- insert(val): Insert a new value into the heap
- extractMax(): Remove and return the maximum value from the heap
- getMax(): Return the maximum value in the heap without removing it
- changeKey(idx, val): Change the value of an element at a given index
- isEmpty(): Check if the heap is empty
- getSize(): Return the number of elements in the heap
Time Complexity:
- insert(val): O(log n)
- extractMax(): O(log n)    
- getMax(): O(1)
- changeKey(idx, val): O(log n)
- isEmpty(): O(1)
- getSize(): O(1)

heapifyUp: This function is used to maintain the heap property after inserting a new element. It compares the newly added element with its parent and swaps them if the new element is greater. This process continues until the heap property is restored.

heapifyDown: This function is used to maintain the heap property after removing the maximum element. It compares the root element with its children and swaps them if the root element is less than either of its children. This process continues until the heap property is restored.



'''


class Implement_maxHeap:
    def __init__(self):
        self.counter = 0
        self.arr = []
    
    def headInitialize(self):
        self.counter = 0
        self.arr.clear()
    
    def heapifyUp(self, arr, idx):
        parentIdx = (idx-1)//2
        if idx>0 and arr[idx]>arr[parentIdx]:
            arr[idx], arr[parentIdx] = arr[parentIdx], arr[idx]
            self.heapifyUp(arr, parentIdx)
    
    def heapifyDown(self, arr, idx):
        
        n = len(arr)
        leftchaildIdx = 2*idx + 1
        rightIdx = 2*idx + 2
        
        largestIdx = idx
        
        if leftchaildIdx<n and arr[leftchaildIdx]>arr[largestIdx]:
            largestIdx = leftchaildIdx
        elif rightIdx<n and arr[rightIdx]>arr[largestIdx]:
            largestIdx = rightIdx
        
        if largestIdx!=idx:
            arr[idx], arr[largestIdx] = arr[largestIdx], arr[idx]
            self.heapifyDown(arr, largestIdx)
    
    def insert(self, val):
        self.arr.append(val)
        self.heapifyUp(self.arr, self.counter)
        self.counter+=1
    
    def display(self):
        print("Heap array:", self.arr)
        
    def changeKey(self, idx, val):
        
        if self.arr[idx]<val:
            self.arr[idx] = val
            self.heapifyUp(self.arr, idx)
        elif self.arr[idx]>val:
            self.arr[idx] = val
            self.heapifyDown(self.arr, idx)
    
    def extractMax(self):
        if self.counter==0:
            return None
        maxVal = self.arr[0]
        self.arr[0] = self.arr[self.counter-1]
        self.arr.pop()
        self.counter-=1
        self.heapifyDown(self.arr, 0)
        return maxVal
    
    def getMax(self):
        if self.counter==0:
            return None
        return self.arr[0]
    def getSize(self):
        return self.counter
    def isEmpty(self):
        return self.counter==0
    
def main():
    heap = Implement_maxHeap()  
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    heap.display()
    print("Maximum value:", heap.getMax())
    print("Extracted maximum value:", heap.extractMax())
    heap.display()
    print("Is the heap empty?", heap.isEmpty())
    print("Size of the heap:", heap.getSize())
main()  