nums = list(map(int, input("Enter element separate by space : ").split()))
k = int(input("Enter the value of 'K' : "))

def Subset(idx, total):
    if total == k:
        return 1
    elif total > k:
        return 0
    elif idx >= len(nums):
        return 0
    pick = Subset(idx+1,total+nums[idx])
    not_pick = Subset(idx+1, total)

    return pick+not_pick

print(f"Total subset whose sum == K {Subset(0, 0)}")