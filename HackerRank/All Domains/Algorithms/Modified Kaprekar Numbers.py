# https://www.hackerrank.com/challenges/kaprekar-numbers

p = int(input())
q = int(input())
ans = []

for n in range(p, q+1):
    d = len(str(n))
    s = str(n**2)

    if len(s) % 2:
        l = s[0:d-1]
        r = s[d-1:]
    else:
        l = s[0:d]
        r = s[d:]

    if len(s) == 1:
        if n == int(n**2):
            ans.append(str(n))
    elif n == int(l) + int(r):
        ans.append(str(n))

if ans:
    print(' '.join(ans))
else:
    print('INVALID RANGE')
