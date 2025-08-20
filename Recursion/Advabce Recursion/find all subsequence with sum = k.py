nums = list(map(int, input("Enter element separate by space : ").split()))
k = int(input("Enter the value of 'K' : "))
result = []


def Solution(idx, total, subset, k):
    if total == k:
        result.append(subset.copy())
        return
    elif total > k:
        return
    elif idx >= len(nums):
        return

    # include nums[idx]
    subset.append(nums[idx])
    SUM = total + nums[idx]
    # Solution(idx + 1, total + nums[idx], subset, k)
    Solution(idx + 1, SUM, subset, k)
    # subset.pop()
    e = subset.pop()
    SUM -= e

    # exclude nums[idx]
    # Solution(idx + 1, total, subset, k)
    Solution(idx + 1, SUM, subset, k)


subset = []
Solution(0, 0, subset, k)
print(result)
print(len(result))