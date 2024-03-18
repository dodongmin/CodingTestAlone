from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    
    while queue:
        cx, cy, dist = queue.popleft()
        if graph[cx][cy] == 1:
            return dist
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny, dist + 1))

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result = max(result, bfs(i, j))

print(result)

# 2번째 방법
'''import math

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

print(int(result))'''