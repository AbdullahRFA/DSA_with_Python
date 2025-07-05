arr = list(map(int,input().split()))
# arr.sort()
# print(arr[-2]) #TC O(n log n)

# Bellow code TC O(N)

n = len(arr)

# fl = arr[0]
# for i in range(1,n):
#     fl =max(arr[i],fl)
# print(fl)
#
# sl = float("-inf")
# for i in range(n):
#     if sl < arr[i] < fl:
#         sl = arr[i]
# print(sl)

# Optimal Solution TC O(N)
fl=sl=float("-inf")
for i in range(n):
    if arr[i]>fl:
        sl=fl
        fl=arr[i]
    elif sl<arr[i]<fl:
        sl=arr[i]
print(fl,sl)

"""
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    sl=fl=float("-inf")
    sm=fm=float("inf")

    for i in range(n):
        if a[i]>fl:
            sl=fl
            fl=a[i]
        if sl<a[i]<fl:
            sl=a[i]
        if a[i]<fm:
            sm=fm
            fm=a[i]
        if fm<a[i]<sm:
            sm=a[i]
    return [sl,sm]
"""