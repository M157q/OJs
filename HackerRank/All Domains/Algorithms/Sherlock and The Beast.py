# https://www.hackerrank.com/challenges/sherlock-and-the-beast

T = int(input())

for _ in range(T):
    N = int(input())

    for i in range(N+1):
        x = '5'*(N-i) + '3'*i

        if x.count('3') % 5 == 0 and x.count('5') % 3 == 0:
            print(x)
            break
    else:
        print(-1)
