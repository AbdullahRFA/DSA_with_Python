n = int(input("Enter a number to find it's all factor: "))
factor = []

# brut force

# for i in range(1,n+1):
#     if n%i==0:
#         factor.append(i)
# O(N)
# ST(K)

# better than brut force
# for i in range(1,int(n//2)+1):
#     if n%i==0:
#         factor.append(i)
# factor.append(n)
# O(N/2) ===O(N)
# ST(K)

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
# O(sqrt(N))+ O(NlogN)
# ST(K)