def fun(n):
    if n==1:
        return 1
    return n*fun(n-1)
n = int(input("Enter a number to find factorial: "))
print(fun(n))

