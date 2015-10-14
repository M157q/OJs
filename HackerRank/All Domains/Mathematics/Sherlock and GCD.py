# https://www.hackerrank.com/challenges/sherlock-and-gcd

from fractions import gcd
from functools import reduce

T = int(input())
for _ in range(T):
    N = int(input())
    s = tuple(int(x) for x in input().split())
    print("YES") if 1 in s or reduce(gcd, s) == 1 else print("NO")
