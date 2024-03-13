n, m = [*map(int,input().split())]
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
sum_arr = [list(map(int, input().split())) for _ in range(k)]

for l in sum_arr:
    i, j, x, y = l
    answer = 0
    for m in range(i-1, x):
        for n in range(j-1, y):
            answer += arr[m][n]
    print(answer)

'''n, m = [*map(int,input().split())]
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
sum_arr = [list(map(int, input().split())) for _ in range(k)]
result = [[0]*(m+1) for _ in range(n+1)]
ans = []

for i in range(n):
    for j in range(m):
        result[i+1][j+1] = arr[i][j] + result[i+1][j] + result[i][j+1] - result[i][j]

for l in sum_arr:
    i, j, x, y = l
    ans.append(result[x][y] - result[x][j-1] - result[i-1][y] + result[i-1][j-1])


for i in ans:
    print(i)'''