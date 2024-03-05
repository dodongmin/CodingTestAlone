from collections import Counter

a = list(input())

def function(a):
    cnt = 0
    answer = ""
    values = sorted(Counter(a).values())
    keys = sorted(Counter(a).keys())
    cnta = Counter(a)

    for i in values:
        if i % 2 != 0:
            cnt += 1

    if cnt >=2:
        answer = "I'm Sorry Hansoo"

    elif cnt ==1:
        for key in keys:
            answer += key*(cnta[key]//2)
            if cnta[key] % 2 != 0:
                center = key
        answer = answer + center + answer[::-1]

    else:
        for key in keys:
            answer += key*(cnta[key]//2)
        answer = answer + answer[::-1]

    return answer

print(function(a))