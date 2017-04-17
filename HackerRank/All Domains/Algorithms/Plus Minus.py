#!/bin/python3

# https://www.hackerrank.com/challenges/plus-minus?h_r=next-challenge&h_v=zen

n = int(input().strip())
array = [int(x) for x in input().strip().split(' ')]

custom_filter = lambda f: len(list(filter(f, array))) / n
custom_print = lambda n: print("{:6f}".format(n))

custom_print(custom_filter(lambda x: x > 0))
custom_print(custom_filter(lambda x: x < 0))
custom_print(custom_filter(lambda x: x == 0))
