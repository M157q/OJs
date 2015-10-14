# https://www.hackerrank.com/contests/projecteuler/challenges/euler002

s = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

T = int(input())
for _ in range(T):
    N = int(input())

    while N > (s[-1]+s[-2]):
        s.append(s[-1]+s[-2])

    print(sum(filter(lambda x: x <= N and x % 2 == 0, s)))
