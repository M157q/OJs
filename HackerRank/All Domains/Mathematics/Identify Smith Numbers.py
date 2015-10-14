# https://www.hackerrank.com/challenges/identify-smith-numbers

N = input()

def digit_sum(n):
    return sum(int(x) for x in n)

def prime_factors_digit_sum(n):
    primes = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            n /= i
            primes.append(str(i))

    if n > 1:
        n = int(n)
        primes.append(str(n))

    return sum(digit_sum(x) for x in primes)

if digit_sum(N) == prime_factors_digit_sum(int(N)):
    print(1)
else:
    print(0)
