import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = [*map(int,input().split())]
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(1, n+1):
    if visited[i] == 0:
        count += 1
        dfs(i)
        
print(count)