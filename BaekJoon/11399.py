cnt = int(input())
line = [*map(int,input().split())]

def function(cnt, line):
    answer = 0
    line = sorted(line)

    for i in line:
        answer += i * cnt
        cnt -= 1
    
    return answer

print(function(cnt, line))

#44ms