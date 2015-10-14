# https://www.hackerrank.com/challenges/chocolate-feast

T = int(input())

for i in range(T):
    N, C, M = str(input()).split()

    ans = int(N) // int(C)

    eat = ans
    left_wrappers = 0

    while eat+left_wrappers >= int(M):
        eat, left_wrappers = divmod(eat+left_wrappers, int(M))
        ans += eat

    print(ans)
