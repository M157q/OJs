# https://www.hackerrank.com/challenges/angry-children

N = int(input())
K = int(input())
s = sorted([int(input()) for _ in range(N)])
d = [s[i+K-1] - s[i] for i in range(N-K+1)]
print(min(d))
