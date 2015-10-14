# https://www.hackerrank.com/challenges/manasa-and-stones

T = int(input())

for _ in range(T):
    n = int(input())
    a = int(input())
    b = int(input())
    ans = []

    for i in range(n):
        ans.append(str(a*i + b*(n-1-i)))

    print(' '.join(sorted(set(ans), key=int)))
