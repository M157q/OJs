# https://www.hackerrank.com/challenges/halloween-party

t = int(input())

for _ in range(t):
    k = int(input())
    x = int(k/2)
    print(x*(k-x))
