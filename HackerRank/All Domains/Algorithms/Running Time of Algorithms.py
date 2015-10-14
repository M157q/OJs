# https://www.hackerrank.com/challenges/runningtime

s = int(input())
ar = [_ for _ in map(int, input().split())]

def insertion_sort(ar, n):
    shift = 0
    for i in reversed(range(1, n+1)):
        if ar[i-1] > ar[i]:
            ar[i-1], ar[i] = ar[i], ar[i-1]
            shift += 1
    return shift

shift_count = 0
for i in range(1, s):
    shift_count += insertion_sort(ar, i)
print(shift_count)
