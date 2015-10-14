# https://www.hackerrank.com/challenges/anagram

import string

T = int(input())

for _ in range(T):
    S = input()

    if len(S) % 2:
        print(-1)
    else:
        S1 = S[:len(S)//2]
        S2 = S[len(S)//2:]
        print(sum( abs(S1.count(c) - S2.count(c)) for c in string.ascii_lowercase ) // 2)

