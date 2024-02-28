cnt, k = [*map(int,input().split())]
coin_list = [int(input()) for _ in range(cnt)]
coin_list = sorted(coin_list, reverse=True)

def function(k, coin_list):
    answer = 0
    for i in coin_list:
        if i <=k:
            answer += k//i
            k = k - i * (k//i)

    return answer

print(function(k, coin_list))

#44ms