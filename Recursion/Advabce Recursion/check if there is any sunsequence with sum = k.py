nums = list(map(int, input("Enter element separate by space : ").split()))
k = int(input("Enter the value of 'K' : "))
# result = []


def Solution(idx, total, subset, k):
    if total == k:
        # result.append(subset.copy())
        return True
    elif total > k:
        return False
    elif idx >= len(nums):
        return False

    # include nums[idx]
    subset.append(nums[idx])
    SUM = total + nums[idx]
    # Solution(idx + 1, total + nums[idx], subset, k)
    pick = Solution(idx + 1, SUM, subset, k)
    if pick:
        return True
    # subset.pop()
    e = subset.pop()
    SUM -= e

    # exclude nums[idx]
    # Solution(idx + 1, total, subset, k)
    Not_pick = Solution(idx + 1, SUM, subset, k)
    return Not_pick


subset = []
print(Solution(0, 0, subset, k))
# print(result)
# print(f"Total subsequences equals=={k} is {len(result)}")