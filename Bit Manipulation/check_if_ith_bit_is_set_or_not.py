num = int(input("Enter a number to check if it's ith bit is set or not : "))
ith = int(input("Enter the value of 'i' : "))

# tem = 1<<ith
#
# result = num & tem
#
# if result:
#     print(f"{ith}th bit of {num}({bin(num)[2:]} is set")
# else:
#     print(f"{ith}th bit of {num}({bin(num)[2:]} is not set")

# if num & (1<<ith) :
#     print(f"{ith}th bit of {num}({bin(num)[2:]}) is set")
# else:
#     print(f"{ith}th bit of {num}({bin(num)[2:]}) is not set")

#   Using right shift

if (num>>ith)&1 :
    print(f"{ith}th bit of {num}({bin(num)[2:]}) is set")
else:
    print(f"{ith}th bit of {num}({bin(num)[2:]}) is not set")

