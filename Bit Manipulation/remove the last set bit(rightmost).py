"""
    16 = 1000
  & 15 = 0111
  -------------
        0000
    40 = 101000
  & 39 = 100111
  -------------
        100000
"""

num = int(input("Enter a number to remove it's last set bit : "))
temp = num - 1

print(f"Before removing the first set bit of {num}({bin(num)[2:]})")
num = num & temp
print(f"After removing the first set bit of {num}({bin(num)[2:]})")

