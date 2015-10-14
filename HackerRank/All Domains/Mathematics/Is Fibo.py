# https://www.hackerrank.com/challenges/is-fibo

def check_fibo(num):
    a, b = 0, 1
    while True:
        if b == num:
            return True
        if a > num:
            return False
        a, b = b, a+b

T = int(input())

for _ in range(T):
    N = int(input())

    if check_fibo(N):
        print('IsFibo')
    else:
        print('IsNotFibo')
