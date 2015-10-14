# https://www.hackerrank.com/challenges/game-of-thrones

s = input()
print("NO") if [s.count(c) % 2 for c in set(s)].count(1) > 1 else print("YES")
