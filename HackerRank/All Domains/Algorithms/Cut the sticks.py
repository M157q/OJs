# https://www.hackerrank.com/challenges/cut-the-sticks

n = int(input())
a = list(map(int, input().strip().split()))

while len(set(a)) >= 1:
    print(len(a))
    a = list(filter(sorted(a)[0].__ne__, a))
