# for j in range(10,0,-1):
#     print(j)
t = int(input())
for _ in range(t):
    n = int(input())
    num = input()
    left,right = 0, n-1

    while left<n:
        if num[left] == "B":
            break
        left+=1

    while right>=0:
        if num[right] == "B":
            break
        right-=1
    print(right-left+1)
