class node:
    def __init__(self,val):
        self.val = val
        self.next = None

node1= node(5)
node2= node(4)
node3= node(7)
node4= node(90)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1.val)
print(node1.next)
print(node1.next.val)
print(node2)
print(node1.next.next.next.val)
print(node4.val)
