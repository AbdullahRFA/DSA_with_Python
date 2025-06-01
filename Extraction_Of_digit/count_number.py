num = int(input("Enter a number to count it number of digit: "))
cnt = 0
tem = num
while num != 0:
    num //= 10
    cnt +=1
print(f"Number of digit in {tem} is ",cnt)