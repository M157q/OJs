# https://www.hackerrank.com/challenges/maximizing-xor

#!/usr/bin/python3

def maxXor(l, r):
  return max([x^y for x in range(l, r+1) for y in range(x, r+1)])
if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))
