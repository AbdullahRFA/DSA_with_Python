

def binary_search(nums,target):
    n = len(nums)
    left = 0
    right = n-1
    return RecursiveBS(nums,target,left,right)
    # while left <= right:
    #     mid = (left+right)//2
    #     if nums[mid] == target:
    #         return  mid
    #     elif nums[mid] < target:
    #         left = mid+1
    #     else:
    #         right = mid-1
    # return -1

def RecursiveBS(nums,target,left,right):
    print("RC")
    if left > right:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return RecursiveBS(nums,target,mid+1,right)
    else:
        return RecursiveBS(nums,target,left,mid-1)


nums = [1,2,3,4,5,6,7,8,9]
target = int(input("Enter a number to be searched: "))
print(binary_search(nums,target))
