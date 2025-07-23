from pandas import lreshape


def lowerBond(nums,targert):
    left = 0
    right = len(nums)-1
    lb = len(nums)
    while left<=right:
        mid = (left+right)//2
        if nums[mid]>=target:
            lb = mid
            right = mid - 1
        else:
            left = mid+1
    return lb

def upperBound(nums,target):
    left = 0;
    right = len(nums)-1
    ub = len(nums)
    while left <= right:
        mid = (left+right)//2
        if nums[mid] > target:
            ub = mid
            right = mid-1
        else:
            left = mid+1
    return ub



# nums = [1,2,3,4,5,6,7,8,9]
nums = [1, 3, 3, 5, 6, 8, 10]
target = int(input("Enter a number to be searched: "))
print(lowerBond(nums,target))
print(upperBound(nums,target))
