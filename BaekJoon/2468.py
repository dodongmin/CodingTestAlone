import math

n, m = [*map(int,input().split())]
graph = [list(map(int, input().split())) for _ in range(n)]
graph2 = []
result = float('inf')

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            graph2.append([i,j])

for k in graph2:
    for l in graph2:
        if k != l:
            result = min(math.sqrt((k[0] - l[0])**2 + (k[1] - l[1])**2), result)

print(int(result))