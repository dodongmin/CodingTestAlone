n, w, l = map(int, input().split())
truck = list(map(int, input().split()))
time = 0

for i in range(1,n):
    if sum(truck) == l:
        time = n + w
    elif len(truck) == 1:
        time = n + w
    else:
        if sum(truck[:i-1]) <= l and sum(truck[:i]) > l:
            time += w + len(truck[:i-1])
            
            del truck[:i-1]
            print(time)
            print(truck)
            print(len(truck))
        if len(truck) == 1:
            time += 1

print(time)
#