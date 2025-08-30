class Stack:
    def __init__(self):
        self.item = []
    def is_empty(self):
        if len(self.item) == 0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
    def push(self,data):
        self.item.append(data)
        print(f"After appending {data} the current stack is {self.item}")
    def pop(self):
        if len(self.item) == 0:
            print("Stack is empty, can't pop right now")
            return
        self.item.pop()
        print("After popping the current stack is ",self.item)
    def top(self):
        if len(self.item) == 0:
            print("Stack is empty, there is no top element right now")
            return
        print("The top element of the is : ",self.item[-1])
    def size(self):
        print("Lenght of the stack is : ",len(self.item))
    
    
    
stack = Stack()
stack.is_empty()
stack.push(10)
stack.push(12)
stack.push(15)
stack.pop()
stack.top()
stack.size()
stack.pop()
stack.pop()
stack.pop()


        
        