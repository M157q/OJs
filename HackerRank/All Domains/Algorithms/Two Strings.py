# https://www.hackerrank.com/challenges/two-strings

T = int(input())

for _ in range(T):
    A = input()
    B = input()

    if len(set(A) & set(B)):
        print('YES')
    else:
        print('NO')
