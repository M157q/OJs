# https://www.hackerrank.com/contests/projecteuler/challenges/euler001

def sum_divisible(i, n):
    return int(i * ((n//i) * ((n//i)+1) >> 1))

def target(n):
    return sum_divisible(3, n) + sum_divisible(5, n) - sum_divisible(15, n)

T = int(input())

for _ in range(T):
    N = int(input())
    print(target(N-1))


    #if N > s[-1]:
        #s.extend([x for x in range(s[-1]+1, N) if x % 3 == 0 or x % 5 == 0])
    #print(sum(filter(lambda x: x < N, s)))
