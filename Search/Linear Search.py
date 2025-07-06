def Linear_Search(arr,n):
    res = -1
    for i in range(len(arr)):
        if n == arr[i]:
            res = i
            break
    return res


arr = list(map(int,input("Enter space separated integer: ").split()))
n = int(input("Enter the finding number: "))
res = Linear_Search(arr,n)
if res!=-1:
    print("Found at ",res)
else:
    print("Not found",res)