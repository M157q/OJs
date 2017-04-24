# https://www.hackerrank.com/challenges/30-review-loop

T = int(input())

for _ in range(T):
    S = input()
    print("{} {}".format(S[::2], S[1::2]))
