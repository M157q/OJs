# https://www.hackerrank.com/challenges/insertionsort2

s = int(input())
ar = [_ for _ in map(int, input().split())]

def insertion_sort(ar, n):
    for i in reversed(range(1, n+1)):
        if ar[i-1] > ar[i]:
            ar[i-1], ar[i] = ar[i], ar[i-1]

    print(' '.join(map(str, ar)))

for i in range(1, s):
    insertion_sort(ar, i)
