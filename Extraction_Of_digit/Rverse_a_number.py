num = int(input("Enter a number to reverse: "))
tem = num
reversed_num = 0
while num != 0:
    r = num % 10
    reversed_num = reversed_num * 10 + r
    num //= 10
print(f"Reverse of {tem} is ",reversed_num)