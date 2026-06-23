n = 5

ages = [[2, 3], [2, 4], [3, 4], [3, 5], [4, 5]]

# Matrix representation of graph
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
print("Matrix representation:", matrix)

for u,v in ages:
    matrix[u][v] = 1
    matrix[v][u] = 1
print("Matrix representation:", matrix)

# list representation of graph
lst = [[] for _ in range(n+1)]
print("List representation:", lst)
for u,v in ages:
    lst[u].append(v)
    lst[v].append(u)
print("List representation:", lst)

# dictionary representation of graph
dct = {i: [] for i in range(n+1)}
print("Dictionary representation:", dct)
for u,v in ages:
    dct[u].append(v)
    dct[v].append(u)
print("Dictionary representation:", dct)