# https://www.hackerrank.com/challenges/insertionsort1

s = int(input())
ar = [i for i in map(int, input().split())]
v = ar[-1]

for i in reversed(range(s-1)):

    if ar[i] > v:
        ar[i+1] = ar[i]
        print(' '.join(map(str, ar)))
        if i == 0:
            ar[i] = v
            print(' '.join(map(str, ar)))
    else:
        ar[i+1] = v
        print(' '.join(map(str, ar)))
        break
