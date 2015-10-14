# https://www.hackerrank.com/challenges/utopian-tree

n = int(input())

for i in range(n):
    m = int(input())
    h = 1
    for x in range(1, m+1):
        if x % 2:
            h *= 2
        else:
            h += 1
    print(h)
