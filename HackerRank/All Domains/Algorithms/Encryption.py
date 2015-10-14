# https://www.hackerrank.com/challenges/encryption

import math

L = input()
c = math.ceil(math.sqrt(len(L)))

print(' '.join(''.join(L[i::c]) for i in range(c)))
