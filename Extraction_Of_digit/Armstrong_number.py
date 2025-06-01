"""
"""
def count_of_digit(n):
    num = n
    cnt = 0
    while num != 0:
        num //= 10
        cnt += 1
    return cnt
def check_armstrong(n,cnt):
    num = n
    armstrong_number = 0
    while num != 0:
        r = num % 10
        armstrong_number += r**cnt
        num //= 10
    return n == armstrong_number


n = int(input("Enter a number to check if it is armstrong number or not: "))
cnt = count_of_digit(n)
if check_armstrong(n,cnt):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")

