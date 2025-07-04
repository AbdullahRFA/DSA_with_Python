def partition(arr,low,high):
    i,j = low+1,high
    pivot = arr[low]
    while i<=j:
        while arr[i]<=pivot and i<=j:
            i+=1
        while arr[j]>pivot and i<=j:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_sort(arr,low,high):
    if low<high:
        p = partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

arr = list(map(int,input("Entert the list to be sorted : ").split()))
quick_sort(arr,0,len(arr)-1)
print("After sorted: ",arr)