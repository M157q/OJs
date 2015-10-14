# https://www.hackerrank.com/challenges/pangrams

import string

s = input().strip().lower()

if all([s.count(i) for i in string.ascii_lowercase]):
    print("pangram")
else:
    print("not pangram")
