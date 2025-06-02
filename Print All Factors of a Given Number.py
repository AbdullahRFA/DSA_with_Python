n = int(input("Enter a number to find it's all factor: "))
factor = []

# brut force

# for i in range(1,n+1):
#     if n%i==0:
#         factor.append(i)

# better than brut force
# for i in range(1,int(n//2)+1):
#     if n%i==0:
#         factor.append(i)
# factor.append(n)

# most efficient
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        factor.append(i)
        if n//i != i:
            factor.append(n//i)
        # factor.append(n//i)
# factor=list(set(factor))
factor.sort()
print(f"Factors of {n} are : ",factor)