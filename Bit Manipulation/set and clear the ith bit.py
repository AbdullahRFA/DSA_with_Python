num = int(input("Enter the number to set ith bit : "))
ith = int(input("Enter the value of 'ith' : "))
print(f"Before setting {ith}th bit of {num}({bin(num)[2:]})")
if num&(1<<ith):
    print(f"{ith}th bit of {num} is already set")
else:
    # num+=1<<ith
    num= num | (1<<ith)
    print(f"After setting {ith}it bit {num}({bin(num)[2:]})")
print()

num = int(input("Enter the number to clear ith bit : "))
ith = int(input("Enter the value of 'ith' : "))
print(f"Before clearing {ith}th bit of {num}({bin(num)[2:]})")
if not (num&(1<<ith)):
    print(f"{ith}th bit of {num} is already clear")
else:
    # tem = 1<<ith
    # tem = ~tem
    # num = num & tem
    num= num ^ (1<<ith)
    print(f"After clearing {ith}it bit {num}({bin(num)[2:]})")