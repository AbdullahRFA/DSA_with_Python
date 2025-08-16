"""
2 = 10
4 = 100
8 = 1000
16 = 10000
32 = 100000

so if we remove the first set bit then all number
that can represent as power  of 2 will be zero


"""

num = int(input("Enter a number to check either it's power of 2 or not : "))

if not num&(num-1):
    print(f"{num} is represented as power of 2")
else:
    print(f"{num} is not represented as power of 2")