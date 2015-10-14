# https://www.hackerrank.com/challenges/service-lane

n, t = input().split()
width = []

for x in input().split():
    width.append(int(x))

for x in range(int(t)):
    i, j = input().split()
    print(min(width[int(i):int(j)+1]))
