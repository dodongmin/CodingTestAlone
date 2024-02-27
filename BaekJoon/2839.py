sugar = int(input())

def function(sugar):
    answer = 0
    binil_5 = sugar // 5

    for i in range(binil_5,-1,-1):
        binil_3 = (sugar - i*5)  // 3
        if (5 * i + 3 * binil_3) == sugar:
            answer = i + binil_3
            break
        else:
            answer = -1

    return answer

print(function(sugar))

#40ms