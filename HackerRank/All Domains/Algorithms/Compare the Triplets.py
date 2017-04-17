#!/bin/python3

# https://www.hackerrank.com/challenges/compare-the-triplets?h_r=next-challenge&h_v=zen

# Solution 1
A = map(int, input().strip().split(' '))
B = map(int, input().strip().split(' '))

comparisons = [(a-b) for a, b in zip(A, B)]

print(
    "{} {}".format(
        sum(map(lambda x: x > 0, comparison)),
        sum(map(lambda x: x < 0, comparison)),
    )
)


# Solution 2
comparisons = [(a-b)/abs(a-b) if (a-b) else 0 for a, b in zip(A, B)]

print("{} {}".format(comparisons.count(1), comparisons.count(-1)))
