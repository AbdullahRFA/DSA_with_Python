def marge_two_arr(arr1,arr2):
    i,j=0,0
    n,m=len(arr1),len(arr2)
    result = []
    while i<n and j<m:
        if arr1[i]<=arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    if i<n:
        while i<n:
            result.append(arr1[i])
            i+=1
    elif j<m:
        while j<m:
            result.append(arr2[j])
            j+=1
    return result

arr1=[1,3,5,7,9]
arr2 = [2,4,6,8,10,12]
print(marge_two_arr(arr1,arr2))