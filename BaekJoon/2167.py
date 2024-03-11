n, m = [*map(int,input().split())]
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
ans = []

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = arr[i][j] + dp[i+1][j] + dp[i][j+1] - dp[i][j]

for _ in range(k):
    i, j, x, y = map(int, input().split())
    ans.append(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

for i in ans:
    print(i)