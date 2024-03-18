import sys
sys.setrecursionlimit(10**7) # 이거 안하면 런타임오류

n, m = [*map(int,sys.stdin.readline().split())]
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

for j in range(1, n+1):
    if visited[j] == 0:
        count += 1
        dfs(j)
        
print(count)