def fun(n,m):
    if n>m:
        return
    print(n)
    fun(n+1,m)
n = int(input("Enter the starting point: "))
m = int(input("Enter the ending point: "))
fun(n,m)