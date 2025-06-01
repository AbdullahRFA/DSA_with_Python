num = int(input("Enter a number to check palindrom: "))
tem = num
reversed_num = 0
while num != 0:
    r = num % 10
    reversed_num = reversed_num * 10 + r
    num //= 10
if tem == reversed_num:
    print(f"{tem} is a palindrom number")
else:
    print(f"{tem} is not a palindrom number")