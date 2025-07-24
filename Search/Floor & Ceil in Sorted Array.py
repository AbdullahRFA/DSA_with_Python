class Solution:
    def seil_floor(self,nums,target):
        left = 0
        right = len(nums)-1
        ceil = -1
        floor = -1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return [nums[mid], nums[mid]]
            elif nums[mid]>target:
                ceil = nums[mid]
                right = mid - 1
            else:
                floor = nums[mid]
                left = mid +1
        return [floor,ceil]

slv = Solution()
nums =list(map(int,input("Enter nums elements space-separated: ").split()))
target = int(input("Enter target value: "))
print(slv.seil_floor(nums,target))