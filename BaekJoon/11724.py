n, m = [*map(int,input().split())]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

visited = [0] * (n+1)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

count = 0
for i in range(1, n+1):
    if visited[i] == 0:
        count += 1
        dfs(i)
        
print(count)