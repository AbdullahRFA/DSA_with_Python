def fun(arr,left,right):
    if left>=right:
        return
    arr[left-1],arr[right-1] = arr[right-1],arr[left-1]
    fun(arr,left+1,right-1)

arr = [1,2,3,4,5,6]
left = 2
right = 4
fun(arr,left,right)
print(arr)