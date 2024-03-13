from collections import deque

t = int(input())
testcases = [input() for _ in range(t)]
direction =deque([[-1,0],[0,1],[1,0],[0,-1]])

for testcase in testcases:
    max_x,max_y,min_x,min_y=0,0,0,0
    x,y=0,0
    for i in testcase:
        if i=='F':
            x=x+direction[0][0]
            y=y+direction[0][1]
        elif i=='B':
            x=x-direction[0][0]
            y=y-direction[0][1]
        elif i=='L':
            direction.rotate(1)
        else:
            direction.rotate(-1)
        
        max_x=max(x,max_x)
        max_y=max(y,max_y)
        min_x=min(x,min_x)
        min_y=min(y,min_y)

    print(abs(max_x-min_x)*abs(max_y-min_y))