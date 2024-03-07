n, w, l = map(int, input().split())
truck = list(map(int, input().split()))

time = 0
result = [0] * w 

while result:
    time += 1
    result.pop(0)

    if truck:
        if sum(result) + truck[0] <=l:
            result.append(truck.pop(0))
            
        else:
            result.append(0)
        
print(time)

#반례 존재
'''if sum(truck) == l:
    time += n + w
elif len(truck) == 1:
    time += n + w
else:
     
    for i in range(1,n):
        if sum(truck) == l:
            time += n + w
        elif len(truck) == 1:
            time += n + w
        else:
            if sum(truck[:i-1]) <= l and sum(truck[:i]) > l:
                time += w + len(truck[:i-1])
                
                del truck[:i-1]
            if len(truck) == 1:
                time += 1

print(time)'''