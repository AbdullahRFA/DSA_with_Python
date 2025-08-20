nums =list(map(int,input("Enter element separate by space : ").split()))
result = []

def Solution(idx, subset):
    if idx >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[idx])
    Solution(idx+1, subset)
    subset.pop()
    Solution(idx+1, subset)


subset = []
Solution(0, subset)
print(result)
print(len(result))