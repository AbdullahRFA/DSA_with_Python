class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

drinks = Node("Drinks")
hot = Node("Hot")
cold = Node("Cold")
drinks.left = hot
drinks.right = cold
tea = Node("Tea")
coffee = Node("Coffee")
hot.left = tea
hot.right = coffee
cola = Node("Cola")
fanta = Node("Fanta")
cold.left = cola
cold.right = fanta  

print(drinks.val)
print(drinks.left.val)
print(drinks.right.val)
print(drinks.left.left.val)
print(drinks.left.right.val)        
print(drinks.right.left.val)
print(drinks.right.right.val)
