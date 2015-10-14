# https://www.hackerrank.com/challenges/find-digits

t = int(input())

for _ in range(t):
    n = input()
    ans = 0
    for x in n:
        if int(x) and int(n)%int(x) == 0:
            ans += 1
    print(ans)
