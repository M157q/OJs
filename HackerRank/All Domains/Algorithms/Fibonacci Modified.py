# https://www.hackerrank.com/challenges/fibonacci-modified

A, B, N = map(int, input().split())

def f(n):
    if n == 1:
        return A
    elif n == 2:
        return B
    else:
        return f(n-1)**2 + f(n-2)

print(f(N))
