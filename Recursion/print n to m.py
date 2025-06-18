def fun(n,m):
    if n>m:
        return
    fun(n + 1, m)
    print(n)

n = int(input("Enter the starting point: "))
m = int(input("Enter the ending point: "))
fun(n,m)