# https://www.hackerrank.com/challenges/acm-icpc-team

N, M = (int(x) for x in input().split())
l = [input() for _ in range(N)]

t = []
for i in range(N-1):
    for x in range(i+1, N):
        t.append(bin(int(l[i], 2) | int(l[x], 2)).count('1'))

print(max(t))
print(t.count(max(t)))
