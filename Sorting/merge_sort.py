
def merge_array(left,right):
    i,j = 0,0
    n,m = len(left),len(right)
    result = []
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    elif j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result

def merge_sort(arr):
    n = len(arr)
    if n <=1:
        return arr
    mid = n//2
    left_array =arr[:mid]
    right_array = arr[mid:]
    left = merge_sort(left_array)
    right = merge_sort(right_array)
    return merge_array(left,right)

arr = list(map(int,input("Enter the array to be sorted: ").split()))
print("Sortd Array: ",merge_sort(arr))
