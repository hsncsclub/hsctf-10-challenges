#!/usr/bin/env python3
from random import randint

flag = "flag{gr33dy_4lg0r1thm_048cc38517}"

def solve(a):
    a.sort(key = lambda x: (x[1], x[0]))
    res = 0
    t = 0
    for pair in a:
        t = max(t, pair[0])
        if pair[1] - t < 10:
            continue
        res += 1
        t += 10
    return res

def solve2(a):
    a.sort()
    res = 0
    t = 0
    for pair in a:
        t = max(t, pair[0])
        if pair[1] - t < 10:
            continue
        res += 1
        t += 10
    return res


N_arr = [5, 100, 100, 100, 100]
try:
    wrong = False
    for n in N_arr:
        pairs = []

        for i in range(n):
            a = randint(0, 6*n)
            b = a + randint(10, 20)
            pairs.append((a, b))
        
        ans2 = solve2(pairs)
        ans1 = solve(pairs)

        print(n)
        for pair in pairs:
            print(str(pair[0]) + " " + str(pair[1]))
        x = input()
        if int(x) != ans1 and int(x) != ans2:
            wrong = True
            break
    if not wrong:
        print(flag)
except:
    print("Something went wrong")
