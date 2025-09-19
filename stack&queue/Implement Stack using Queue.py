from collections import  deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()
    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    def pop(self):
        if len(self.queue) == 0:
            print("Stack is empty")
        else:
            print(self.queue.popleft())
    def peek(self):
        if len(self.queue) == 0:
            print("Stack is empty")
        else:
            print(self.queue[0])
    def is_empty(self):
        if len(self.queue)==0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
    def size(self):
        print(f"Size of the stack is {len(self.queue)}")
    def display(self):
        if len(self.queue) == 0:
            print("Stack is empty")
        else:
            print("Stack elements are:",list(self.queue))

st = StackUsingQueue()

st.display()
st.push(10)
st.display()
st.push(20)
st.display()
st.push(22)
st.display()
st.push(23)
st.display()
st.push(24)
st.display()
st.push(25)
st.display()
st.push(26)
st.display()
st.pop()
st.display()
st.peek()
st.is_empty()
st.size()
    # 14. Clear the deque
st.queue.clear()
st.display()
