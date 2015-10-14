# https://www.hackerrank.com/challenges/make-it-anagram

import string

A = input()
B = input()

print(sum( abs(A.count(c) - B.count(c)) for c in string.ascii_lowercase ))
