# https://www.hackerrank.com/challenges/cavity-map

n = int(input())

map = []
for _ in range(n):
    map.append(input())

for i in range(n):
    s = ''
    for j in range(n):
        if 0 < i < n-1 and 0 < j < n-1 and all((map[i][j] > x for x in [map[i-1][j], map[i+1][j], map[i][j-1], map[i][j+1]])):
            s += 'X'
        else:
            s += map[i][j]
    print(s)
