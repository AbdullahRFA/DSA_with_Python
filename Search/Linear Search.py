def Linear_Search(arr,n):
    for i in range(len(arr)):
        if n == arr[i]:
            return i
    return -1

    # if element must be present into the arr then it works otherwise it throw an error
    # return arr.index(n)


arr = list(map(int,input("Enter space separated integer: ").split()))
n = int(input("Enter the finding number: "))
res = Linear_Search(arr,n)
if res!=-1:
    print("Found at ",res)
else:
    print("Not found",res)