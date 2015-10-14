# https://www.hackerrank.com/challenges/angry-professor

n = int(input())

for _ in range(n):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    if len(list(filter((0).__ge__, a))) >= k:
        # >= k students entered classroom on time
        print('NO')
    else:
        print('YES')
