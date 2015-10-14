# https://www.hackerrank.com/challenges/filling-jars

N, M = map(int, input().split())
sum = 0

for _ in range(M):
    a, b, k = map(int, input().split())
    sum += (b-a+1)*k

print(int(sum/N))
