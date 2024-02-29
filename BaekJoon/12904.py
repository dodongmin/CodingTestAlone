s = list(input())
t = list(input())

def function(s, t):
    while len(s) != len(t):
        if t[-1] == 'A':
            t.pop()
        else:
            t.pop()
            t = t[::-1]

    if s == t:
        return 1
    else:
        return 0

print(function(s, t))