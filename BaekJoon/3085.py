a = int(input())
candy_list = [list(input()) for _ in range(a)]

def function_candy(candy_list):
    max_cnt = 1

    for row in candy_list:
        cnt = 1
        for j in range(1, len(row)):
            if row[j] == row[j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)

    for i in range(len(candy_list[0])):
        cnt = 1
        for j in range(1, len(candy_list)):
            if candy_list[j][i] == candy_list[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)

    return max_cnt

def function_max(a, candy_list):
    result = 1

    for i in range(a):
        for j in range(a-1):
            if j+1 < a and candy_list[i][j] != candy_list[i][j+1]:
                candy_list[i][j], candy_list[i][j+1] = candy_list[i][j+1], candy_list[i][j]
                result = max(result, function_candy(candy_list))
                candy_list[i][j], candy_list[i][j+1] = candy_list[i][j+1], candy_list[i][j]

            if i+1 < a and candy_list[i][j] != candy_list[i+1][j]:
                candy_list[i][j], candy_list[i+1][j] = candy_list[i+1][j], candy_list[i][j]
                result = max(result, function_candy(candy_list))
                candy_list[i][j], candy_list[i+1][j] = candy_list[i+1][j], candy_list[i][j]

    return result

print(function_max(a, candy_list))