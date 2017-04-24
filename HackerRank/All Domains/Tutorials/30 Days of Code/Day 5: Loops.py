# https://www.hackerrank.com/challenges/30-loops

#!/bin/python3

n = int(input().strip())

for i in range(1, 11):
    print("{} x {} = {}".format(n, i, n*i))
