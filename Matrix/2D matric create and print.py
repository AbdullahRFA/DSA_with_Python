n=int(input("Number of rows: "))
m=int(input("Number of clos: "))
lst = []

for i in range(n):
    row = []
    for j in range(m):
        val = int(input())
        row.append(val)
    lst.append(row)
print(lst)

for i in range(n):
    for j in range(m):
        print(lst[i][j],end=" ")
    print()