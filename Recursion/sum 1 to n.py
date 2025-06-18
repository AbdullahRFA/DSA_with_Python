# Sum = 0
# pramatized recursion
# def fun(i,n,Sum):
#     if i>n:
#         print(Sum)
#         return
#     # Sum+=i
#     # print(i+1,n,Sum)
#     fun(i+1,n,Sum+i)
# n = int(input("Enter the ending point: "))
# fun(1,n,0)

# functional recursion
# return something
def fun(n):
    if n == 1:
        return 1
    return n + fun(n-1)
n = int(input())
print(fun(n))