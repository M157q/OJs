# https://www.hackerrank.com/challenges/gem-stones

N = int(input())
# make every string into a set and find the number of the element in the intersection of these sets
print(len(set.intersection(*[set(input()) for _ in range(N)])))

#import functools
#print(len(functools.reduce(set.__and__, [set(input()) for _ in range(N)])))
