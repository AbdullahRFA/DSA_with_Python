class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        if len(self.items) == 0:
            print("Queue is empty")
        else:
            print("Queue is not empty")
    def enqueue(self, data):
        self.items.append(data)
        print(f"After appending {data} the current queue is ",self.items)
    def size(self):
        print("The length of the queue is ",len(self.items))
    def dequeue(self):
        if len(self.items) :
            self.items.pop(0)
            print("After dequeuing the current queue is ",self.items)
        else:
            print("queue is empty, dequeue is not possible right now")
    def front(self):
        if len(self.items):
            print(f"Front element of the queue is {self.items[0]}")
        else:
            print("Queue is empty, there is no element")
    def rear(self):
        if len(self.items):
            print(f"Rear element of the queue is {self.items[-1]}")
        else:
            print("Queue is empty, there is no element")


queue = Queue()
queue.is_empty()
queue.enqueue(12)
queue.enqueue(23)
queue.enqueue(45)
queue.enqueue(56)
queue.size()
queue.rear()
queue.front()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.size()
queue.dequeue()
queue.rear()
queue.front()
    