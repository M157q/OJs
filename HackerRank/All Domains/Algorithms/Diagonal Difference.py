#!/bin/python3

# https://www.hackerrank.com/challenges/diagonal-difference

n = int(input().strip())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().strip().split(' ')])
d1_sum = sum(matrix[i][i] for i in range(n))

left_rotate_matrix = list(zip(*reversed(matrix)))
d2_sum = sum(left_rotate_matrix[i][i] for i in range(n))

print(abs(d1_sum - d2_sum))
