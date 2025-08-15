while True:
    num1 = int(input())
    num2 = int(input())

    if num1 == 0:
        break
    print(f"{num1} & {num2} = ",num1 & num2)
    print(f"{num1} | {num2} = ",num1 | num2)
    print(f"{num1} ^(XOR) {num2} = ",num1 ^ num2)
    print(f"{num1} >> 1 : ", num1>>1)
    print(f"{num2} << 1 : ", num2<<1)
    print(f"not(!) {num2} : ", ~num2)
    print("-------------------------")