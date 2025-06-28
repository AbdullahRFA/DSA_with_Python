def insertionSortAsc(arr):
    n = len(arr)
    for i in range(1,n):
        j = i-1
        key = arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
def insertionSortDes(arr):
    n = len(arr)
    for i in range(1,n):
        j = i-1
        key = arr[i]
        while j>=0 and arr[j]<key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
arr = list(map(int,input().split()))
asc = arr.copy()
print("Before sorting : ",arr)
print("After sorting in ascending order : ",insertionSortAsc(asc))
desc = arr.copy()
print("After sorting in descending order : ",insertionSortDes(desc))