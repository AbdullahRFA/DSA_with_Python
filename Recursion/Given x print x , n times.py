def fun(name,n):
    if n == 0:
        return
    print(name)
    fun(name,n-1)

fun("Abdullah",3)