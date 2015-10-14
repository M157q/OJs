# https://www.hackerrank.com/challenges/sherlock-and-squares

T = int(input())

for _ in range(T):
    A, B = (int(x) for x in input().split())
    x = A**(1/2)
    x = int(x) if x.is_integer() else int(x)+1
    y = int(B**(1/2)) + 1
    print(len(range(x, y)))
