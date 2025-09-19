class QueueUsingStack:
    def __init__(self):
        self.st1 = []
        self.st2 = []
        
    def push(self, item):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(item)
        while self.st2:
            self.st1.append(self.st2.pop())
    def pop(self):
        if self.st1:
            print(f"Pop : {self.st1.pop()}")
        else:
            print("Queue is empty")
    def peek(self):
        if self.st1:
            print(f"Pop : {self.st1[-1]}")
        else:
            print("Queue is empty")
    def is_empty(self):
        if self.st1:
            print("Queue is empty: False")
        else:
            print("Queue is empty: True")
    def size(self):
        if self.st1:
            print(f"Size : {len(self.st1)}")
        else:
            print("Queue is empty")
    def display(self):
        if self.st1:
            print(f"Current Queue : {self.st1}")
        else:
            print("Queue is empty")
            
queue = QueueUsingStack()
queue.display()
queue.is_empty()
queue.push(1)
queue.display()
queue.push(2)
queue.display()
queue.push(3)
queue.display()
queue.push(4)
queue.display()
queue.push(5)
queue.display()
queue.pop()
queue.pop()
queue.pop()
queue.display()
queue.size()
queue.st1.clear()
queue.display()
