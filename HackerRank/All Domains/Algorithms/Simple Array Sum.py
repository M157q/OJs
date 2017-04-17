#!/bin/python3

# https://www.hackerrank.com/challenges/simple-array-sum

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(sum(arr))
