# https://www.hackerrank.com/challenges/30-conditional-statements

#!/bin/python3

N = int(input().strip())

s = "Weird"

if N % 2 == 0 and (2 <= N <= 5 or N > 20):
    s = "Not " + s

print(s)
